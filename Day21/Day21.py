import re
from collections import Counter

with open('foods.txt', 'r') as File:
  foods = ''.join(food for food in File).strip().split('\n')

allergen_count = {}
allergen_ingred = {}
unknown_ingred_lst = []
for food in foods:
  unknown = re.search(r'.+(?= \()', food).group(0).split(" ") # get list of unknown ingredients and known allergens
  known = re.search(r'(?<=contains ).+(?=\))', food).group(0).split(', ')
  unknown_ingred_lst += unknown # add ingredient to big list
  for allergen in known:
    if allergen in allergen_count:
      allergen_count[allergen] += 1 # keep count of allergen appearance
      allergen_ingred[allergen] += unknown.copy() # append list of possible ingredients appearing with each known allergen
    else: # if first time seeing allergen, create new key for both dicts
      allergen_count[allergen] = 1
      allergen_ingred[allergen] = unknown.copy()
sus_ingreds = [] # create list of all ingredients that cause allergies
for allergen in allergen_ingred:
  possible_allergens = [item for item, n in Counter(allergen_ingred[allergen]).items() if n == allergen_count[allergen]]
  # if the number of allergen apperances matches number of ingredient appearances beside it, means it could be the allergen
  sus_ingreds += possible_allergens
  allergen_ingred[allergen] = possible_allergens # for part 2: remove all ingredients that are now deemed as impossible to contain the allergen
sus_ingreds = set(sus_ingreds)
count = sum(1 for ingred in unknown_ingred_lst if ingred not in sus_ingreds) # count total appearance of ingreds that are not suspicious
print(f"Part 1: {count}")

confirmed_allergen = {}
while allergen_ingred: # while dictionary is not empty
  for allergen in allergen_ingred:
    if len(allergen_ingred[allergen]) == 1: # if only 1 ingred linked to allergen, ingred must == allergen
      confirmed = allergen_ingred.pop(allergen)[0] # remove allergen key and extract confirmed ingredient linked to it
      confirmed_allergen[allergen] = confirmed
      for allergen in allergen_ingred:
        if confirmed in allergen_ingred[allergen]:
          allergen_ingred[allergen].remove(confirmed) # remove confirmed ingred from other allergens as confirmed not linked
      break
sorted_ingreds = ''.join(f"{confirmed_allergen[allergen]}," for allergen in sorted(confirmed_allergen.keys(), key=lambda x:x)).strip(',')
# write list of ingredients sorted alphabetically by corresponding allergen
print(f"Part 2: {sorted_ingreds}")
