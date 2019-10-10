from random import randint
from colored import fg, attr

red = fg('red')
green = fg('green')
yellow = fg('yellow')
reset = attr('reset')

attempt = 1
score = 0
scores = []

while attempt <= 5:
  randomnum = randint(1, 6)
  usernum = int(input("Guess the number between 1 and 6: "))
  difference = abs(usernum - randomnum)
  attempt += 1

  print("The difference between your and computer's number is", green, difference, reset, "\n")
  print("Computer's num is", yellow, randomnum, reset, "\n")

  if difference == 0:
    score = 6
    scores.append(score)
  elif difference == 1:
    score = 5
    scores.append(score)
  elif difference == 2:
    score = 4
    scores.append(score)
  elif difference == 3:
    score = 3
    scores.append(score)
  elif difference == 4:
    score = 2
    scores.append(score)
  elif difference == 5:
    score = 1
    scores.append(score)
  else:
    score = 0

  totalscore = sum(scores)

  print("You got", yellow, score, reset, "points\n")
print("Your total score is", yellow, totalscore, reset, "\n")

if totalscore < 25:
  print(red + "YOU LOSE!" + reset, "\n")
  print(red + "You haven't got enought points. Try again!" + reset)
else:
  print(green + "YOU WIN!" + reset)
  