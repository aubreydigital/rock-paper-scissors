import random
best_of_ten = 0
myScore = 0
compScore = 0
print()
print('Rock, Paper, Scissors: Best of Ten')
print('-' * 20)
while best_of_ten < 10:
    print()
    print('Round:', best_of_ten + 1)
    print('Current Score | User:', myScore, 'Computer:', compScore)
    print()
    choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n\n'))
    compChoice = random.randint(0,2)
    print('Computer chose:', compChoice)
    print()

    if compChoice == 0 and choice == 2:
        print('Computer wins!')
        compScore += 1
    elif compChoice == 0 and choice == 0:
        print("It's a draw")
    elif compChoice == 0 and choice == 1:
        print('Paper covers rock! You win!')
        myScore += 1
    elif compChoice == 1 and choice == 0:
        print('Computer wins!')
        compScore += 1
    elif compChoice == 1 and choice == 1:
        print("It's a draw")
    elif compChoice == 1 and choice == 2:
        print('Scissors cut paper! You win!')
    elif compChoice == 2 and choice == 0:
        print('Rock beats scissors! You win!')
        myScore += 1
    elif compChoice == 2 and choice == 1:
        print('Computer wins!')
        compScore += 1
    elif compChoice == 2 and choice == 2:
        print("It's a draw!")
    else:
        print('Invalid entry')
    if choice == 0 or choice == 1 or choice == 2:
        best_of_ten += 1
if myScore > compScore:
    print('You are the winner!')
elif compScore > myScore:
    print('The computer wins!')
else:
    print("It's a tie!")