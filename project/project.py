import pyfiglet
from colorama import Fore
from tabulate import tabulate
import random


def main():
    print(Fore.BLUE, pyfiglet.figlet_format('Tic-Tac-Toe'))
    print('Choose a Game mode: ')
    print('1. Single Player')
    print('2. Multi Player', Fore.GREEN)
    mode = int(input('\n==========>   ').strip())
    single_player_game() if mode == 1 else multiplayer_game()


def print_board(board):
    print(tabulate(board, tablefmt="simple_grid"))


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def evaluate(board):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None


def minimax(board, depth, maximizing_player):
    result = evaluate(board)

    if result is not None:
        return result

    if maximizing_player:
        max_eval = float('-inf')
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        random.shuffle(available_moves)
        for i, j in available_moves:
            if board[i][j] == ' ':
                board[i][j] = 'O'
                val = minimax(board, depth + 1, False)
                board[i][j] = ' '
                max_eval = max(max_eval, val)
        return max_eval
    else:
        min_eval = float('inf')
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        random.shuffle(available_moves)
        for i, j in available_moves:
            if board[i][j] == ' ':
                board[i][j] = 'X'
                val = minimax(board, depth + 1, True)
                board[i][j] = ' '
                min_eval = min(min_eval, val)
        return min_eval


def find_best_move(board, computer):
    if computer == 'O':
        best_val = float('-inf')
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = computer
                    move_val = minimax(board, 0, False)
                    board[i][j] = ' '

                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move
    else:
        best_val = float('inf')
        best_move = (1, 1)
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = computer
                    move_val = minimax(board, 0, True)
                    board[i][j] = ' '

                    if move_val < best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move


def print_winner(winner, computer):
    if winner == 1:
        if computer == 'O':
            print(Fore.RED, pyfiglet.figlet_format('You Lose :(', font='slant'))
        else:
            print(Fore.GREEN, pyfiglet.figlet_format('You win!', font='slant'))
    elif winner == -1:
        if computer == 'X':
            print(Fore.RED, pyfiglet.figlet_format('You Lose :(', font='slant'))
        else:
            print(Fore.GREEN, pyfiglet.figlet_format('You win!', font='slant'))
    else:
        print(Fore.BLUE, pyfiglet.figlet_format('Tie??', font='slant'))


def single_player_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        try:
            current_player: str = input('Choose Your Sign (X or O): ').strip().upper()
            if current_player not in ['O', 'X']: raise ValueError('Value')
            break
        except ValueError:
            print(Fore.RED, 'Invalid Player Character', Fore.GREEN, sep='')
            pass
    if current_player == 'O':
        computer = 'X'
    else:
        computer = 'O'

    while True:
        print_board(board)
        if current_player != computer:
            print(Fore.GREEN, end='')
            try:
                row, col = map(lambda x: int(x) - 1,
                               input("Enter the row and column (1 or 2 or 3 | r, c ): ").strip().split(','))
            except ValueError:
                print(Fore.RED, 'Invalid Input Format', Fore.GREEN, sep='')
                continue
            if board[row][col] == ' ':
                board[row][col] = current_player
            else:
                print(Fore.RED, "Invalid move. Try again.", Fore.RESET)
                continue
        elif current_player == computer:
            print(Fore.RED, "Computer's turn:")
            row, col = find_best_move(board, computer)
            board[row][col] = computer
        winner = evaluate(board)

        if winner is not None:
            print_board(board)
            print_winner(winner, computer)
            break

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


def multiplayer_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = players[0]

    while True:
        print_board(board)
        row, col = map(lambda x: int(x) - 1, input(f"{current_player}'s turn - Enter the row and column (1 or 2 or 3 | r, w): ").strip().split(','))
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print(Fore.RED, "Invalid move. Try again.", Fore.RESET)
            continue

        winner = evaluate(board)

        if winner is not None:
            print_board(board)
            if winner == 1 :
                print(Fore.RED, pyfiglet.figlet_format(f'{current_player} wins!', font='slant'))
            elif winner == -1:
                print(Fore.GREEN, pyfiglet.figlet_format(f'{current_player} wins!', font='slant'))
            else:
                print(Fore.BLUE, pyfiglet.figlet_format('Tie??', font='slant'))
            break

        current_player = players[1] if current_player == players[0] else players[0]


if __name__ == "__main__":
    main()
