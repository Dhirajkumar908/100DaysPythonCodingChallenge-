namelist = []


def peoples_names():
  print()
  for index in range(len(namelist)):
    print(f"{index+1}: {namelist[index]}")
  print()


while True:
  print()
  first_name = input("Enter your first name:").strip().capitalize()
  last_name = input("Enter your last name:").strip().capitalize()
  full_name = f"{first_name} {last_name}"
  if full_name not in namelist:
    namelist.append(full_name)
  else:
    print("ERROR: Duplicate name")
  print()
  peoples_names()
