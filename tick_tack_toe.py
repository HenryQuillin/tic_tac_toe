'''
Henry Quillin
Tick Tack Toe Board
10/1/2020
'''
# / Welcome message
# / Draw Board
# / Choose number of players (0 - 2)
# Use .random to pick who goes first
# / Place first entry on the board
# / Gameplay
    # insert an x or O into an array
    # my_board_array[4] = O
# Check for winner/tie condition
# Win/lose message (with ASCII art)
# Ask user to play again

#variables
check_for_x = ["X", "X", "X"]
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
#functions
def printboard():
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
def p1turn():
    p1_row = int(input('Player 1 please enter your row '))
    p1_col = int(input('Player 1 please enter your column '))
    board[p1_row][p1_col] = p1_x_or_o
    printboard()
    win_check()
def p2turn():
    p2_row = int(input('Player 2 please enter your row '))
    p2_col = int(input('Player 2 please enter your column '))
    board[p2_row][p2_col] = p2_x_or_o
    printboard()
    win_check()
didiwin = False
def win_check():
    if board[0][0] == board [0][1] and board[0][0] == board[0][2]:
        didiwin = False
        print(f"{board[0][0]}'s are the winner!")


print('Welcome to Tic-Tac- Toe') #welcome message
# num_of_players = input('Choose number of players (0, 1 or 2): ') # Input for # of players
# print(f'You have chosen to play with {num_of_players} players')

x_or_o = input("Player 1, chose X's or O's: ").upper() # Input for X or O's
if x_or_o == 'X':
    p1_x_or_o = 'X'
    p2_x_or_o = 'O'
    print("Player 1 is X's and player 2 is O's")
else:
    p1_x_or_o = 'O'
    p2_x_or_o = 'X'
    print("Player 1 is O's and player 2 is X's")
printboard()
while didiwin == False:
    p1turn()
    if didiwin == False:
        break
    p2turn()


'''
Gameplay loop: 
- While didiwin is false: 
    - p1 turn 
    - p2 turn 
- Else: 
    - (winning player) has won! 
    - Would you like to play again? 
'''