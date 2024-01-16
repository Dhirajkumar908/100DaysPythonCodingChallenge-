print("🌟Contact Card🌟")
cantact = {}

cantact["name"] = input('Enter your name: ')
cantact["DOB"] = input('Enter you Date of birth: ')
cantact["phone"] = input('Enter your phone number: ')
cantact["email"] = input('Enter your emial: ')
cantact["address"] = input('Enter your address: ')

print()
print("🌟Contact Card🌟")

print(
  f"Hi {cantact['name']}. Our dictionary says that you were born on {cantact['DOB']}, We can call you on {cantact['phone']}, email {cantact['email']}, or write to {cantact['address']}"
)
