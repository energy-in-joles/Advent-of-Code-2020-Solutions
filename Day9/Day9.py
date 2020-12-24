import itertools

def main():
  with open('data.txt', 'r') as file:
    data = [int(line.strip()) for line in file]
    first_invalid = find_first_invalid(data, 2, 25)
  print(f"Part 1: {first_invalid}")
  print(f"Part 2: {find_contiguous_set(data, first_invalid)}")

# Part 1: Find first value that is not a sum of any two numbers in the subset of 25 numbers before it.
def find_first_invalid(data, ints_in_sum, preamble_len):
  preamble = [data[i] for i in range(preamble_len)] # create preamble (queue) of 25 numbers
  for j in range(preamble_len, len(data)):
    in_preamble = False
    for x in itertools.combinations(preamble, ints_in_sum):
      if sum(x) == data[j]: # if sum found, data[j] is valid
        in_preamble = True
        break
    if in_preamble == False: # after for loop, check if sum was found
      return data[j] # if not, return invalid data[j]
    preamble.pop(0) # remove first number in preamble and add number after preamble
    preamble.append(data[j])
  return

# CREDIT: Sliding window concept inspired from u/bpanthi977's comment in r/adventofcode
# Produce sliding window that adjusts forward and backward until sum of subarray is target_sum
def find_contiguous_set(A, sum_target):
  data_length = len(A)
  i = 1
  subarray = [A[i - 1], A[i]]  # initiate an array of first 2 elements
  current_sum = sum(subarray)  # and get sum
  while current_sum != sum_target:  # keep running until sum reached
    if i >= data_length - 1:  # prevent index error, indicate if sum never found
      print(f"ERROR: Sum of array smaller than {sum_target}")
      return
    if current_sum < sum_target:  # if current_sum less than sum_target, add elemnt after subarray
      i += 1
      current_sum += A[i]
      subarray.append(A[i])
    else:  # if sum of subarray too big, start dropping first element until size is less or equal to sum_target
      removed = subarray.pop(0)
      current_sum -= removed
  return min(subarray) + max(subarray)

if __name__ == "__main__":
    main()
