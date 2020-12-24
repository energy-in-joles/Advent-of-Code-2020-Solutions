import re
import math

def main():
  with open('passports.txt') as file:
    all_pass = ""
    for row in file:
      all_pass += row

  passes = all_pass.split("\n\n")
  counter_1 = 0
  counter_2 = 0

  # part 1: validate that all fields are present except for cid
  for pass_p in passes:
    byr = re.search(r"(?<=byr:)([^\n\s]*)", pass_p)  # find text after "[field]:" and before space or newline
    iyr = re.search(r"(?<=iyr:)([^\n\s]*)", pass_p)
    eyr = re.search(r"(?<=eyr:)([^\n\s]*)", pass_p)
    hgt = re.search(r"(?<=hgt:)([^\n\s]*)", pass_p)
    hcl = re.search(r"(?<=hcl:)([^\n\s]*)", pass_p)
    ecl = re.search(r"(?<=ecl:)([^\n\s]*)", pass_p)
    pid = re.search(r"(?<=pid:)([^\n\s]*)", pass_p)
    if (byr and iyr and eyr and hgt and hcl and ecl and pid):  # if not empty. ie. if field exists
      counter_1 += 1

      # Part 2: individual checks for each field
      if (year_validate(4, 1920, 2002, byr.group(0)) &  # byr check
          year_validate(4, 2010, 2020, iyr.group(0)) &  # iyr check
          year_validate(4, 2020, 2030, eyr.group(0)) &  # eyr check
          hgt_check(150, 193, 59, 76, hgt.group(0)) &
          hcl_check(hcl.group(0)) &
          ecl_check(ecl.group(0)) &
          pid_check(9, pid.group(0))):
        counter_2 += 1


  print(f"Part 1: {counter_1}")
  print(f"Part 2: {counter_2}")


# part 2 functions
def year_validate(n_digits, year_min, year_max, yr):  # used for byr/iyr/eyr
  try:
    year = int(yr)  # if not convertable, just ignore
  except:
    return False
  if int(math.log10(year)) + 1 == n_digits and year >= year_min and year <= year_max:  # check digits and year range
    return True
  return False

def hgt_check(cm_min, cm_max, in_min, in_max, hgt_str):  # check if ends with "cm" or "in"
  try:
    hgt_val = int(hgt_str[:-2])
  except:
    return False
  if hgt_str[-1] == "m" and hgt_str[-2] == "c" and hgt_val >= cm_min and hgt_val <= cm_max:  # if cm, check if within metric range
    return True
  elif hgt_str[-1] == "n" and hgt_str[-2] == "i" and hgt_val >= in_min and hgt_val <= in_max:  # if in, check if within imperial range
    return True
  return False

def hcl_check(hcl):
  if not (hcl[0] == "#" and len(hcl[1:]) == 6):
    return False
  for ch in hcl[1:]:
    if ch.isalpha():  # if ch is alphabet
      ch = ord(ch.lower())
      if ch < 97 or ch > 102:  # 97 is ord("a") and 102 is ord("102")
        return False
    elif not ch.isdigit(): # if some weird character not digit and not alpha
      return False
    # no digit check because digit can only be between 0 to 9 anyway
  return True

def ecl_check(ecl):  # eye colour check
  ecl = ecl.lower()
  ecl_types = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  if ecl in ecl_types: # if eye colour in list
    return True
  return False

def pid_check(digit_len, pid):  # check if it is digit and digit_len long
  if pid.isdigit() and len(pid) == digit_len:
    return True
  return False


if __name__ == "__main__":
    main()

