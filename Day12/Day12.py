def main():
  with open('directions.txt', 'r')as file:
    directions = [row.strip() for row in file]
  bearings = ['N','E','S','W']
  print(f"Part 1: {Part1(directions, bearings)}")
  print(f"Part 2: {Part2(directions, bearings)}")

def Part1(directions, bearings):
  move_count = {}
  for bearing in bearings:
    move_count[bearing] = 0
  facing_index = 1 # starts east, bearing[1] = E
  for direction in directions:
    command = direction[0] # first char in direction (F, N, E, etc)
    if command == 'N' or command == 'E' or command == 'S' or command == 'W':
      move_count[command] += int(direction[1:]) # add movement in direction
    elif command == "R": # rotate by shifting index, shifting along the bearings list
      facing_index = int((facing_index + (int(direction[1:]) / 90)) % 4)
    elif command == "L":
      facing_index = int((facing_index - (int(direction[1:]) / 90)) % 4)
    else: # condition for 'F' - forward
      move_count[bearings[facing_index]] += int(direction[1:]) # add movement in direction facing
  return abs(move_count['N'] - move_count['S']) + abs(move_count['E'] - move_count['W']) # manhatten dist

def Part2(directions, bearings):
  move_count = {'N':0,'E':0}
  waypoint_coords = {'N':1,'E':10,'S':0,'W':0} # inital waypoint coords relative to boat 1 unit N, 10 units E
  turn_index = 0
  for direction in directions:
    command = direction[0]
    if command == 'N' or command == 'E' or command == 'S' or command == 'W':
      waypoint_coords[command] += int(direction[1:]) # waypoint coords just keep adding, movement based on diff between N and S / E and W
    elif command == "R" or command == "L":
      turn_index = int((int(direction[1:]) / 90)) # determine how much to shift dictionary based on angle of rot
      if command == "R":
        waypoint_coords = {bearings[bearing_index] : waypoint_coords[bearings[(bearing_index - turn_index) % 4]] for bearing_index in range(len(bearings))}
        # shift coords to down the bearings list (simulate rotation)
      else: # command == 'L'
        waypoint_coords = {bearings[bearing_index] : waypoint_coords[bearings[(bearing_index + turn_index) % 4]] for bearing_index in range(len(bearings))}
    else:
      move_count['N'] += (waypoint_coords['N'] - waypoint_coords['S']) * int(direction[1:]) # only N, negative if S
      move_count['E'] += (waypoint_coords['E'] - waypoint_coords['W']) * int(direction[1:]) # only E, negative if W
  return abs(move_count['N']) + abs(move_count['E'])

if __name__ == "__main__":
    main()
