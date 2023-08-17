def exp_gain(base_yield, wild_lvl, lvl, modifiers):
    multiplier = ((base_yield * wild_lvl) / 5) * (( 2 * wild_lvl + 10)  / (lvl + wild_lvl + 10)) ** 2.5 + 1
    for modifier in modifiers:
        multiplier = multiplier * modifier
    return multiplier




###### MAIN #####

base_yield = 395
modifiers = [1.5]
lvl = 85
wild_lvl = 55
gain = exp_gain(base_yield, wild_lvl, lvl, modifiers)
print(gain)