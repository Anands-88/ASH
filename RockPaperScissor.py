import random, sys

print('Rock, Paper, Scissors')

# These variables keep track of the number of wins, losses, ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s wins, %s losses, %s ties' %(wins, losses, ties))
    while True:# the player input loop.
        print('enter your move:(r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()# qiut the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r,p,s,or q.')

    #Display what the player chose:
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus ...')
    elif playerMove == 's':
        print('Scissors versus ...')


    #Display What the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
            computerMove = 'r'
            print('Rock')
    elif randomNumber == 2:
            computerMove = 'p'
            print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissor')

    
    #Display and record the win/lose/tie:
    if playerMove == computerMove:
        print('it is tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('you win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('you win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('you win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('you lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('you lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('you lose!')
        losses = losses + 1