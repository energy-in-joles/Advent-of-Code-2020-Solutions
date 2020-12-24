from math import ceil, floor

def main():
  seat_bins = []
  seat_ids = []
  with open('seats.txt','r') as file:
    for row in file:
      seat = row.strip("\n")
      seat_bins.append(seat)
  max_id = 0
  for seat in seat_bins:
    row = row_col_find(seat, "B", "F", 128) # B: upper half, F: lower half (128 rows)
    col = row_col_find(seat, "R", "L", 8) # R: upper half, L: lower half (8 columns)
    seat_id = row * 8 + col
    seat_ids.append(seat_id)
    # Part 1: Find the largest ID
    if max_id < seat_id:
      max_id = seat_id
  print(f"Part 1: {max_id}")

  seat_ids = sorted(seat_ids)
  print(f"Part 2: {find_my_seat(seat_ids)}")

def row_col_find(seat, upper_char, lower_char, row_col_max, row_col_min=1):
  if seat[0] == lower_char:
    row_col_max = floor(((row_col_max - row_col_min) / 2) + row_col_min)  # floor to get the lower of .5
  elif seat[0] == upper_char:
    row_col_min = ceil(((row_col_max - row_col_min) / 2) + row_col_min)  # ceil to get upper of .5
  if row_col_max == row_col_min:
    return row_col_max - 1 # base case, when no more upper_char or lower_char commands
  return row_col_find(seat[1:], upper_char, lower_char, row_col_max, row_col_min)
  # this needs to be returned, if not the return value will be lost in recursion and returns NONE

def find_my_seat(lst): # find missing number in sorted list
  number = lst.pop(0) # removes index 1 and also gives first number in consecutive sequence
  for i in lst:
    if i == number + 1:
      number += 1
    else:
      return number + 1


if __name__ == "__main__":
    main()
