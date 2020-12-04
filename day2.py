'D:\Programy\python 3.9\python'

print("Advent of Code - day 2")

with open("./input/day2.txt", "r") as file:
  passwords = [line.split() for line in file.read().splitlines()]

# part 2

password_count = 0
for i in range(len(passwords)):
  line = passwords[i]
  a, b = line[0].split('-')
  letter = line[1][0]
  password = line[2]
  if (password[int(a)-1] == letter) ^ (password[int(b)-1] == letter):
    password_count+=1
    
print(password_count)

if __name__ == "__main__":

  password_count = 0
  for i in range(len(passwords)):
    line = passwords[i]
    a, b = line[0].split('-')
    letter = line[1][0]
    password = line[2]
    if int(a) <= password.count(letter) <= int(b):
      password_count += 1

  print(password_count)