
from copy import deepcopy

def read_input():
  with open("./input/day11.txt") as file: # change input file
    return [list(line) for line in file.read().splitlines()]

DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def get_frame(pos, limits, area):
  x, y = pos
  x_lim, y_lim = limits
  frame = []
  for dir in DIRS:
    if x+dir[0] < 0 or x+dir[0] > x_lim: continue
    if y+dir[1] < 0 or y+dir[1] > y_lim: continue
    frame.append(area[y+dir[1]][x+dir[0]])
  return frame

if __name__ == "__main__":  
  print("Advent of Code - day 11") # change day counter

  original_layout = read_input()

  rows = len(original_layout)
  cols = len(original_layout[0])
  index_limits = (rows-1, cols-1)

  previous = deepcopy(original_layout)
  same = False
  while not same:
    layout = deepcopy(previous)
    for row in range(rows):
      for col in range(cols):
        position = previous[row][col]
        frame = get_frame((col, row), index_limits, previous)
        if position == 'L' and '#' not in frame:
          layout[row][col] = '#'
        elif position == '#' and frame.count('#') > 3:
          layout[row][col] = 'L'

    same = True
    for row in range(rows):
      for col in range(cols):
        if previous[row][col] != layout[row][col]:
          same = False 
          break
      if not same:
        break
  
    previous = deepcopy(layout)
    if same:  
      break

  occupated = 0
  for row in range(rows):
      for col in range(cols):
        if previous[row][col] == '#':
          occupated+=1
  print(occupated)
  
  # part 2
