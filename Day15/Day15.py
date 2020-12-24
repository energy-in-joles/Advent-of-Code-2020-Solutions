def main():
  with open('game.txt', 'r') as File:
    nums = [int(x) for x in ''.join(num for num in File).split(',')] # get list of int(numbers) split by ","
  print(f"Part 1: {find(nums, 2020)}")
  print(f"Part 2: {find(nums, 30000000)}")

def find(nums_lst, turn_n):
  nums_dict = {nums_lst[i] : i for i in range(len(nums_lst))} # create a dict {value : position} (last position of value)
  before = nums_lst[-1] # first "before" (last round) value to look at is the last starting number
  for i in range(len(nums_lst), turn_n):
    if before in nums_dict:
      current = i - 1 - nums_dict[before] # if "before" value appeared before, current = "before" position - position of last apearance of "before" value
    else:
      current = 0 # if "before" value is first appearance, current = 0
    nums_dict[before] = i - 1 # set the last appearance of the "before" value as "before"s position as it is now the value's last appearance
    before = current # next round, so current is next round's before
  return current

if __name__ == "__main__":
  main()

# idea to replace list with before,current values inspired from u/Jozkings on r/adventofcode
