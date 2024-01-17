website = {"name": None, "URL": None, "description": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

for name, value in website.items():
  print(f"{name}:{value}")
