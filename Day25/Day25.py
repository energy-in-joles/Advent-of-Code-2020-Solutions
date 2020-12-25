# Diffie-Hellman Problem!
# Initially solved using online calculator. Loop_1 found with: https://www.alpertron.com.ar/DILOG.HTM
# Then loop_1 used with pub_key_2 to find final_key with: https://planetcalc.com/8326/

# But decided to write a code for today:
# Inspired by u/AidGli on r/adventofcode (https://github.com/AidanGlickman/Advent-2020/blob/master/day25/solution.py)
# because I did not know how to deal with large exponents :(

def main():
  with open('pub_keys.txt', 'r') as File:
    pub_keys = [row.strip() for row in File]
  pub_key_1 = int(pub_keys[0])
  pub_key_2 = int(pub_keys[1])
  loop_1 = find_loop(7,pub_key_1,20201227) # only find loop 1 because both produce same result
  final_key = find_key(pub_key_2, loop_1, 20201227) # (mod 20201227) is provided by the problem
  print(f"Part 1: {final_key}")
  print("Part 2: MERRY CHRISTMAS!!")

def find_loop(base,pub_key, mod_num):
  key_try = base
  loop = 1
  while key_try != pub_key: # find the exponent b, where base ** b % mod_num == pub_key
    key_try *= base
    key_try %= mod_num # keep getting mod value (key_try) * 7 until key_try == pub_key
    #(modding at each cycle allows working with smaller number than modding at end)
    loop += 1 # keep updating loop until key_try == pub_key
  return loop # when it equals, get the loop value, ie exponent

def find_key(base,power,mod_num):
  key = base
  for i in range(power - 1): # similar as find_loop, multiply base to itself and mod loop times. ie base ** key % mod_num
    key *= base
    key %= mod_num # mod every cycle to work with smaller vals compared to mod at end
  return key

if __name__ == "__main__":
  main()
