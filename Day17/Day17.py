from itertools import product
from collections import Counter
from operator import add

def main():
  with open('conway.txt', 'r') as File:
    layers = [row.strip() for row in File]
  print(f"Part 1: {Find_Active(layers, 3, 6)}")
  print(f"Part 2: {Find_Active(layers, 4, 6)}")

def Find_Active(layers, dimensions, cycles):
  # first, get dictionary of active_coords coord:1 (1 for active, 0 for inactive)
  active_coord_dict = {(0,) * (dimensions - 2) + (y,x):1 for y in range(len(layers)) for x in range(len(layers[y])) if layers[y][x] == "#"}
  active = len(active_coord_dict) # get initial active count
  check_range = [x for x in product(range(-1,2), repeat=dimensions)] # get all neighbours, for any dimension
  check_range.remove((0,) * dimensions) # remove (0,0,0,0) search coord, that's itself!
  for i in range(cycles):
    coord_dict = {}
    for coord in active_coord_dict:
      for check in check_range:
        neighbour = tuple(map(add, coord, check)) # go through all neighbours of active coords
        if neighbour not in active_coord_dict: # if neighbour is not in active (not active), add to coord_dict
          coord_dict[neighbour] = 0 # these coords are impt as non_active coords also are altered in each cycle by neighbour actives
    coord_dict.update(active_coord_dict) # add back the active_coords
    for coord in coord_dict:
      active_neighbours = 0
      for check in check_range:
        neighbour = tuple(map(add, coord, check))
        if neighbour in coord_dict and coord_dict[neighbour] == 1: # count number of active neighbours
          active_neighbours += 1
          if active_neighbours > 3: # if exceeds 3, don't bother continuing
            break
      if coord_dict[coord] == 1 and active_neighbours != 2 and active_neighbours != 3: # active now inactive
        del active_coord_dict[coord]
        active -= 1 # keep updating active count
      elif coord_dict[coord] == 0 and active_neighbours == 3: # inactive now active
        active_coord_dict[coord] = 1
        active += 1
  return active

if __name__ == "__main__":
  main()
