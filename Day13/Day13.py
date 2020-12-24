def main():
  with open('schedules.txt', 'r') as File:
    schedules = [schedule.strip() for schedule in File]
  departure = int(schedules[0]) # depature time is first row
  buses = schedules[1].split(',') # make list of buses
  buses_no_x = [int(bus) for bus in buses if bus != 'x'] # remove those not in service
  print(f"Part 1: {part1(departure, buses_no_x)}")
  print(f"Part 2: {part2(buses, buses_no_x)}")

def part1(departure_time, bus_lst):
  depart_buses = [] # earliest departure time for each bus
  for bus in bus_lst:
    new_bus = 0
    while new_bus < departure_time:
      new_bus += bus
    depart_buses.append(new_bus)
  fastest = min(depart_buses) # all values > departure_time, so to find fastest, just find smallest
  return bus_lst[depart_buses.index(fastest)] * (fastest - departure_time)

def part2(bus_str_lst, bus_lst):
  n = [int(-i) for i in range(len(bus_str_lst)) if bus_str_lst[i] != "x"] # create an array of -indexes to find chinese remainder
  # ap formula: u + (n - 1)d. So, u % bus_id = -i (aka -(n-1)d) because u * k = v * bus_id - (n - 1)d, where k and v are any positive integers
  return chinese_remainder(bus_lst, n)

# CRT: find x with list of x % n = a
from functools import reduce #CREDIT (TAKEN DIRECTLY): https://rosettacode.org/wiki/Chinese_remainder_theorem
def chinese_remainder(n, a): # need to use chinese remainder theorum, because testing k for u * k takes forever (help taken from r/adventofcode)
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

if __name__ == "__main__":
    main()
