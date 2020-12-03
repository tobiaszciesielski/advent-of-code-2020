'D:\Programy\python 3.9\python'

print("Advent of Code - day 2")

with open("./input/day2.txt", "r") as file:
  passwords = [line.split() for line in file.read().splitlines()]

passwordCount = 0
for i in range(len(passwords)):
  line = passwords[i]
  a, b = line[0].split('-')
  letter = line[1][0]
  password = line[2]
  if int(a) <= password.count(letter) <= int(b):
    passwordCount += 1

print(passwordCount)

# part 2

passwordCount = 0
for i in range(len(passwords)):
  line = passwords[i]
  a, b = line[0].split('-')
  letter = line[1][0]
  password = line[2]
  if (password[int(a)-1] == letter) ^ (password[int(b)-1] == letter):
    passwordCount+=1
    
print(passwordCount)