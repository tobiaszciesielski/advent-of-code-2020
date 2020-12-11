
def read_input():
  with open("./input/day10.txt") as file:
    return [int(num) for num in file.read().splitlines()]

if __name__ == "__main__":  
  print("Advent of Code - day 10")

  adapters = read_input()
  adapters.sort()
  adapters.append((adapters[-1]+3))
  adapters.insert(0, 0)
  
  # part 1

  three = 0
  one = 0
  for i in range(len(adapters)):
    adapters[i]+1
    next_three = adapters[i+1:i+4]
    if adapters[i]+1 in next_three:
      one+=1
    elif adapters[i]+3 in next_three:
      three +=1
  
  print(one * three)    

  # part 2

  # code ...
