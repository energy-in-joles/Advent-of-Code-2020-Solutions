import re

def main():
  with open('boot.txt', 'r') as file:
    code = [row.strip() for row in file]
    code_len = len(code)
    part1(code, code_len)
    part2(code, code_len)

# Part 1: print acc value on code execution before loop (any line repeated)
def part1(code, code_len):
  acc_val = code_reader(code, code_len)[0] # get acc value after loop detected
  print(f"Part 1: {acc_val}")

# Part 2: try to change jmp or nop until infinte loop broken
def part2(code, code_len):
  for line in range(code_len): # go through every line and replace jmp with nop or vice versa
    code_copy = code.copy()
    if code[line][:3] == "jmp":
      code_copy[line] = "nop"+ code[line][3:]
    elif code[line][:3] == "nop":
      code_copy[line] = "jmp"+ code[line][3:]
    acc_val, looped = code_reader(code_copy, code_len)
    if looped == False:
      print(f"Part 2: {acc_val}")
      return

# execute line of code until infinte loop detected or code execution finished (iterates out of code range)
def code_reader(code, code_len):
  line_nums = [j for j in range(code_len)]  # make list of line nums to detect if line is repeated
  i = 0
  acc_val = 0
  while i < code_len and isloop(code_len, line_nums, i) == False:
    if code[i][:3] == "acc":
      acc_val += action(code[i])
      i += 1
    elif code[i][:3] == "jmp":
      i += action(code[i])
    else:
      i += 1
  return acc_val, isloop(code_len, line_nums, i)

# Used for both jmp and acc. Extracts integer value in each command to execute
def action(line):
  return int(re.search(r"[+-]\d+", line).group())

# Detect if line number has already been visited.
def isloop(code_len, line_nums, curr_line_num):
  if curr_line_num >= code_len: # if line exceeds code lines, means no loop as code is finished
    return False
  if curr_line_num in line_nums:
    line_nums.remove(curr_line_num) # remove line num from list so that if line num appears again, loop detected
    return False
  else:
    return True


if __name__ == "__main__":
    main()
