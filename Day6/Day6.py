from string import ascii_lowercase
import re

def main():
  with open('responses.txt') as file:
    response_str = ''
    for row in file:
      response_str += row
  responses = response_str.strip().split("\n\n")
  # .strip needed to remove \n at end of document, then split by empty lines
  print(f"Part 1: {count_unique_chars(responses)}")

  char_lst = list(ascii_lowercase)  # get list of all alpha characters to check if char in
  print(f"Part 2: {count_overlap_chars(responses, char_lst)}")

# Part 1: get unique characters in each string to get all unique yes_responses for each group
def count_unique_chars(responses):
  count = 0
  for i in range(len(responses)):
    unique_response = ''.join(set(responses[i])).replace('\n', '') # set to get unique characters, then remove \n
    count += len(unique_response)
  return count

# Part 2: count number of character responded by every member of group
def count_overlap_chars(responses, char_lst):
  count = 0
  for i in range(len(responses)):
    string = ""
    peeps_in_grp = len(re.findall('\n', responses[i])) + 1 # use newlines to determine number of responses in group
    for ch in char_lst:
      if len(re.findall(ch, responses[i])) == peeps_in_grp: # if number of a character matches number of peeps, count it
        string += ch
        count += 1
  return count


if __name__ == "__main__":
    main()
