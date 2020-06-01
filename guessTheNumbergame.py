# This is guess the number game.
import random
secretnumber = random.randint(1,10)
print('I am thinking of a number between 1 and 10.')

# Ask the player guess 3 times.
for guessestaken in range(1,4):
    print('take a guess.')
    guess = int(input())

    if guess < secretnumber:
        print('your guess is too low.')
    elif guess > secretnumber:
        print('your guess is too high.')
    else:
        break  #this condition is the correct guess!

    Totalguesses = 3
    rmngChance = Totalguesses-guessestaken
    if rmngChance > 0 :
        print('Good try, You still have ' +str(rmngChance)+' chances left.')
    else:
        print('Sorry, You used all chances.')

if guess == secretnumber:
    print('Good Job! You guessed my number in ' + str(guessestaken)+' guesses!')
else:
    print('Nope. the number i was thinking of was ' + str(secretnumber))