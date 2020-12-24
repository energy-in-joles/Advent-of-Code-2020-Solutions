def main():
  final_cup = 1
  with open('cups.txt', 'r') as File:
    cups = [int(n) for n in ''.join(row for row in File)]
  max_cup = max(cups)
  cup_dict = shuffle(cups, max_cup, 100)
  i = final_cup
  final_string = ''
  while cup_dict[i] != final_cup: # loop through cups after cup 1 (if next cup is 1, means it is looping and end)
    final_string += str(cup_dict[i])
    i = cup_dict[i]
  print(f"Part 1: {final_string}")

  #Part 2: 1 mil cups and 10 mil cycles
  cups = cups + [cup for cup in range(max_cup + 1,1000001)]
  cup_dict = shuffle(cups, cups[-1], 10000000)
  print(f"Part 2: {cup_dict[final_cup] * cup_dict[cup_dict[final_cup]]}")

# solved using linked lists: dictionary is cup:next-cup (clockwise)
def shuffle(cups, max_cup, cycles):
  cup_dict = {cups[i]:cups[i + 1] for i in range(len(cups) - 1)}
  cup_dict[cups[-1]] = cups[0] # create a looping linked list, last item loops back to first
  current = next(iter(cup_dict)) # start with the first cup
  for i in range(cycles):
    pickup_lst = [] # get a list of the 3 cups after current card
    pickup_pt = current
    for j in range(3):
      pickup_lst.append(cup_dict[pickup_pt])
      pickup_pt = cup_dict[pickup_pt]
    target = current - 1
    # target = current - 1 while not in pickup_lst. If target = 0, loop back to max
    while target in pickup_lst or target == 0:
      if target == 0:
        target = max_cup
      else:
        target -= 1
    # the pickup cups go behind target. Manipulate linked list to shift pickup cups
    cup_dict[current] = cup_dict[pickup_lst[-1]] # first, current cup points to the cup after pickup cups (since pickups are removed) (1)
    cup_dict[pickup_lst[-1]] = cup_dict[target] # next, last cup in pickups points to cup that target was pointed to at first (2)
    cup_dict[target] = pickup_lst[0] # finally, target points to first cup in pickups. Now pickups is behind target (3)
    current = cup_dict[current] # current cup is now the cup that current was pointed to (shift 1 down for next cycle)
    #e.g [2] --> 3 --> 4 --> 5 --> 1 --> 2 (back to 2)
    #pickups are [3,4,5]
    # first, 2 --> 1 (point 2 to 1) (1)
    # pickups shifted to behind 1 (target)
    # next, 5 --> 2 (point 5 to 2 (last cup in pickups points to cup that target, 1, pointed to)) (2)
    # finally, 1 --> 3 (point target to first cup in pickup) (3)
    # new state: 2 --> 1 --> 3 --> 4 --> 5 --> 2
  return cup_dict

if __name__ == "__main__":
  main()
