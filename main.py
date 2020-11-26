# ---- Global Variables ----

# Game Board
board = ["-", "-", "-",    "-", "-", "-", "-", "-", "-", ]

# if game is still going
game_still_going = True

# Who won? or tie
winner = None

# Whose turn is it
current_player = "X"

# Print the board


def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

# Play a game of Tic tac toe


def play_game():

    # Display initial board
    display_board()

    # While the game is still going
    while game_still_going:

        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game is over
        check_if_game_over()

        # flip to the other player
        flip_player()

    # game has ended
    if winner == "X" or winner == "O":
        print(winner+" won.")
    elif winner == None:
        print("Tie.")

# handle a single turn for arbitrary player


def handle_turn(player):

    print(player + "'s turn.")
    position = input("choose a position from 1-9: ")
    # check for valid position
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or board[int(position)-1] != "-":

        position = input(
            "It is already occupied or the number is incorrect. Please input an appropriate position.  Choose a position from 1-9: ")
    position = (int(position)-1)
    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    # set up global variable
    global winner
    # check rows
    row_winner = check_rows()
    # check colunms
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    # Set up global variable
    global game_still_going
    # Check if rows have same value and not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # flag any row win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner (X or O)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_columns():
    # Set up global variable
    global game_still_going
    # Check if colums have same value and not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # flag any column win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner (X or O)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return


def check_diagonals():
    # Set up global variable
    global game_still_going
    # Check if diagonals have same value and not empty
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    # flag any diagonal win
    if diag_1 or diag_2:
        game_still_going = False
    # return the winner (X or O)
    if diag_1:
        return board[0]
    if diag_2:
        return board[2]

    return


def check_for_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # global variable needed
    global current_player
    # if current player was X, change it to O
    if current_player == "X":
        current_player = "O"
    # if the current player was O the change it to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()


# board
# display board
# play game
# handle turn
# check win
# check rows
# check colums
# check diagonals
# check tie
# flip player
