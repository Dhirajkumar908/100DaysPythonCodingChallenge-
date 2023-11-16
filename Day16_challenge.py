"""Day 16 Challenge
Create a "Name the Lyrics" game. Write your favorite song lyrics with a word or two missing. The user has to figure out the correct song lyric in as few attempts as possible. Find the true lyric master among you!"""


while True:
    print('Never going to ______ you up.')
    print('Fill in the blank lyrics!')
    print('(Type in the blank lyrics and see if you are as cool as me.)\n')
    word = input('Type in the blank lyrics:')
    if word == "give":
        print('Well done! You got the lyrics right!\n')
        break
    else:
        print("")
        print('Nope, try again')
        print("")
