import random
points = 100
continuare = True
#the number you have to guess (default range is from 1 to 100)
number = random.randint(1, 100)
#gender is just for fun, if you dont answear 
gender = input("What is your gender?\n")
#here is the actual game where you try to guess the number.
def game():
    global points
    global continuare
    while True:
        #-----Lose-----
        if points <= 0:
            lose = input("You ran out of points.\nYOU LOSE!\nDo you want to continue?\nY/N\n")
            if lose == "y" or lose == "Y":
                points = 100
                break
            else:
                continuare = False
                break
        #-----Guess the number----
        guess = int(input("Guess the number: "))
        if guess < number:
            print("Wrong!\nHint: bigger.")
            points = points - 10
            continue
        elif guess > number:
            print("Wrong!\nHint: smaller.")
            points = points - 10
            continue
        #-----Win-----
        else:
            win= input("Congratulations! YOW WON THE GAME!\nDo you want to continue?\nY/N\n")
            if win == "y" or win == "Y":
                break
            else:
                continuare = False
                break

while continuare:
    #Ask if you want 
    QuestionHint = input("Do you need a hint now?It will cost you 10 points.\nY/N\n")
    #give hints about the number if you want.
    if QuestionHint == "y" or QuestionHint == "Y":
        if number < 40 and number > 0:
            print("Hint: The number is low")
            points -= 10
            game()

        elif number >= 40 and number <= 60:
            print("Hint: The number is somewhere in mid")
            points -= 10
            game()

        elif number > 60 and number <= 100:
            print("Hint: The number is high")
            points -= 10
            game()

        else:
            print("I think you changes some values. check the lines who starts with #\nI will take the points anyway")
            points -= 10
            break
    elif QuestionHint == "n" or QuestionHint == "N":
        game()
        break
    #If you dont answear the question
    else:
        print(f"You had only two options {gender}, TWO!!!")
        break