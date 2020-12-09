
def read_input():
  with open("./input/day9.txt") as file:
    return [int(num) for num in file.read().splitlines()]

if __name__ == "__main__":  
  print("Advent of Code - day 9")

  numbers = read_input()

  # part 1
  
  preamble = 25  
  
  for i in range(preamble, len(numbers)):
    array, number = numbers[i-preamble:i], numbers[i]
    if not len([n for n in array if number - n in array]):
      print(number) 
      break

  # part 2

  # code ...
