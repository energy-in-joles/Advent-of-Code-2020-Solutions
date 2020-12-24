tob_map = []

# parse toboggan map into list: tob_map[row][column]
with open('map.txt', 'r') as file:
  for x in file:
    tob_map.append(x.strip("\n"))
col_len = len(tob_map[0])


# Part 1
col_counter = 0 # keep counting column
tree_counter = 0 # tree_counter
col_len = len(tob_map[0])  # register the column size
# tobagon moves 3 steps to right and 1 down. If exceeds column size, loop around to left of map
for row in range(1, len(tob_map)):
  col_counter += 3
  column = col_counter % col_len  # thought this is kinda cool, floor to keep counter within 0 to 30
  position = tob_map[row][column]
  if position == "#":  # "#" is a tree, if crash into tree, count
    tree_counter += 1
print(f"Part 1: {tree_counter}")


# Part 2: Part 1, but multiply result of a few tries (Using a function)
def count_tob_trees(row_step, column_step, map_lst, column_length):
  col_counter = 0
  tree_counter = 0
  for row in range(row_step, len(tob_map), row_step):
    col_counter += column_step
    column = col_counter % column_length
    position = tob_map[row][column]
    # tob_map[row] = tob_map[row][:column] + "X" + tob_map[row][(column + 1):]  (draw out position traversal using X)
    # print(tob_map[row])
    if position == "#":
      tree_counter += 1
  return tree_counter

print(f"""Part 2: {
      count_tob_trees(1, 1, tob_map, col_len) *
      count_tob_trees(1, 3, tob_map, col_len) *
      count_tob_trees(1, 5, tob_map, col_len) *
      count_tob_trees(1, 7, tob_map, col_len) *
      count_tob_trees(2, 1, tob_map, col_len)}""")
