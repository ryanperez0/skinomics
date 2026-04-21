# Objective: To identify price discrepancies between Steam and 3rd party markets
# Constraint: Incorporating a 15% Steam "sink" and 3rd party withdrawal frictions.

# Note: This file is unfinished: code framework will be used later once pandas is integrated - moving onto CSV manipulation


# Field-Tested is the median asset class
steam_prices = {
    "AK-47 | Inheritance (Field-Tested)" : 67.50 , "M4A1-S | Printstream (Field-Tested)" : 309.87 ,
    "USP-S | Jawbreaker (Field-Tested)" : 6.91
}

float_prices = {
"AK-47 | Inheritance (Field-Tested)" : 48.99 , "M4A1-S | Printstream (Field-Tested)" : 213.19 ,
    "USP-S | Jawbreaker (Field-Tested)" : 4.32
}

# Previously explained data from calc.py
csfloat_deposit = 0.028
csfloat_withdraw = 0.02
steam_fee = 0.15

# Let's also introduce a 'slippage' factor to account for risk and market volatility
slippage = 0.01

print(f"--- Skinomics Quant Market Analysis ---")
print()


for skin_name, skin_price in steam_prices.items():
    breakevensteam = skin_price / (1 - steam_fee)
    f_price = float_prices[skin_name]

print()

for skin_name, skin_price in float_prices.items():
    breakevenfloat = skin_price / (1 - csfloat_withdraw) * (1 - csfloat_deposit)
    print(f" The final break-even CSFloat price for {skin_name} is {round(breakevenfloat, 2)}")



print(f"""
Asset: {skin_name}
--------------------------
Steam Break-even: {breakevensteam}
Float Break-even: {breakevenfloat}
Gross Spread:
Decision: [Arbitrage Viable / Avoid]
""")

