"""
This is the challenge you're looking for. This program will generate your Star Wars Name.

Ask the user to input their first & last names.
Slice the first 3 letters of the first name.
Slice the first 3 letters of the last name (surname).
Join them together. Ideally change the case so that it looks good - think fStrings or .upper()/.lower(). This is the user's Star Wars first name.
Now ask the user for their mother's maiden name and the city where they were born. (Maiden name is the last name they had before they got married. If you are not sure, make up a last name.)
Combine the first two letters of the maiden name with the last 3 letters of the city to make the user's Star Wars last name. Remember, fStrings and .upper()/.lower().
Finally, print them both as part of a sentence.
🥳 Extra points for getting all the inputs with just one input command and the split function.

"""

print("🌟Star Wars Name Generator🌟")

all = input(
  "Enter you first name, last name, Mum's maiden name and the city you were born in:"
).split()
print()

first_name = all[0].strip()
last_name = all[1].strip()
maiden_name = all[2].strip()
city = all[3].strip()

name = f"{first_name[:3]}{last_name[:3]} {maiden_name[:2]}{city[:3]}"
print(f"Your Star Wars name is {name}")
print()