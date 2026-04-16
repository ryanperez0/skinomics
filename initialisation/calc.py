# When looking at CS2 skins as economic assets,
# It is important to understand the difference between engaging with the Steam market and 3rd party sites due to differences in commission

# Hypothetical 15 purchase price, can be changed to account for actual price
purchase_price = 15
steam_fee = 0.15

# Csfloat is the leading 3rd party marketplace for these digital assets

csfloat_deposit = 0.028
csfloat_withdraw = 0.02

# Now onto the break even (added rounding function)

breakevensteam = purchase_price / (1- steam_fee)

breakevencsfloat = purchase_price / (1 - csfloat_deposit)

print(f" The break-even price for steam is {round(breakevensteam, 2)}")

print(f" The break-even price for CSFloat is {round(breakevencsfloat, 2)}")

# Now, the ratios

print(f" The transaction-cost ratio is {round( breakevencsfloat / breakevensteam , 2)}")

trans_cost_ratio = (breakevencsfloat / breakevensteam)

print(f" In turn the efficiency gap is {round(1- trans_cost_ratio, 2)} (2dp) , giving us {round(1- trans_cost_ratio, 2)} more buying power if we choose CSFloat marketplace!")

# In any case, withdrawing money back to your bank acc will always have a cost as it's not possible through steam

# Lets assume we always pick the more efficient marketplace

truebreakeven = breakevencsfloat / (1 - csfloat_withdraw)

print(f" Assuming we go with Float as the market leader, our true break even when including withdraw costs is {round(truebreakeven, 2)} ")
print(f" Or in pure math with variable asset costs where x = asset price, it is x / ((1 - 0.028) * (1- 0.02))")
