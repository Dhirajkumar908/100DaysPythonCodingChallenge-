import random, os, time

listOfWords = [
  "british", "suave", "integrity", "accent", "evil", "genius", "Downton"
]

wordChosen = []
lives = 6

word = random.choice(listOfWords)

print(word)

while True:
  time.sleep(1)
  os.system("clear")
  letter = input("Choose a letter:").lower()

  if letter in wordChosen:
    print("you have tried that before")
    continue
  wordChosen.append(letter)
  if letter in word:
    print("You have found a letter")
  else:
    print("Nope, not in there")
    lives -= 1

  allLetters = True
  print()
