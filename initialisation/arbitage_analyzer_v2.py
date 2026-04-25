import pandas as pd

# 1. Defined constant market multipliers
STEAM_FEE = 0.15
CSFLOAT_DEPOSIT = 0.028
CSFLOAT_WITHDRAW = 0.02
SLIPPAGE = 0.01
MIN_VOLUME_HURDLE = 50

# 2. Loading data from CSV with try/except block
try:
    df = pd.read_csv(r'C:\Users\ryanp\Desktop\Extra\Skinomics\data\market_assets1.csv')
except FileNotFoundError:
    print("Error: 'market_assets1.csv' not found. Ensure it is in the same folder as this script.")
    exit()

# Data originally gathered in arbitage_analyzer.py
steam_market_data = {
    "AK-47 Inheritance (FT)": 67.50,
    "M4A1-S Printstream (FT)": 309.87,
    "USP-S Jawbreaker (FT)": 6.91
}

float_market_data = {
    "AK-47 Inheritance (FT)": 48.99,
    "M4A1-S Printstream (FT)": 213.19,
    "USP-S Jawbreaker (FT)": 4.32
}

# 3. Changing CSV to include these values
df['current_steam_price'] = df['skin_name'].map(steam_market_data)
df['current_float_price'] = df['skin_name'].map(float_market_data)
df.to_csv('market_assets1.csv', index=False)

# 4. Defining desired variables
df['steam_breakeven'] = df['buy_price'] / (1 - STEAM_FEE)
df['float_breakeven'] = (df['buy_price'] / (1 - CSFLOAT_WITHDRAW)) * (1 - CSFLOAT_DEPOSIT)
df['adjusted_steam_breakeven'] = df['steam_breakeven'] * (1 + SLIPPAGE)

print(f"--- Skinomics Quant Market Analysis ---")
# Print summary of table first
print(df[['skin_name', 'buy_price', 'steam_breakeven', 'float_breakeven']])

# 5. Breaking down each asset
print("\n--- Individual Asset Breakdown ---")
for index, row in df.iterrows():

    if 'current_steam_price' in row:
        market_price = row['current_steam_price']
        potential_margin = (market_price * (1 - STEAM_FEE)) - row['buy_price']
    else:
        market_price = 0.00
        potential_margin = -row['buy_price']

    volume = row['volume_24h']

# 6. Decision logic
    if potential_margin <= 0:
        decision = "AVOID - NEGATIVE MARGIN"
    elif volume < MIN_VOLUME_HURDLE:
        decision = "AVOID - LOW LIQUIDITY"
    else:
        decision = "ARBITRAGE VIABLE"

    # 7. Clean output per asset
    print(f"Asset: {row['skin_name']}")
    print(f"--------------------------")
    print(f"Buy Price:        ${row['buy_price']:.2f}")
    print(f"Steam Break-even: ${row['steam_breakeven']:.2f}")
    print(f"Float Break-even: ${row['float_breakeven']:.2f}")
    print(f"24h Volume:       {volume}")
    print(f"Estimated Profit: ${potential_margin:.2f}")
    print(f"Decision:         {decision}")
    print("-" * 26)
