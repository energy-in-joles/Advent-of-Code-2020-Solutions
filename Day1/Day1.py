import itertools
# Interesting material: https://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number
# Challenge: given a list of integers, find the product of the integers that sum to 2020. part1: 2 integers that sum, part 2: 3 integers that sum.

with open('input.txt', 'r') as file: #append all numbers to a list
  lst = [int(row.strip()) for row in file]

# part 1: Using nested for loop
for i in range(len(lst)):
  for j in range(i+1, len(lst)): # start at i + 1 to prevent duplicate pairs ie. 1 2 and 2 1.
    if lst[i] + lst[j] == 2020:
        print(f"Part 1: {lst[i] * lst[j]}")

# part 2: Using Itertools
def prod_of_val_sum_n(sum_n, lst, val_count): # find product of [val_count] number of integers in [lst] that add to [sum_n]
  prod = 1
  for x in itertools.combinations(lst, val_count):
    if sum(x) == sum_n:
      for i in range(val_count):
        prod *= x[i]
  print(f"Part 2: {prod}")

prod_of_val_sum_n(2020, lst, 3)
#prod_of_val_sum_n(2020, lst, 2)
