import re
bag_containedby_dict = {} # each key contains a list of bags that can contain the key
bag_container_dict = {}
rules = []
containers = []
contents = []

def main():
  with open('rules.txt', 'r') as file:
    for row in file:
      rule = row.strip("\n")
      rules.append(rule)
  for rule in rules:
    bag_container = re.findall(r".+(?= bags contain)", rule)[0] # bag container found before " contain"
    bags_lst = re.findall(r"(?<=contain \d )[^,.]+(?= bag)|(?<=, \d )[^,.]+(?= bag)", rule)
    # bag type found between "contain n" and "bag"
    count_lst = re.findall(r"(?<=contain )[\d]|(?<=, )[\d]", rule)

    # Part 1: dictionary stored in format bag_x: [bags_that_store_bag_x]
    for bag in bags_lst:
      if bag in bag_containedby_dict:
        bag_containedby_dict[bag].append(bag_container)
      else:
        bag_containedby_dict[bag] = [bag_container]

    # Part 2: nested dictionary stored in format bag_container_x : {bag_a : num_of_bag_a, bag_b : num_of_bag_b, ...}
    if bags_lst:
      bag_container_dict[bag_container] = {}
    for bag in range(len(bags_lst)):
        bag_container_dict[bag_container][bags_lst[bag]] = int(count_lst[bag])
  lst_bag_containers("shiny gold", bag_containedby_dict)
  print(f"Part 1: {len(containers)}")
  print(f"Part 2: {sum_content_calc('shiny gold', contents, bag_container_dict)}")


def lst_bag_containers(bag, containedby_dict): # fill list with all containers of bag
  if bag in containedby_dict:
    for bag_container in containedby_dict[bag]:
      if bag_container not in containers:
        containers.append(bag_container)
      lst_bag_containers(bag_container, containedby_dict) # fill list wiht outer containeres of bag

# Part 2: first, produce tuple of (container, content_x, count_x) and use tuple to match and multiply container count with content count
def lst_bag_content(bag, container_dict):
  if bag in bag_container_dict:
    for bag_container in container_dict[bag]:
      contents.append((bag, bag_container, container_dict[bag][bag_container]))
      lst_bag_content(bag_container, container_dict)


def sum_content_calc(bag, bag_content_lst, container_dict): # sum all bag products for each bag in tuple
  lst_bag_content(bag, container_dict)
  sum = 0
  for i in range(len(bag_content_lst)):
    var = content_count_calc(bag, bag_content_lst, i, bag_content_lst[i][1]) # set initial target as current bag so that it is the first elif case below
    sum += var
  return sum


def content_count_calc(bag, bag_content_lst, iter_i, curr_bag_target): # multiply containers with bag until container is "shiny gold"
  if bag_content_lst[iter_i][0] == bag: # if bag in question is "shiny gold", return count (base case)
    return bag_content_lst[iter_i][2]
  elif curr_bag_target == bag_content_lst[iter_i][1]: # if current bag is container of target_bag,
    # multiply bag count with container count and container's container count until "shiny gold"
    return bag_content_lst[iter_i][2] * content_count_calc(bag, bag_content_lst, iter_i - 1, bag_content_lst[iter_i][0])
    # set container (tuple[0]) of current bag as target to find container's container
  else:
      return content_count_calc(bag, bag_content_lst, iter_i - 1, curr_bag_target) # if target is not current bag, keep iterating

if __name__ == "__main__":
    main()
