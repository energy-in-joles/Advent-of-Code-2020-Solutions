import re
from itertools import product

def main():
  with open('inits.txt', 'r') as File:
    inits = [init.strip() for init in File]
  print(f"Part 1: {Part1(inits)}")
  print(f"Part 2: {Part2(inits)}")

def Part1(inits):
  mem = {}
  for init in inits:
    if re.search('mask = ', init): # extract and replace current mask
      mask = re.search(r'(?<=mask = ).+', init)[0]
    else:
      number = int(re.search(r'(?<=] = )(\d+)', init)[0]) # extract number being set to mem loc
      loc = int(re.search(r"(?<=mem\[)\d+(?=\])", init)[0]) # extract mem loc
      number_bin = f"{number:036b}" # format to be bit size 36, so same size as mask
      new_number = int(''.join(mask[n] if mask[n] != 'X' else number_bin[n] for n in range(len(mask))), 2) # replace number_bin with mask if not x. Then, convert to int
      mem[loc] = new_number # set mem loc as number, overwrite if loc has been visited before
  return sum(mem.values()) # get sum of all values in memory

def Part2(inits):
  mem = {}
  for init in inits:
    if re.search('mask = ', init):
      mask = re.search(r'(?<=mask = ).+', init)[0]
    else:
      number = int(re.search(r'(?<=] = )(\d+)', init)[0]) # extract number being set to mem loc
      loc = int(re.search(r"(?<=mem\[)\d+(?=\])", init)[0]) # extract mem loc
      loc_bin = f"{loc:036b}"
      masked_loc = ''.join(loc_bin[n] if mask[n] == "0" else mask[n] for n in range(len(mask))) # masked but replace X later
      x_locs = [n for n in range(len(masked_loc)) if masked_loc[n] == "X"] # find all locations of "X" in binary string
      # product() get all possible combinations to replace "X"s (use cartesian product)
      # ie 0X01X0: (1, 0), (0, 1), (0, 0), (1, 1) as each X can be 0 or 1
      for x_perm in product("01", repeat=len(x_locs)): # for each set of combinations, replace the "X"s in loc values
        for i, x_loc in enumerate(x_locs):
          masked_loc = masked_loc[:x_loc] + x_perm[i] + masked_loc[x_loc + 1:]
        mem[int(masked_loc, 2)] = number # set new memory loc as number
  return sum(mem.values())


if __name__ == "__main__":
    main()
