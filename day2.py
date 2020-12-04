
def parse_password_template(pwd):
  a, b = pwd[0].split('-')
  letter = pwd[1][0]
  password = pwd[2]
  return (a, b, letter, password)

if __name__ == "__main__":
  print("Advent of Code - day 2")

  with open("./input/day2.txt", "r") as file:
    passwords = [line.split() for line in file.read().splitlines()]

  part_one_valid_passwords = 0
  part_two_valid_password = 0
  for password_template in passwords:
    a, b, letter, password = parse_password_template(password_template)
    
    # part 1 
    if int(a) <= password.count(letter) <= int(b):
      part_one_valid_passwords += 1
    
    # part 2
    if (password[int(a)-1] == letter) ^ (password[int(b)-1] == letter):
      part_two_valid_password +=1

  print(part_one_valid_passwords)
  print(part_two_valid_password)
