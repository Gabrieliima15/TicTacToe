from os import system # Used for clearing the outputs
from time import sleep # Used for delay

# Initializing board
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

next = 0 # Indicates next player
x1 = False # Player1 is X
x2 = False # Player2 is X

# Clears the outputs
def clear():
    _ = system('clear') # Change to 'cls' if running on windows

# Starts the game, asks what will be player1's symbol
def beginGame():
    global next, x1, x2, name1, name2
    print('\nWelcome to Tic Tac Toe!\n')
    choice = 'wrong' # Placeholder value
    name1 = input('Player 1: Insert your name: ')
    name2 = input('Player 2: Insert your name: ')

    while choice not in ['O', 'X', 'o', 'x']:
        choice = input(f'\n{name1}: Do you want to be X or O? ')

        if choice.lower() == 'x':
            print(f'{name1} will go first.')
            next = 1
            x1 = True
        elif choice.lower() == 'o':
            print(f'{name2} will go first.')
            next = 2
            x2 = True
        else:
            continue

# Prints and updates the board
def show_board():
    sleep(0.5)
    clear()

    print(f'\n  {row1[0]}  |  {row1[1]}  |  {row1[2]} ')
    print('\n' + '------------------')
    print(f'\n  {row2[0]}  |  {row2[1]}  |  {row2[2]} ')
    print('\n' + '------------------')
    print(f'\n  {row3[0]}  |  {row3[1]}  |  {row3[2]} ')

# lets each player decide where to draw an X or O
def turn(name, marker):
    global row1, row2, row3
    turn = 'wrong' # Placeholder value

    while True:
            turn = input(f'\n{name}: choose your position ({marker}): (1-9)\n')
            
            if turn.isdigit() == False: # Check if the input is not a digit
                print('\nInvalid input, try again\n')
                continue
            
            turn = int(turn)

            # Updates the values of the board
            if turn in range(1, 4):
                row3[turn-1] = marker
                break
            elif turn in range(4, 7):
                row2[turn-4] = marker
                break
            elif turn in range(7, 10):
                row1[turn-7] = marker
                break
            else:
                print('\nInvalid input, try again\n')

# Check if someone won the game
def check_win(mark):
    return ((row1[0] == mark and row1[1] == mark and row1[2] == mark) or 
    (row2[0] == mark and row2[1] == mark and row2[2] == mark) or 
    (row3[0] == mark and row3[1] == mark and row3[2] == mark) or 
    (row1[0] == mark and row2[0] == mark and row3[0] == mark) or 
    (row1[1] == mark and row2[1] == mark and row3[1] == mark) or 
    (row1[2] == mark and row2[2] == mark and row3[2] == mark) or
    (row1[0] == mark and row2[1] == mark and row3[2] == mark) or 
    (row1[2] == mark and row2[1] == mark and row3[0] == mark))

# Check if the board is full
def check_full():
    for x in row1:
        if x == ' ':
            return False
    for x in row2:
        if x == ' ':
            return False
    for x in row3:
        if x == ' ':
            return False
    return True

beginGame()

# Runs the game until someone wins or the board is full
while True:
    show_board()
    if next == 1 and x1: 
        turn(name1, 'X')
        next = 2
    elif next == 1 and x2:
        turn(name1, 'O')
        next = 2
    elif next == 2 and x2:
        turn(name2, 'X')
        next = 1
    else:
        turn(name2, 'O')
        next = 1

    if check_win('X'):
        if x1:
            show_board()
            print(f'\n{name1} is the winner !!!')
            break
        
        else:
            show_board()
            print(f'\n{name2} is the winner !!!')
            break
    
    elif check_win('O'):
        if x2:
            show_board()
            print(f'\n{name1} is the winner !!!')
            break
        
        else:
            show_board()
            print(f'\n{name2} is the winner !!!')
            break 

    elif check_full():
        show_board()
        print('\nGame over !!!')
        break   