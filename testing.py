empolyee={
    'name':'dhiraj',
    'age':'26',
    'city':'noida',
    'hobbies':['movies','youtube']
}

# get method get()
age=empolyee.get("age")
print(age)

# The keys() Method:

keys=empolyee.keys()
print(keys)

# The values() Method:
values=empolyee.values()
print(values)

# The items() Method:
items=empolyee.items()
print(items)
print()

# The update() Method:
country = {
    "name": "Bangladesh",
    "capital": "Dhaka",
    "population": 160000000,
    "is_developed": False,
}
country_extra_info = {"continent": "Asia", "is_island": False, "currency": "BDT"}
print(country)
country.update(country_extra_info)
print(country)

is_developed=country.pop("is_developed")
print(is_developed)

is_developed=country.pop("is_developed", None)

print(country)
print()
print(is_developed)

# The copy() Method:
print("===============================")
shallow_copy=country.copy()
shallow_copy["name"]="india"
print(country)
print(shallow_copy)
print("===============================")

import copy
countries = {
    "name": "Bangladesh",
    "capital": {
        "name": "Dhaka",
        "area": 306.38,
        "population": 8906039
        },
    "population": 160000000,
    "is_developed": False, 
}

deep_copy=copy.deepcopy(countries)
deep_copy["capital"]["name"]="Dhaka city"
print(f"origanal:{countries}")
print(f"shallow copy: {deep_copy}")
deep_copy.clear()
print(f"shallow copy: {deep_copy}")
is_developed, is_developed_status=countries.popitem()

print(is_developed)
print(is_developed_status)