'''
Henry Quillin
Tick Tack Toe Board
10/1/2020
'''

print('Welcome to tick tack toe')
vertical = [' | | ']
horizontal = ['- - -']


def board():
    for i in range(3):
        print(vertical[0])
        if i < 2:
            print(horizontal[0])


board()

