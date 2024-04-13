import time
import random
import drugtable


def timeloop():
  while True:
    for x in range(0, len(drugtable.savetable)):
      number = random.randint(-20, 20)
      if drugtable.savetable[x][1] + number > 0:
        drugtable.savetable[x][1] += number
    time.sleep(60)
    


