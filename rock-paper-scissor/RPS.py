#importing the libraries
import random as rnd

#deifning the moves and players in the game
moves = ['Rock', 'Paper', 'Scissor']
players = ['player1', 'player2']

#getting the suer input
turn = input('Which player do you want to play as? (player1/ player2) \n')

#check to see if the turn is available
if turn in players:
    pass
else:
    raise ValueError('This player is not defined! \n')

#setting the computer player
players.remove(turn)
computer = players[0]
computer_move = rnd.choice(moves)

#getting the player move
player_move = input('Select a move (Rock, Paper, Scissor) \n')

#check to see if the move is available
if player_move in moves:
    pass
else:
    raise ValueError('This move is not defined!')
    

life = 1
#choose the winner
print('Computer played ', computer_move)  

while(life>0):
    
    if player_move == 'Rock':
        if computer_move == 'Rock':
            print('Tie!')
        elif computer_move == 'Paper':
            print('You Lost!')
        else:
            print('You Win!')
            life -= 1
    elif player_move == 'Paper':
        if computer_move == 'Rock':
            print('You Win!')
        elif computer_move == 'Paper':
            print('Tie!')
        else:
            print('You Lost!')
            life -= 1
    else:
        if computer_move == 'Rock':
            print('You Lost!')
            life -= 1
        elif computer_move == 'Paper':
            print('You Win!')
        else:
            print('Tie!')
            life -= 1


