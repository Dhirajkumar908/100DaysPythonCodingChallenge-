import os

usertype = os.environ['usertype']
passord = os.environ['password']

user = input("Username: ")
password = input("Password: ")

if user == usertype and password == passord:
  print('Hello Admin')
else:
  print('hello normie')