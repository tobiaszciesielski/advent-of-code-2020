
from copy import deepcopy

def read_input():
  with open("./input/day8.txt") as file: 
    program = []
    for line in file.read().splitlines():
      op, val = line.split()
      program.append([op, int(val), False])
    return program

def execute(program):
  current_line = 0
  global_value = 0
  terminates = True
  while current_line < len(program):
    op, val, was_executed = program[current_line]
    if was_executed: 
      terminates = False
      return global_value, terminates
    program[current_line][2] = True # was_executed to True
    if op == 'jmp':
      current_line+=val
      continue
    elif op == 'acc':
      global_value+=val
    current_line+=1
  return global_value, terminates 

if __name__ == "__main__":  
  print("Advent of Code - day8")

  program = read_input()

  # part 1
  
  print(execute(deepcopy(program))[0])
  
  # part 2


  for i in range(len(program)):
    boot_code = deepcopy(program) # 
    
    operation = boot_code[i][0]
    if operation != 'acc':
      boot_code[i][0] = 'nop' if operation == 'jmp' else 'jmp'
    else: continue

    value, terminate_flag = execute(boot_code)
    
    if terminate_flag:
      break

  print(value)
