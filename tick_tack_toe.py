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
    # insert an x or O into an array
    # my_board_array[4] = O
# Check for winner/tie condition
# Win/lose message (with ASCII art)
# Ask user to play again




check_for_x = ["X", "X", "X"]
board = [
    ["X", "X", " "],
    ["X", "x", "X"],
    [" ", " ", "0"]
]
print(f'''
    0 1 2
   _______
0 | {board[0][0]}|{board[0][1]}|{board[0][2]} |
  | -+-+- | 
1 | {board[1][0]}|{board[1][1]}|{board[1][2]} |
  | -+-+- |                                    
2 | {board[2][0]}|{board[2][1]}|{board[2][2]} | 
   -------
''')
def didiwin():
    if board[0][0] == board [0][1] and board[0][0] == board[0][2]:
        print(board[0][0], 'is the winner row')

didiwin()

player1_col = input('Player 1 please enter you column ')
player1_row = input('Player 1 please enter you row ')
board[player1_col]

print('Welcome to Tic-Tac- Toe')
num_of_players = input('Choose number of players (0, 1 or 2): ') # Input for # of players
print(f'You have chosen to play with {num_of_players} players')

x_or_o = input("Chose X's or O's: ").upper() # Input for X or O's
if x_or_o == 'X':
    print("Player 1 is X's and player 2 is O's")
else:
    print("Player 1 is O's and player 2 is X's")

board()
