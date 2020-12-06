
def read_input():
  with open("./input/day6.txt") as file:
    return [group_questions.splitlines() for group_questions in file.read().split('\n\n')]

def collect_group_questions(group_questions):
  return [set(''.join(string for string in answers)) for answers in group_questions]
    
def create_char_dictionary(characters):
    char_dictionary = dict()
    for character in characters:
      char_dictionary[character] = 0
    return char_dictionary

if __name__ == "__main__":  
  print("Advent of Code - day _") # change day counter

  group_questions = read_input()

  # part 1

  questions = collect_group_questions(group_questions)
  print(sum([len(question) for question in questions]))

  # part 2

  counter = 0
  for i in range(len(group_questions)):
    char_dict = create_char_dictionary(questions[i])
    current_questions = group_questions[i]
    for person_questions in current_questions:
      for question in person_questions:
        char_dict[question]+=1
    for question in char_dict.keys():
     if len(current_questions) == char_dict[question]:
       counter+=1

  print(counter)
