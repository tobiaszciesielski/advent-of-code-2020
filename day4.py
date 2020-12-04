with open("./input/day4.txt") as file:
  documents = file.read().split('\n\n')

required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]) # "cid",)

valid_documents = 0
for i in range(len(documents)):
  parsed_document = documents[i].replace('\n', ' ').split(' ')
  document_fields = set([field.split(':')[0] for field in parsed_document])
  valid_documents += required_fields.issubset(document_fields)

print(valid_documents)
