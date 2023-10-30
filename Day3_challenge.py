#Day 3 Challenge
# Create these as a variable:
# A type of food
# A type of plant
# A method of cooking
# A word to describe burned food
# A household item

# 2. Output a nice looking Recipe page that *concatenates* a dish in this format:
# cooking food with burned plant on a bed of item

food= input("Name of food:")
plant=input("Name a type of plant:")
method=input("Name a method of cooking:")
burned=input("What word describes burned food:")
item=input("Name a DIY item:")
print()
print(method, food,"with",burned,plant, "on a bed of", item)