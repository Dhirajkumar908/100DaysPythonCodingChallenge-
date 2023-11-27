from replit import audio

import os, time


def play():
  print("its called")
  source = audio.play_file('autio.wav')
  source.paused = False
  while True:
    stop_palyback = audio.play_file(
      "Press 2 anytime to stop playback and go back to the menu:")
    if stop_palyback == 2:
      source.paused = True
      return
    else:
      continue


while True:
  os.system("clear")
  print("MyPod music player")
  time.sleep(1)
  print("Press 1 to play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu apain")
  userinput = int(input(" "))
  if userinput == 1:
    print("Playing some proper tunes")

  elif userinput == 2:
    exit()

  else:
    continue
