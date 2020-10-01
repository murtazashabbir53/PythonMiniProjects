#GUESS THE NUMBER#
print("\t\t\t\t*****Welcome To The Game*****\n ")
print("Description: You will be given an access to enter any random number first.\n You need to guess the number imagined by the examiner")
print("Rules for the game are as followed:\n")

print("rule.1:- No. of guesses allowed are 9 ")
print("rule.2:- Prize will be given with respect to your number of guesses")

#number_of_guesses_alloted = 9

nog = 0
while nog < 9:
    print("Enter number:\n")
    num = int(input())
    if 18 == num:
        print(f"Congratulations! You guessed the number in {nog} guesses")
        break
    else:

        if num > 18:
            print("Just subtract your number and come down")
            nog = nog + 1
            print(f"You used {nog} guesses ")
            continue



        elif num < 18:
            print("Come Up brother!")
            nog = nog + 1
            print(f"You used {nog} guesses")
            continue
else:
    print("##################GAME OVER#################")
    exit()
