#1st making challenge theme is: make a game but in less than 30 lines (i will make a guessing game it ez)
from random import randint

your_number = 0
answer = 0
time_guess = 0

print("wellcome to guessing game, the game to think about number or something")
print("how to play write a number have 1 to 5 digits and computer will higher! or lower!")

while True:
    answer = randint(0,99999)
    time_guess = 0
    your_number = int(input("write number you guessing "))
    time_guess += 1
    if your_number > answer:
        print("lower")
    elif your_number < answer:
        print("higher!")
    else:
        print("you won!!!")
        print("you guess: " + str(time_guess) + " times")
        if input("do you want play again(y/n) ") ==  "y":
            answer = randint(0,99999)
            time_guess = 0
        else:
            break
print("goodbye have a good day")
