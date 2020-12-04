import re 

def in_range(number, a, b):
  return True if a <= int(number) <= b else False 

def validate_byr(value):
  return in_range(value, 1920, 2002) 

def validate_iyr(value):
  return in_range(value, 2010, 2020)

def validate_eyr(value):
  return in_range(value, 2020, 2030)

def validate_hgt(value):
  unit = value[-2:]
  if unit == "cm":
    return in_range(value[:-2], 150, 193)
  elif unit == "in":
    return in_range(value[:-2], 59, 76)
  else:
    return False

def match(schema, value):
  return True if re.match(schema, value) else False

def validate_hcl(value):
  return match(r"\#\b\w[0-9a-f]{5}\b", value)

def validate_ecl(value): 
  return match(r"\b(?:amb|blu|brn|gry|grn|hzl|oth)\b", value)

def validate_pid(value):
  return match(r"\b\d{9}\b", value)

def convert_to_dictionary(doc):
  dictionary = {}
  for field in doc:
    key, value = field.split(':') 
    dictionary[key] = value
  return dictionary

def read_input():
  with open("./input/day4.txt") as file:
    documents = file.read().split('\n\n')  
    for i in range(len(documents)):
      parsed_document = documents[i].replace('\n', ' ').split(' ')
      documents[i] = convert_to_dictionary(parsed_document)
    return documents

def validate_flieds_value(document, schema):
  for key in schema.keys():
    if not schema[key](document[key]):
      return False
  return True

if __name__ == "__main__":  
  print("Advent of Code - day 4")

  documents_to_scan = read_input()

  validation_schema = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr, 
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid
  }
  
  required_fields = set(validation_schema.keys()) 

  # part 1
  
  documents_with_required_fields = [document for document in documents_to_scan if required_fields.issubset(set(document.keys()))]
  print(len(documents_with_required_fields))
  
  # part 2

  validated = [document for document in documents_with_required_fields if validate_flieds_value(document, validation_schema)]
  print(len(validated))
