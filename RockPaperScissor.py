#Rock Paper Scissor Game--
import random

game_Icon='''
  .--------.--------------------------------------------------.
  |    `  __)__________________________________________       |
  |  )   |.-------------------------------------------.|      |
  |,`._,-||                     o                     ||      |
  |      ||  ___  __ _    __       _   __  ____ __  _ ||      |
  |      || (( `| || |\  /||     ,'-`| || |'||`| \\ / ||,'`.  |
  |      ||  .`.  || |\\/ ||    ((     ||   ||    ||  ||    `'|
  |      || |._)) || | `  ||     `._,| ||   ||    ||  ||`--'`-|
  |,.    ||  __________________   __________________  ||      |
  | \`._,|| |         Rock||paper||scissor
  |.__`\_|| '------------------' '------------------' ||,-' ,'|
  |::::::||             __________________            || ,'  ;|
  |::::::||            |  Game Started
  |:::::_||            '------------------'           ||::::::|
  |:,-'' ||_____________________o_____________________||::::::|
  |     ,`-------,----------.-------.------------------'::::::|
  |  ,         ,':::::::::::|       |::::::::::::::::::::::SSt|
  '-'---------'-------------'-------'-------------------------'

  
  '''
print(game_Icon)
userChoice=input("enter your choice : ")
computerChoice=random.choice(["Rock","paper","Scissor"])

if userChoice==computerChoice:
    print("ComputerChoice = ",computerChoice)
    print("match tie")
elif userChoice == "rock" :
    if computerChoice == "scissor":
        print("computer won")
    else:
        print("Paper covers Rock = You Won")
elif userChoice == "paper" :
    if computerChoice == "rock":
        print("Paper covers Rock = computer won")
    else:
        print("Scissors cuts Paper = You Won")
elif userChoice == "scissor" :
    if computerChoice == "paper":
        print("Scissors cuts Paper = computer won")
    else:
        print("Rock crushes Scissors = You Won")