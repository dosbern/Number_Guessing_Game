import random
winner = random.randint(1, 20)
#print(winner)
print ('Choose a number between 1 and 20')
print (' ')
for guessesTaken in range(1, 7):
    guess = int(input())
    if guess == winner:
        print ('YES, congratulations!')
        print (' ')
        break
    elif guess > winner:
        print ('You guessed too high...')
        print ('Please try again')
        print ('You have '+ str(6-guessesTaken) + ' tries remaining')
        print (' ')
    elif guess < winner:
        print ('You guessed too low...')
        print ('Please try again')
        print ('You have '+ str(6-guessesTaken) + ' tries remaining')
        print (' ')
    else:
        print ('No, please try again...')
        print ('You have '+ str(6-guessesTaken) + ' tries remaining')
        print (' ')
print ('You win!')
print ('You guessed the correct number in '+ str(guessesTaken) +' tries')