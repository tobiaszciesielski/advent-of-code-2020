
def read_input():
  with open("./input/day8.txt") as file: 
    program = []
    for line in file.read().splitlines():
      op, val = line.split()
      program.append([op, int(val), False])
    return program


if __name__ == "__main__":  
  print("Advent of Code - day8")

  boot_code = read_input()

  # part 1
  
  current_line = 0
  global_value = 0
  while current_line < len(boot_code):
    op, val, was_executed = boot_code[current_line]
    if was_executed: break
    boot_code[current_line][2] = True # was_executed to True
    if op == 'jmp':
      current_line+=val
      continue
    elif op == 'acc':
      global_value+=val
    current_line+=1

  print(global_value)
  
  # part 2

  # code ...
