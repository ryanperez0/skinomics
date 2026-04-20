# Lets take 3 of the most popular assets on the market
# Note: every asset has a 'class' - the skin may be the same but the lower the 'float' the more expensive

# Field-Tested is the median asset class
steam_prices = {
    "AK-47 | Inheritance (Field-Tested)" : 67.50 , "M4A1-S | Printstream (Field-Tested)" : 309.87 ,
    "USP-S | Jawbreaker (Field-Tested)" : 6.91
}

float_prices = {
"AK-47 | Inheritance (Field-Tested" : 48.99 , "M4A1-S | Printstream (Field-Tested)" : 213.19 ,
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

    steaminput = input(print(f"Would you like the break even price for {skin_name} on Steam? (Y/N)"))
    if steaminput == "Y" or steaminput == "y":
        print(f" The final break-even steam price for {skin_name} is {round(breakevensteam, 2)}, adjusted to 1% risk fee would be {round(breakevensteam * (1 + slippage), 2)}")

print()

for skin_name, skin_price in float_prices.items():
    breakevenfloat = skin_price / (1 - csfloat_withdraw) * (1 - csfloat_deposit)
    print(f" The final break-even CSFloat price for {skin_name} is {round(breakevenfloat, 2)}")

