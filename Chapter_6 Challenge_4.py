X = 'X'
O = 'O'
empty = ' '
tie = 'TIE'
num_squares = 9


def display_instructions():
    print(
        '''

        TIC-TAC-TOE

        You will make your move by entering a number 0 - 8

                0 | 1 | 2
                ---------
                3 | 4 | 5 
                ---------
                6 | 7 | 8

        ''')


def yes_no_question(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    go_first = yes_no_question('Do you want the first move? (y,n) : ')
    if go_first == 'y':
        print('\nYou now have the first move.')
        human = X
        computer = O

    else:
        print('\nThe computer will have the first move.')
        computer = X
        human = O
    return computer, human


def new_board():
    board = []
    for square in range(num_squares):
        board.append(empty)
    return board


def print_board(board):
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '---------')
    print('\n\t', board[3], '|', board[4], '|', board[5])
    print('\t', '---------')
    print('\n\t', board[6], '|', board[7], '|', board[8])


def legal_moves(board):
    moves = []
    for square in range(num_squares):
        if board[square] == empty:
            moves.append(square)
    return moves


def winner(board):
    ways_to_win = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner
    if empty not in board:
        return tie
    return None


def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Where will you move? (0 - 8) : ', 0, num_squares)
        if move not in legal:
            print('\nThat square is already occupied, Choose another.\n')
    print('OK')
    return move


def computer_move(board, computer, human):
    board = board[:]
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print('I will take square number ', end='')
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = empty
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = empty
    for move in best_moves:
        if move in legal_moves(board):
            print(move)
            return move
        elif move not in legal_moves(board):
            if best_moves[5] in legal_moves(board):
                print(best_moves[5])
                return best_moves[5]


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


def congratulate_player(the_winner, computer, human):
    if the_winner != tie:
        print(the_winner, 'won!\n')
    else:
        print('It\'s a tie\n')

    if the_winner == computer:
        print('I won')
    elif the_winner == human:
        print('You won')
    elif the_winner == tie:
        print('Its a tie')


def main():
    display_instructions()
    computer, human = pieces()
    turn = X
    board = new_board()
    print_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        print_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()
