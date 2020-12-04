
def get_two_numbers():
  for i in range(len(numbers)): 
    for j in range(len(numbers)):
      if numbers[i] + numbers[j] == 2020:
        return numbers[i], numbers[j]

def get_three_numbers():
  for i in range(len(numbers)): 
    for j in range(len(numbers)):
      for k in range(len(numbers)):
        if numbers[i] + numbers[j] + numbers[k] == 2020:
          return numbers[i], numbers[j], numbers[k]

if __name__ == "__main__":
  print("Advent of Code - day 1")

  with open("./input/day1.txt", mode="r") as file: 
    numbers = [int(line) for line in file.read().splitlines()]

  # part 1

  x, y = get_two_numbers()
  print(x*y)

  # part 2

  a, b, c = get_three_numbers()
  print(a*b*c)
      