'''
Henry Quillin
Tick Tack Toe Board
10/1/2020
'''
# / Welcome message
# / Draw Board
# / Choose number of players (0 - 2)
# Use .random to pick who goes first
# Place first entry on the board
# Gameplay
# Check for winner/tie condition
# Win/lose message (with ASCII art)
# Ask user to play again



vertical = [' | | ']
horizontal = ['- - -']


def board():
    for i in range(3):
        print(vertical[0])
        if i < 2:
            print(horizontal[0])



print('Welcome to Tic-Tac- Toe')
num_of_players = input('Choose number of players (0, 1 or 2): ') # Input for # of players
print(f'You have chosen to play with {num_of_players} players')

x_or_o = input("Chose X's or O's: ").upper() # Input for X or O's
if x_or_o == 'X':
    print("Player 1 is X's and player 2 is O's")
else:
    print("Player 1 is O's and player 2 is X's")

board()
