
from math import floor, ceil

def read_input():
  with open("./input/day5.txt") as file:
    return file.read().splitlines()

def count_position(seat_code, upper_value):
  code = seat_code 
  a, b = 0, upper_value-1
  threshold = upper_value
  code_lenght = len(seat_code)
  for i in range(code_lenght):
    half = code[i]
    if half == 'F' or half == 'L': # lower half
      if i == code_lenght-1: return a 
      threshold = floor(threshold/2)
      b -= threshold
    elif half == 'B' or half == 'R': # upper half
      if i == code_lenght-1: return b 
      threshold = ceil(threshold/2)
      a += threshold

def count_position_id(seat_code):
  total_rows, total_cols = 128, 8
  row_code, col_code = seat_code[:7], seat_code[7:]
  return count_position(row_code, total_rows) * total_cols + count_position(col_code, total_cols)

if __name__ == "__main__":  
  print("Advent of Code - day 5")

  seat_codes = read_input()

  # part 1

  seat_ids = [count_position_id(seat_code) for seat_code in seat_codes]
  print(max(seat_ids))

  # part 2

  seat_ids.sort()
  for i in range(len(seat_ids)-1):
    if seat_ids[i+1] - seat_ids[i] > 1:
      print(seat_ids[i]+1)

