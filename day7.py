
def read_input():
  with open("./input/day7.txt") as file:
    return file.read().splitlines()

def get_bag_name(words):
  name = words.pop(0) + " " + words.pop(0)
  return name

  # light red       {'bright white': '1', 'muted yellow': '2'}
  # dark orange     {'bright white': '3', 'muted yellow': '4'}
  # bright white    {'shiny gold': '1'}
  # muted yellow    {'shiny gold': '2', 'faded blue': '9'}
  # shiny gold      {'dark olive': '1', 'vibrant plum': '2'}
  # dark olive      {'faded blue': '3', 'dotted black': '4'}
  # vibrant plum    {'faded blue': '5', 'dotted black': '6'}
  # faded blue      {}
  # dotted black    {}

def find_bags_containing_target(container, target_bag, parents=set()):
  for key, value in container.items():
    if target_bag in container[key].keys():
      parents.add(key)
      find_bags_containing_target(container, key, parents)
  return parents

if __name__ == "__main__":  
  print("Advent of Code - day _") # change day counter

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

  # code ...


