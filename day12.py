
def read_input():
  with open("./input/day12.txt") as file: # change input file
    return [(line[0], int(line[1:])) for line in file.read().splitlines()]

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the

if __name__ == "__main__":  
  print("Advent of Code - day 12") # change day counter

  actions = read_input()

  # part 1
  
  directions = ['W', 'N', 'E', 'S']
  current_directon = 2 # East
  
  position = {d:0 for d in directions}

  for action in actions:
    direction, value = action
    
    if direction in directions:
      position[direction] += value

    elif direction == 'F':
      position[directions[current_directon]] += value
    
    elif direction == 'R':
      current_directon += int(value/90)
      current_directon %= len(directions)
    
    elif direction == 'L':
      current_directon -= int(value/90)
      current_directon %= len(directions)

  print(abs(position['E'] - position['W']) + abs(position['S'] - position['N']))
  
  # part 2

  directions = ['W', 'N', 'E', 'S']
  current_directon = 2 # East
  
  position = {d:0 for d in directions}
  waypoint = 

  for action in actions:
    direction, value = action


  print(abs(position['E'] - position['W']) + abs(position['S'] - position['N']))
  
