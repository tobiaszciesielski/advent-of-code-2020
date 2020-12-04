
def read_input(): 
  with open("./input/day3.txt", "r") as file: 
    return file.read().splitlines()

def makeStep(x, y, step):
  x+=step[0]
  y+=step[1]
  return x, y 

def count_collisions(area, steps):
  TREE = '#'
  area_size = len(area[0]), len(area)
  collisions_multiplication = 1
  for step in steps:
    x, y = 0, 0 # starting position
    collisions = 0
    while y < area_size[1]: 
      encountered = area[y][x % area_size[0]]
      if encountered == TREE: 
        collisions+=1
      x, y = makeStep(x, y, step)
    collisions_multiplication*=collisions
  return collisions_multiplication

if __name__ == "__main__":   
  print("Advent of Code - day 3")

  area = read_input()

  # part 1

  print(count_collisions(area, [(3, 1)]))

  # part 2 

  steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  print(count_collisions(area, steps))
