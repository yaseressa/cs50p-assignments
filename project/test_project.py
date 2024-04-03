import pytest
from project import check_winner, is_board_full, evaluate, minimax, find_best_move


def test_check_winner():
    board1 = [['X', 'X', 'X'], ['O', 'O', ' '], [' ', ' ', ' ']]
    board2 = [['O', 'X', 'O'], [' ', 'X', 'O'], ['X', ' ', ' ']]
    assert check_winner(board1, 'X') == True
    assert check_winner(board2, 'X') == False
    assert not check_winner(board1, 'O') == True
    assert not check_winner(board2, 'O') == True


def test_is_board_full():
    board1 = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
    board2 = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', ' ']]
    assert is_board_full(board1) == True
    assert is_board_full(board2) == False


def test_evaluate():
    board1 = [['X', 'X', 'X'], ['O', 'O', ' '], [' ', ' ', ' ']]
    board2 = [['O', 'X', 'O'], [' ', 'X', 'O'], ['X', ' ', ' ']]
    board3 = [['O', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
    assert evaluate(board1) == -1
    assert not evaluate(board2)
    assert evaluate(board3) == 1


def test_minimax():
    board = [['X', 'O', ' '], [' ', 'X', 'O'], ['O', ' ', 'X']]
    assert minimax(board, 0, True) == -1


def test_find_best_move():
    board = [['X', 'O', ' '], [' ', 'X', 'O'], ['O', ' ', 'X']]
    assert find_best_move(board, 'O') == (0, 2)
