import re

def main(Part = 1):
  with open('math.txt', 'r') as File:
    equations = [line.strip() for line in File]
  # Part 1: Left to right operations
  sum = 0
  for equation in equations:
    while re.search(r"\([^\(\)]+\)", equation): # while brackets exists
      bracket_match = re.search(r"(?<=\()[^\(\)]+(?=\))", equation)
      # find inner brackets first, then outer (reject brackets inside search field)
      equation = equation[:bracket_match.start(0) - 1] + str(weird_operate(bracket_match.group(0), Part)) + equation[bracket_match.end(0) + 1:]
    sum += weird_operate(equation, Part)
  print(f"Part {Part}: {sum}")

def weird_operate(short_exp, Part):
  if Part == 1:
    return LtoR_operate(short_exp)
  elif Part == 2:
    return Addfirst_operate(short_exp)
  else:
    print(f"INVALID: Part {Part} does not exist.")
    exit()
# Part 1: left to right operation
def LtoR_operate(short_exp):
  while re.search(r"\d+ [\*\+] \d+", short_exp): # while operations still not calculated in expression
    match = re.search(r"\d+ [\*\+] \d+", short_exp) # get first result of "number */+ number"
    end = match.end(0) # get positions of the new operations
    exp = match.group(0) # get expression
    equals = add_or_prod(exp) # run operation from collected in line 17
    short_exp = f"{equals} {short_exp[end + 1:]}" # replace calculated number in expression
  return int(short_exp)

# Part 2: add then multiply
def Addfirst_operate(short_exp):
  operator_strings = [r"\d+ \+ \d+", r"\d+ \* \d+"] # do add first, then multiply
  for string in operator_strings:
    while re.search(string, short_exp):
      match = re.search(string, short_exp) # similar process to above
      start = match.start(0)
      end = match.end(0)
      exp = match.group(0)
      equals = add_or_prod(exp)
      short_exp = f"{short_exp[:start]}{equals}{short_exp[end:]}"
  return int(short_exp)

def add_or_prod(short_exp):
  exp_items = short_exp.split(" ") # break "num +/* num" into [num, operator, num]
  if exp_items[1] == "+":
    return int(exp_items[0]) + int(exp_items[2])
  elif exp_items[1] == "*":
    return int(exp_items[0]) * int(exp_items[2])
  else:
    print(f"ERROR: {exp_items[1]} is an unknown operation.")
    exit()

if __name__ == "__main__":
  main(1)
  main(2)
