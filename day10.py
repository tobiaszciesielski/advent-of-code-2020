from collections import defaultdict

def read_input():
  with open("./input/day10.txt") as file:
    return sorted(int(num) for num in file.readlines())

if __name__ == "__main__":  
  print("Advent of Code - day 10")

  adapters = read_input()
  max_joltage = (adapters[-1]+3)
  adapters.append(max_joltage)
  adapters.insert(0, 0)
  
  # part 1

  three = 0
  one = 0
  for i in range(len(adapters)):
    current, next_three = adapters[i], adapters[i+1:i+4]
    if current+1 in next_three:
      one+=1
    elif current+3 in next_three:
      three +=1
    
  print(one * three)    

  # part 2

  paths = defaultdict(int)
  paths[0] = 1

  for adapter in sorted(adapters):
      for diff in range(1, 4):
          next_adapter = adapter + diff
          if next_adapter in adapters:
              paths[next_adapter] += paths[adapter]
 
  print(paths[max_joltage])
