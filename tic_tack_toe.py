#!/usr/bin/python3
#
#
__author__ = 'bofh'

import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#------------------------------------------------------------------------------

def print_board(f_board, f_num = 3):
    print(bcolors.BOLD + bcolors.HEADER + "\n------------------------------------------\n", bcolors.BOLD + bcolors.OKBLUE + " 1", " ", "2", " ", "3", bcolors.ENDC)
    for i in range(f_num):
        print(bcolors.BOLD + " ---" * f_num)
        print("|", f_board[i][0], "|", f_board[i][1], "|", f_board[i][2], "|", bcolors.BOLD + bcolors.OKBLUE + str(i + 1), bcolors.ENDC)
    print(" ---" * f_num)

#------------------------------------------------------------------------------

def move_input(f_message, f_player1):
    if f_player1:
        f_player_str = "Player 1 " + f_message
    else:
        f_player_str = "Player 2 " + f_message

    f_move = input(f_player_str)
    f_move_list = f_move.split(",")
    f_move_list = [f_move_list[x].strip() for x in range(len(f_move_list))]
    while (len(f_move_list) != 2) or (not re.match(r'^\d+$', f_move_list[0])) or (not re.match(r'^\d+$', f_move_list[1])) or (int(f_move_list[0]) < 1) or (int(f_move_list[0]) > 3 ) or (int(f_move_list[1]) < 1) or (int(f_move_list[1]) > 3 ):
        f_move = input(f_player_str)
        f_move_list = f_move.split(",")
        f_move_list = [f_move_list[x].strip() for x in range(len(f_move_list))]

    f_row = int(f_move_list[0]) - 1
    f_col = int(f_move_list[1]) - 1
 
    return f_row, f_col

# -----------------------------------------------------------------------------

def check_if_played(f_row, f_col):
    if board[f_row][f_col] != " ":
        return True

    return False

# -----------------------------------------------------------------------------

def check_if_filled():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                f_filled = False
                break
            else:
                f_filled = True

    if (not f_filled):
        return False
    else:
        print("\nNo more available moves!\n")
        return True

# -----------------------------------------------------------------------------

def check_row_win(f_player1):
    for i in range(3):
        if (board[i][0] != " "):
            if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]):
                f_winner = f_player1
                f_won = True
                break
            else:
                f_winner = f_player1
                f_won = False

    if (f_won) and (f_player1):
        print("\nPlayer 1 won!\n")
        return True
    elif (f_won) and (not f_player1):
        print("\nPlayer 2 won!\n")
        return True
    else:
        return False

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    won = False
    filled = False
    input_message = "- enter your move as row,col: "
    
    print_board(board)
    while (not (won or filled)):
        player1 = True
        row, col = move_input(input_message, player1)
        played = check_if_played(row, col)
        while played:
            row, col = move_input(input_message, player1)
            played = check_if_played(row, col)
        board[row][col] = "X"
        print_board(board)

        won = check_row_win(player1)
        if (not won):
            filled = check_if_filled()
        
        if (not (won or filled)):
            player1 = False
            row, col = move_input(input_message, player1)
            played = check_if_played(row, col)
            while played:
                row, col = move_input(input_message, player1)
                played = check_if_played(row, col)
            board[row][col] = "O"
            print_board(board)

            won = check_row_win(player1)
