def main(Part):
  with open('seats.txt', 'r') as file:
    seats = ["." + row.strip() + "." for row in file] # add dot border to prevent error for easier 3x3 sweep
  col_nums = len(seats[0])
  seats = [col_nums * "."] + seats + [col_nums * "."]
  row_nums = len(seats)
  seated_count = 0 # keep count of occupied seats for Part 1
  seat_pos = [(i, j) for i in range(1, row_nums - 1) for j in range(1, col_nums - 1) if seats[i][j] != "."]
  neighbour_dict = {} # dict of 3x3 neighbouring seats for part 1
  if Part == 1:
    to_neighbour_dict(seat_pos, neighbour_dict, seats)
    min_seat_vacate = 4 # minimum number of seats filled to cause vacate
  elif Part == 2:
    to_direction_dict(seat_pos, neighbour_dict, seats, row_nums, col_nums)
    min_seat_vacate = 5
  # get list of seat positions (prevent unnecessary iteration through floor spaces)
  while True:
    seats_copy = seats.copy() # create a copy of initial cycle's state that is not changed
    for i, j in seat_pos:
      if seats[i][j] == "#" and vacate(min_seat_vacate, i, j, neighbour_dict, seats): # if seat is occupied and can be vacated
        seats_copy[i] = seats_copy[i][:j] + "L" + seats_copy[i][j + 1:]
        seated_count -= 1
      if seats[i][j] == "L" and occupy(i, j, neighbour_dict, seats): # if seat is empty and can be occupied
        seats_copy[i] = seats_copy[i][:j] + "#" + seats_copy[i][j + 1:]
        seated_count += 1
    if seats_copy == seats:
      print(f"Part {Part}: {seated_count}")
      break
    seats = seats_copy # final state set as next cycle's initial state

def to_neighbour_dict(seat_pos, neighbour_dict, seat_lst): # Part 1: get list of neighbouring 3x3 seats (prevent excessive iteration over floor tile)
  for i, j in seat_pos:
    neighbour_dict[(i, j)] = [(o, k) for o in range(i-1, i+2) for k in range(j-1, j+2) if (o != i or k != j) and seat_lst[o][k] != "."]
  # append seat pos (empty or not) around coords (!= "." floor), as long as coord is not the centre_coord (target_coord)

def to_direction_dict(seat_pos, neighbour_dict, seat_lst, row_len, col_len): # Part 2: get list of first seats viewed for all 8 directions from seat
  for i, j in seat_pos:
    neighbour_dict[(i,j)] = (search(seat_lst, row_len - i - 1, i, j, (1, 0)) + # horizontal traversal
                             search(seat_lst, i, i, j, (-1, 0)) +
                             search(seat_lst, col_len - j - 1, i, j, (0, 1)) + # vertical traversal
                             search(seat_lst, j, i, j, (0, -1)) +
                             search(seat_lst, min(row_len - i - 1, col_len - j - 1), i, j, (1, 1)) + # diag down right
                             search(seat_lst, min(row_len - i - 1, j), i, j, (1, -1)) + # diag down left
                             search(seat_lst, min(i, col_len - j - 1), i, j, (-1, 1)) + # diag up right
                             search(seat_lst, min(i, j), i, j, (-1, -1))) # diag up left
  # uses min func as diagonals end at shortest row/col route length

# Part 2: search traversal in all 8 directions (uses multiplier to change traversal direction)
def search(seat_lst, range_x, row, col, mult): # multiplier concept taken from u/WilkoTom on r/adventofcode
  for x in range(1, range_x):
    if seat_lst[row + mult[0] * x][col + mult[1] * x] != ".":
      return [(row + mult[0] * x, col + mult[1] * x)]
  return []

def vacate(min_seat, row, col, coord_dict, seats_lst): # check if seat can be vacated (part 1) max seat: max number of seats before must be vacated
  count = 0
  for o, k in coord_dict[(row, col)]:
    if (o != row or k != col) and seats_lst[o][k] == "#":
        count += 1
        if count >= min_seat:
          return True
  return False

def occupy(row, col, coord_dict, seats_lst): # check if seat can be occupied (part 1)
  for o, k in coord_dict[(row, col)]:
      if (o != row or k != col) and seats_lst[o][k] == "#": # don't occupy if one of seats already occupied
        return False
  return True

if __name__ == "__main__":
    main(1)
    main(2)
