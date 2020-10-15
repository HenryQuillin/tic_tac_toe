'''
Henry Quillin
Tick Tack Toe Board
10/1/2020
'''
import sys

# / Welcome message
# / Draw Board
# / Choose number of players (0 - 2)
# Use .random to pick who goes first
# / Place first entry on the board
# / Gameplay
# / Check for winner/tie condition
# / Win/lose message (with ASCII art)
# make tie condition
#
# Ask user to play again

# variables
didiwin = False
winning_position_msg = ' '
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
p1_x_or_o = ' '
p2_x_or_o = ' '


# functions
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


def choose_x_or_o():
    global p1_x_or_o
    global p2_x_or_o
    x_or_o = input("Player 1, chose X's or O's: ").upper()  # Input for X or O's
    if x_or_o == 'X':
        p1_x_or_o = 'X'
        p2_x_or_o = 'O'
        print("Player 1 is X's and player 2 is O's")
    else:
        p1_x_or_o = 'O'
        p2_x_or_o = 'X'
        print("Player 1 is O's and player 2 is X's")

    printboard()


def p1turn():  # Function for player 1's turn
    p1_row = int(input('Player 1 please enter your row '))
    p1_col = int(input('Player 1 please enter your column '))

    if board[p1_row][p1_col] == 'X' or board[p1_row][p1_col] == 'O':
        print('Oops! This spot has already been taken')
        p1turn()
    board[p1_row][p1_col] = p1_x_or_o
    printboard()
    win_check()


def p2turn():  # Function for player 1's turn
    p2_row = int(input('Player 2 please enter your row '))
    p2_col = int(input('Player 2 please enter your column '))
    if board[p2_row][p2_col] == 'X' or board[p2_row][p2_col] == 'O':
        print('Oops! This spot has already been taken')
        p2turn()
    board[p2_row][p2_col] = p2_x_or_o
    printboard()
    win_check()


def win_check():  # Function to check winning condition
    # row 0, row 1, row 2, col 0, col 1, col 2, across left, across right
    global didiwin
    global winning_position_msg
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != ' ':
        didiwin = True
        winning_position_msg = 'row 0'
    if board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != ' ':
        didiwin = True
        winning_position_msg = 'row 1'
    if board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != ' ':
        didiwin = True
        winning_position_msg = 'row 2'
    if board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != ' ':
        didiwin = True
        winning_position_msg = 'col 0'
    if board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != ' ':
        didiwin = True
        winning_position_msg = 'col 1'
    if board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != ' ':
        didiwin = True
        winning_position_msg = 'col 2'
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[2][2] != ' ':
        didiwin = True
        winning_position_msg = 'a diagonal from 0,0 to 2,2'
    if board[0][2] == board[1][1] and board[0][2] == board[0][2] and board[0][2] != ' ':
        didiwin = True
        winning_position_msg = 'a diagonal from 0,2 to 0,2'
    count = 0
    for i in range(3):  # Check if there is a tie
        for y in range(3):
            if board[i][y] != ' ':
                count += 1
                y += 1
    if count == 9:
        didiwin == True
        print('Its a tie!')


def clear_board():  # Clears board
    global board
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


print('Welcome to Tic-Tac- Toe')  # welcome message
# num_of_players = input('Choose number of players (0, 1 or 2): ') # Input for # of players
# print(f'You have chosen to play with {num_of_players} players')


choose_x_or_o()

while didiwin == False:  # Gameplay loop
    p1turn()
    win_check()
    if didiwin == True:
        print(f"Player 1 won with {winning_position_msg}!")
        print('♪┏(・o･)┛♪┗ ( ･o･) ┓♪')
        playagain = input('Would you like to play again?(y/n)')
        if playagain == 'y':
            didiwin == False
            clear_board()
            choose_x_or_o()
        else:
            print('Goodbye')
            break
    p2turn()
    win_check()
    if didiwin == True:
        print(f"Player 2 won with {winning_position_msg}!")
        print('♪┏(・o･)┛♪┗ ( ･o･) ┓♪')
        playagain = input('Would you like to play again?(y/n)')
        if playagain == 'y':
            didiwin == False
            clear_board()
            choose_x_or_o()
        else:
            print('Goodbye')
            break

'''
Gameplay loop: 
- While didiwin is false: 
    - p1 turn 
    - p2 turn  
- Else: 
    - (winning player) has won! 
    - Would you like to play again? 
'''
