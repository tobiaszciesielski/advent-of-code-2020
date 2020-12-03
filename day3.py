'D:\Programy\python 3.9\python'

print("Advent of Code - day 3")

with open("./input/day3.txt", "r") as file: 
  area = file.read().splitlines()

area_size = len(area[0]), len(area)
x, y = 0, 0
tree = '#'
trees = 0

while y < area_size[1]: 
  encountered = area[y][x % area_size[0]]
  if encountered == tree: trees+=1
  x+=3
  y+=1 

print(trees)

# part 2 

def makeStep(x, y, step):
  x+=step[0]
  y+=step[1]
  return x, y 

trees_mul = 1
steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for i in range(len(steps)):
  x, y = 0, 0 # reset
  trees = 0
  while y < area_size[1]: 
    encountered = area[y][x % area_size[0]]
    if encountered == tree: trees+=1
    x, y = makeStep(x, y, steps[i])
  trees_mul*=trees

print(trees_mul)
