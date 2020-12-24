import re
from functools import reduce

def main():
  with open('tickets.txt', 'r') as File:
    tickets = ''.join(i for i in File).strip().split('\n\n') # creates a list of 3, lst[0] == fields, lst[1] == myticket, lst[2] == nearby ticks
  my_vals = tickets[1].split('\n')[1].split(',')
  field_names = re.findall(r'.+(?=:)', tickets[0])
  field_vals = [re.findall(r'(\d+)-(\d+)', val) for val in tickets[0].split('\n')]
  field_vals = [[(int(val[0]), int(val[1])) for val in field_vals[i]] for i in range(len(field_vals))] # get list of list of fields in each nearby ticket
  fvals_sorted = sorted(sum(field_vals, []), key=lambda tup: tup[0]) # sort by range floor (asc.)
  total_range = find_total_range(fvals_sorted) # see below
  nearby = [list(map(int, ticket.split(','))) for ticket in tickets[2].split('\n')[1:]]
  valid_nearby = nearby.copy()
  sum_1 = 0
  for ticket in nearby: # see if values are valid in any range
    valid = True
    for field in ticket:
      inside = False
      for range_n in total_range:
        if field >= range_n[0] and field <= range_n[1]:
          inside = True
          break
      if not inside:
        valid = False
        sum_1 += field
    if not valid:
      valid_nearby.remove(ticket)
  print(f"Part 1: {sum_1}")

  nearby_fields = [[ticket[i] for ticket in valid_nearby] for i in range(len(valid_nearby[0]))] # re group nearby tickets by fields
  possible_fields = [(i, lst_possible_fields(nearby_field, field_vals)) for i, nearby_field in enumerate(nearby_fields)] # get list of which field is satisfied for each column. Index is remembered before sorting in next step
  possible_fields = sorted(possible_fields, key=lambda tup: tup[1].count(True))
  # go through fields by increasing number of fields that the tickets are valid for. Tickets that are only valid for 1 are confirmed, narrowing the right field for tickets later.
  taken = []
  field_index_dict = {}
  for x in possible_fields:
    for item in taken: # if field already filled, set to False as it cannot be the right field
      x[1][item] = False
    field_index = x[1].index(True)
    taken.append(field_index)
    field_index_dict[field_names[field_index]] = x[0] # match field name with column index
  departure_index = [value for key, value in field_index_dict.items() if 'departure' in key] # column index for fields that contain "departure"
  prod = 1
  for x in departure_index:
    prod *= int(my_vals[x])
  print(f"Part 2: {prod}")

def find_total_range(tups_lst): # merge overlapping ranges and get lists of ranges not overlapping
  lst = [tups_lst[0]]
  for i in range(len(tups_lst)):
    if lst[-1][1] < tups_lst[i][0]: # range ceiling < range floor of next range (ie not overlapping)
      lst.append(tups_lst[i])
    elif lst[-1][1] < tups_lst[i][1]: # merge if next range ceiling is higher, else next range is a subset and ignore it
      lst[-1] = (lst[-1][0], tups_lst[i][1])
  return lst

def lst_possible_fields(nearby_field, field_vals):
  return [is_in_field_range(nearby_field, field_ranges) for field_ranges in field_vals]

def is_in_field_range(nearby_field, field_ranges): #
  for val in nearby_field:
    inrange = False
    for f_range in field_ranges:
      if val >= f_range[0] and val <= f_range[1]:
        inrange = True
        break
    if not inrange:
      return False
  return True


if __name__ == "__main__":
  main()
