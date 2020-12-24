from math import factorial

def main():
  with open('test.txt', 'r') as file:
    joltages = sorted([int(joltage.strip()) for joltage in file])
  # Part 1: count number of j_dff of 1 and 3 and multiply
  j_1 = j_3 = 0
  in_j = 0 # input joltage
  diff_lst = []
  joltages.insert(0, in_j) # add to the front
  joltages.append(joltages[-1] + 3)  # append final output that is always 3 more than max adapter
  print(joltages)
  for i in range(len(joltages) - 1): # simple count of diff 1 and 3
    j_diff = joltages[i + 1] - joltages[i]
    diff_lst.append(j_diff)
    if j_diff == 1:
      j_1 += 1
    elif j_diff == 3:
      j_3 += 1
    elif j_diff != 2: # if j_diff == 2, ignore for Part 1
      print(f"ERROR: Voltage Difference larger than 3 between {joltages[i]} and {joltages[i + 1]}")

  print(f"Part 1: {(j_1) * (j_3)}")
  print(f"Part 2: {calculate_combis(3, diff_lst)}")
  better_part2_solution(joltages)
# Part 2: find number of combinations
# only block of diff = 1 can have numbers removed while not exceeding a difference of 3, so calculate combinations using blocks of 1.
# Solution makes 2 assumptions:
# Firstly, that there are only 2 cases: diff = 1 or 3 (which is true for all cases given)
# Secondly, that one_count - 1 (the len(consecutive block of diff = 1)) < max_diff (3) + 2 (too complicated to account for and not an issue for this problem)
# for max_diff of x, number of allowed consecutive 1s is x - 1
# n = one_count - 1 (ignore last 1 ignored because if last 1 removed, difference = 4)
# So the combinations of C for each block of 1s are nC(x-1) + nC(x-2) + ... + nC(1)
# total combinations equals produt of all 1s block combinations
def calculate_combis(max_diff, diff_lst):
  total_product = 1
  one_count = -1 # starts at -1 because last 1 ignored
  for diff in diff_lst:
    if diff == 1:
      one_count += 1 # count if difference is 1
    else:
      if one_count >= -1:
        n_sum = 1
        for j in range(1, max_diff):
          n_sum += combi(one_count, j)
        total_product *= n_sum # multiply all individual 1 block combinations
      one_count = -1
  return total_product

def combi(n, r):  # n choose r (implemented for use prior to python 3.8)
  if n < r:
    return 0 # return 0 instead of error
  return int(factorial(n) / (factorial(r) * factorial(n - r)))

#Taken from u/RobBobertsThe3rd's solution on r/adventofcode
def better_part2_solution(joltages):
  tribo_seq = [1] + [0 for i in range(1,len(joltages))]
  for i in range(1,len(tribo_seq)):
    tribo_seq[i] = sum(tribo_seq[o] for o in range(i-3,i) if joltages[o] + 3 >= joltages[i])
  print(tribo_seq)
  return tribo_seq[-1]

if __name__ == "__main__":
    main()
