#!/usr/bin/python3
#
#
__author__ = 'bofh'

import re

class bcolors:
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    RED       = '\033[91m'
    GREEN     = '\033[92m'
    WARNING   = '\033[41m'
    BLUE      = '\033[94m'
    HEADER    = '\033[95m'
    CYAN      = '\033[96m'

#------------------------------------------------------------------------------

def print_board(f_board, f_num = 3):
    print(bcolors.BOLD + bcolors.BLUE + "  1", "  2", "  3" + bcolors.ENDC)
    print(bcolors.BOLD + " ___" * f_num)

    for i in range(f_num):
        print(bcolors.BOLD + "|" + bcolors.ENDC, f_board[i][0], bcolors.BOLD + "|" + bcolors.ENDC, f_board[i][1], bcolors.BOLD + "|" + bcolors.ENDC, f_board[i][2], bcolors.BOLD + "|", bcolors.BLUE + str(i + 1) + bcolors.ENDC)
        print(bcolors.BOLD + "|___" * f_num + "|" + bcolors.ENDC)

#------------------------------------------------------------------------------

def move_input(f_message, f_player1):
    if f_player1:
        f_player_str = "\nPlayer 1 " + f_message
    else:
        f_player_str = "\nPlayer 2 " + f_message

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

def check_if_filled(f_num = 3):
    for i in range(f_num):
        for j in range(3):
            if (board[i][j] == " "):
                f_filled = False
                break
            else:
                f_filled = True
        if (f_filled == False):
            break

    if (not f_filled):
        return False
    else:
        print(bcolors.BOLD + bcolors.WARNING + "\nNo more available moves!\n" + bcolors.ENDC)
        return True

# -----------------------------------------------------------------------------

def check_row_win(f_player1):
    f_won = False

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
        print(bcolors.BOLD + bcolors.RED + "\nPlayer 1 won!\n")
        return True
    elif (f_won) and (not f_player1):
        print(bcolors.BOLD + bcolors.CYAN + "\nPlayer 2 won!\n")
        return True
    else:
        return False

# -----------------------------------------------------------------------------

def check_col_win(f_player1):
    f_won = False

    for i in range(3):
        if (board[0][i] != " "):
            if (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]):
                f_winner = f_player1
                f_won = True
                break
            else:
                f_winner = f_player1
                f_won = False

    if (f_won) and (f_player1):
        print(bcolors.BOLD + bcolors.RED + "\nPlayer 1 won!\n")
        return True
    elif (f_won) and (not f_player1):
        print(bcolors.BOLD + bcolors.CYAN + "\nPlayer 2 won!\n")
        return True
    else:
        return False

# -----------------------------------------------------------------------------

def check_diag_win(f_player1):
    f_won = False

    if (board[0][0] != " "):
        if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
            f_winner = f_player1
            f_won = True
        else:
            f_winner = f_player1
            f_won = False

    if (not f_won):
        if (board[0][2] != " "):
            if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
                f_winner = f_player1
                f_won = True
            else:
                f_winner = f_player1
                f_won = False

    if (f_won) and (f_player1):
        print(bcolors.BOLD + bcolors.RED + "\nPlayer 1 won!\n")
        return True
    elif (f_won) and (not f_player1):
        print(bcolors.BOLD + bcolors.CYAN + "\nPlayer 2 won!\n")
        return True
    else:
        return False

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    won = False
    filled = False
    input_message = "- enter your move as row,col: "
    
    print("\033c")
    print_board(board)
    while (not (won or filled)):
        player1 = True
        row, col = move_input(input_message, player1)
        played = check_if_played(row, col)
        while played:
            row, col = move_input(input_message, player1)
            played = check_if_played(row, col)
        
        print("\033c")
        board[row][col] = bcolors.RED + "X" + bcolors.ENDC
        print_board(board)

        won = check_row_win(player1) or check_col_win(player1) or check_diag_win(player1)
        if (not won):
            filled = check_if_filled()
        
        if (not (won or filled)):
            player1 = False
            row, col = move_input(input_message, player1)
            played = check_if_played(row, col)
            while played:
                row, col = move_input(input_message, player1)
                played = check_if_played(row, col)
            board[row][col] = bcolors.CYAN + "O" + bcolors.ENDC
            print("\033c")
            print_board(board)

            won = check_row_win(player1) or check_col_win(player1) or check_diag_win(player1)
