import re
from collections import Counter
from operator import add

move_vectors = {'e':(0,1),'w':(0,-1),'ne':(.5,.5),'nw':(.5,-.5),'se':(-.5,.5),'sw':(-.5,-.5)} # ne,nw move by .5 and e/w move by 1
with open('tiles.txt', 'r') as File:
  tiles = [tile.strip() for tile in File]
vectors = []
for i, tile in enumerate(tiles): # read movement lines and determine vector from origin
  vector = (0,0)
  while tile:
    if tile[0] == 'e' or tile[0] == 'w':
      vector = tuple(map(add, vector, move_vectors[tile[0]]))
      tile = tile[1:]
    else:
      vector = tuple(map(add, vector, move_vectors[tile[:2]]))
      tile = tile[2:]
  vectors.append(vector)
tile_dict_black = {coord:1 for coord, count in Counter(vectors).items() if count % 2 != 0} # if tile flips in odd number, means it is black (since starts at white)
black_tile_count = len(tile_dict_black)
print(f"Part 1: {black_tile_count}") # print initial black tile count

adjacent_range = [vec for vec in move_vectors.values()] # range of neighbour vectors for each tile
for i in range(100): # almost identical to day 17
  tile_dict = {}
  for tile in tile_dict_black:
    for adj in adjacent_range:
      neighbour = tuple(map(add,adj,tile))
      if neighbour not in tile_dict_black:
        tile_dict[neighbour] = 0
  tile_dict.update(tile_dict_black) # add new surrounding white tiles to known black tiles
  for tile in tile_dict:
    blk_adj_count = 0
    for adj in adjacent_range:
      neighbour = tuple(map(add,adj,tile))
      if neighbour in tile_dict and tile_dict[neighbour] == 1: # count adjacent black tiles
        blk_adj_count += 1
        if blk_adj_count > 2: # don't bother searching after 2.
          break
    if tile_dict[tile] == 1 and (blk_adj_count == 0 or blk_adj_count > 2): # if number of adj black tiles is 0 or more than 2 and target is black
      del tile_dict_black[tile] # remove from black tile dict and black tile count - 1
      black_tile_count -= 1
    elif tile_dict[tile] == 0 and blk_adj_count == 2:
      tile_dict_black[tile] = 1 # opposite if number of adj black tiles is exactly 2 and target is white
      black_tile_count += 1

print(f"Part 2: {black_tile_count}")
