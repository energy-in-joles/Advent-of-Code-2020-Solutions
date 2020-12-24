import re

lst_min = []
lst_max = []
lst_char = []
lst_pass = []

with open('input.txt', 'r') as file: #append all numbers to a list
  for x in file:
    lst_min.append(re.findall(r"(\d+)(?:-)", x)[0])
    lst_max.append(re.findall(r"(?:-)(\d+)", x)[0])
    lst_char.append(re.findall(r"(?: )([a-z])(?:: )", x)[0])
    lst_pass.append(re.findall(r"(?:: )(.+)", x)[0])
counter = 0

# part 1: range of values used to match for characters in string
for i in range(len(lst_pass)):
  #eg \b([^a]*a[^a]*){2,4}\b match for "a" 2 to 4 times anywhere in string
  if re.match(fr"\b([^{lst_char[i]}]*{lst_char[i]}[^{lst_char[i]}]*){{{lst_min[i]},{lst_max[i]}}}\b", lst_pass[i]):
    counter += 1
print(f"Part 1: {counter}")
counter = 0

# part 2: exactly 1 of the index positions in lst_min and lst_max (index starts at 1) must contain character  in string
for j in range(len(lst_pass)):
  # using XOR operand where True True and False False are rejected. minus 1 because convert to index 0
  if (lst_pass[j][int(lst_min[j]) - 1] == lst_char[j]) ^ (lst_pass[j][int(lst_max[j]) - 1] == lst_char[j]):
    counter += 1
print(f"Part 2: {counter}")


