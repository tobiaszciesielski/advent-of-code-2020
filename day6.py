
def read_input():
  with open("./input/day6.txt") as file:
    groups = file.read().split('\n\n')
    for i in range(len(groups)):
      groups[i] = groups[i].replace('\n', '')  
    return groups


if __name__ == "__main__":  
  print("Advent of Code - day _") # change day counter

  groups = read_input()

  # part 1
  
  print(sum([len(set(group)) for group in groups]))

  # part 2

  # code ...
