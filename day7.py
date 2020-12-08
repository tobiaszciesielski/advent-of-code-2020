
def read_input():
  with open("./input/day7.txt") as file:
    return file.read().splitlines()

def get_bag_name(words):
  name = words.pop(0) + " " + words.pop(0)
  return name

def count_all_bags_inside_target(bags, target_bag):
  count = 1
  for key, number in bags[target_bag].items():
    count += int(number) * count_all_bags_inside_target(bags, key)
  return count

def find_bags_containing_target(bags, target_bag, parents=set()):
  for key, value in bags.items():
    if target_bag in bags[key].keys():
      parents.add(key)
      find_bags_containing_target(bags, key, parents)
  return parents

if __name__ == "__main__":  
  print("Advent of Code - day 7") # change day counter

  luggages = read_input()

  target_bag = "shiny gold"
  luggage_relations = {}
  for luggage in luggages:
    unwanted = ["contain", "bag", "bag.", "no", "other", "bags", "bags.", "bags,", "bag,"]
    words = [word for word in luggage.split(' ') if word not in unwanted]
    main_container = get_bag_name(words)

    luggage_relations[main_container] = {}
    while len(words) > 0:
      count = words.pop(0)
      container = get_bag_name(words)
      luggage_relations[main_container][container] = count

  # part 1

  print(len(find_bags_containing_target(luggage_relations, target_bag)))

  # part 2

  print(count_all_bags_inside_target(luggage_relations, target_bag)-1)
