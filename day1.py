
if __name__ == "__main__":
  print("Advent of Code - day 1")

  with open("./input/day1.txt", mode="r") as file: 
      numbers = [int(line) for line in file.read().splitlines()]

  # part 1

  for i in range(len(numbers)): 
    for j in range(len(numbers)):
      if i != j:
        if numbers[i] + numbers[j] == 2020:
          print(numbers[i] * numbers[j])

  # part 2

  for i in range(len(numbers)): 
    for j in range(len(numbers)):
      if i != j:
        for k in range(len(numbers)):
          if j != k and i != k:
            if numbers[i] + numbers[j] + numbers[k] == 2020:
              print(numbers[i] * numbers[j] * numbers[k])
      