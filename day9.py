
def read_input():
  with open("./input/day9.txt") as file:
    return [int(num) for num in file.read().splitlines()]

if __name__ == "__main__":  
  print("Advent of Code - day 9")

  numbers = read_input()

  # part 1
  
  preamble = 25  
  invalid_number = 0
  
  for i in range(preamble, len(numbers)):
    numbers_array, number = numbers[i-preamble:i], numbers[i]
    if not len([n for n in numbers_array if number - n in numbers_array]):
      invalid_number = number
      break

  print(invalid_number)

  # part 2

  encryption_weakness = 0

  for i in range(len(numbers)):
    j = i+2 # at least two numbers
    sum_of_numbers = 0
    while sum_of_numbers < invalid_number:
      if j+1 >= len(numbers): break
      j+=1
      numbers_array = numbers[i:j]
      sum_of_numbers = sum(numbers_array)
      if sum_of_numbers == invalid_number:
        encryption_weakness = min(numbers_array)+max(numbers_array)
        break
    if encryption_weakness:
      break

  print(encryption_weakness)
