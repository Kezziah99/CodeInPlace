"""
This program is a game known as Tictactoe or X and Os.
The game is played by two players. They are presented with a 3 by 3 board
with 9 positions. One player is X and the other O. The players alternately place
an X or O in positions of their choice in the board.The winner will be the one that
will be first to place their letter(X or O) in three consecutive positions either
horizontally,vertically or diagonally .As players seek to ensure that they place their letter
in those positions they should also be cautious not to let their opponent win by blocking
them from putting their letter in the three consecutive positions stated above. If the board
gets full before any player wins, the game is declared a tie.
"""
import random

def main():
    print("                                 TICTACTOE")
    print("      Two players are required to play this game. Player 1 plays x and Player 2 plays o. ")
    print("             Your task is to place an x or an o at the position of your choice.")
    print("You win when you place your letter in three consecutive positions horizontally, vertically or diagonally.")
    print("             Ensure your opponent does not win by blocking them using your letter.")
    bd = []
    size = 3
    for i in range(size**2):
        bd.append('_')
    print(" ")
    print("This is the board:")
    display_board(bd, size)
    print("These are the positions to place your letter:")
    display_positions(size)
    play(bd, size)

def play(bd, size):
    """
    This function gives players alternate turns to play then checks if either player
    has won or if their is a tie and ends the game is so. If not, the game continues.
    :param bd:
    :param size:
    :return:
    """
    while True:
       player1(bd)
       display_board(bd, size)
       winner = check_winner(bd)
       if winner:
           break
       print(" ")
       player2(bd)
       display_board(bd, size)
       winner = check_winner(bd)
       if winner:
           break
       print(" ")

def display_positions(size):
    """
    Displays the positions that a player can play.
    :param size:
    :return:
    """
    bod = []
    for i in range(size*size + 6):
        bod.append(i+1)
    k = 0
    for y in range(size + 3):
        for x in range(size):
            if y % 2 == 0:
                if x != 2 and x != 8 and x != 14:
                    print(str(bod[k]) + " ", end=' ')
                    k += 1
                else:
                    print(str(bod[k]), end=' ')
                    k += 1

            else:
                print('_  ', end='')
        print("")

def display_board(bd, size):
    """
    Updates and displays the board.
    :param bd:
    :param size:
    :return:
    """
    k = 0
    for y in range(size):
        for x in range(size):
            print(str(bd[k]) + " ", end=' ')
            k += 1
        print(" ")

def player1(bd):
    """
    Takes in the position the player chooses to play and checks if it is valid.
    if valid, it appends an x to that position
    :param bd:
    :return:
    """
    pos = int(input("Player 1 choose a position to play in terms of numbers displayed on board: "))
    while pos < 1 or pos > len(bd):
        print("Invalid position. ", end='')
        pos = int(input("Choose a position to play in terms of numbers displayed on board: "))
    while bd[pos-1] == 'x' or bd[pos-1] == 'o':
        pos = int(input("Position already played. Choose another position to play: "))
    bd[pos-1] = 'x'

def player2(bd):
    """
    Takes in the position the player chooses to play and checks if it is valid.
    if valid, it appends an o to that position
    :param bd:
    :return:
    """
    pos = int(input("Player 2 choose a position to play in terms of numbers displayed on board: "))
    while pos < 1 or pos > len(bd):
        print("Invalid position. ", end='')
        pos = int(input("Choose a position to play in terms of numbers displayed on board: "))
    while bd[pos - 1] == 'x' or bd[pos - 1] == 'o':
        pos = int(input("Position already played.Choose another position to play: "))
    bd[pos - 1] = 'o'

def check_winner(bd):
    """
    Checks if either player has placed their letter in three consecutive positions horizontally,
    vertically or diagonally and declares them the winner.
    If board gets full before anyone wins, it declares a tie.
    :param bd:
    :return:
    """
    tie = check_tie(bd)
    if bd[0]=='x' and bd[1] == 'x' and bd[2] == 'x':
        print(" ")
        print("Player 1 wins")
        return True
    elif bd[0]=='x' and bd[3] == 'x' and bd[6] == 'x':
        print(" ")
        print("Player 1 wins")
        return True
    elif bd[0]=='x' and bd[4] == 'x' and bd[8] == 'x':
        print(" ")
        print("Player 1 wins")
        return True
    elif bd[1]=='x' and bd[4] == 'x' and bd[7] == 'x':
        print(" ")
        print("Player 1 wins")
        return True
    elif bd[2]=='x' and bd[5] == 'x' and bd[8] == 'x':
        print(" ")
        print("Player 1 wins")
        return True
    elif bd[3]=='x' and bd[4] == 'x' and bd[5] == 'x':
        print(" ")
        print("Player 1 wins")
        return True
    elif bd[6]=='x' and bd[7] == 'x' and bd[8] == 'x':
        print(" ")
        print("Player 1 wins")
        return True
    elif bd[2]=='x' and bd[4] == 'x' and bd[6] == 'x':
        print(" ")
        print("Player 1 wins")
        return True
    elif bd[0]=='o' and bd[1] == 'o' and bd[2] == 'o':
        print(" ")
        print("Player 2 wins")
        return True
    elif bd[0]=='o' and bd[3] == 'o' and bd[6] == 'o':
        print(" ")
        print("Player 2 wins")
        return True
    elif bd[0]=='o' and bd[4] == 'o' and bd[8] == 'o':
        print("Player 2 wins")
        return True
    elif bd[1]=='o' and bd[4] == 'o' and bd[7] == 'o':
        print(" ")
        print("Player 2 wins")
        return True
    elif bd[2]=='o' and bd[5] == 'o' and bd[8] == 'o':
        print(" ")
        print("Player 2 wins")
        return True
    elif bd[3]=='o' and bd[4] == 'o' and bd[5] == 'o':
        print(" ")
        print("Player 2 wins")
        return True
    elif bd[6]=='o' and bd[7] == 'o' and bd[8] == 'o':
        print(" ")
        print("Player 2 wins")
        return True
    elif bd[2]=='o' and bd[4] == 'o' and bd[6] == 'o':
        print(" ")
        print("Player 2 wins")
        return True
    elif tie:
        print(" ")
        print("It's a tie")
        return True

def check_tie(bd):
    """
    checks if board is full and returns a boolean.
    :param bd:
    :return:
    """
    k = 0
    for i in range(len(bd)):
        if bd[i] == 'x' or bd[i] == 'o':
            k += 1
    if k == len(bd):
        return True
    else:
        return False

if __name__ == '__main__':
    main()