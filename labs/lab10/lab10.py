"""
Name: Trent Varnes
lab10.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def display_board(board):
    print("{0} {1} {2}".format(board[0], board[1], board[2]))
    print("{0} {1} {2}".format(board[3], board[4], board[5]))
    print("{0} {1} {2}".format(board[6], board[7], board[8]))
    return

def fill_spot(board, pos, char):
    if board[pos-1] == "X" or board[pos-1] == "O":
        return " "
    else:
        board[pos-1] = char


def is_legal(board, pos):
    if board[pos-1] == "X" or "O":
        return False
    else:
        return True


def game_won(board):
    if board[0] == board[1] == board[2] == "O" or "X":
        return True
    elif board[3] == board[4] == board[5] == "O" or "X":
        return True
    elif board[6] == board[7] == board[8] == "O" or "X":
        return True
    elif board[0] == board[3] == board[6] == "O" or "X":
        return True
    elif board[1] == board[4] == board[7] == "O" or "X":
        return True
    elif board[2] == board[5] == board[8] == "O" or "X":
        return True
    elif board[0] == board[4] == board[8] == "O" or "X":
        return True
    elif board[2] == board[4] == board[6] == "O" or "X":
        return True
    else:
        return False


def game_over(board):
    acc = 0
    for i in board:
        if i == "X" or i == "O":
            acc += 1

    if game_won(board):
        return True

    elif acc == 9:
        return True
    else:
        return False


def play_game():
      board = build_board()
      print(display_board(board))
      player = input("player 1 or player 2: ")
      acc = 0
      while acc != 9:
          char = input("enter X or O: ")
          pos = eval(input("enter a position: "))
          if char == "X":
              fill_spot(board, pos, char)
              is_legal(board, pos)
              game_won(board)
              game_over(board)
              acc += 1
          elif char == "Y":
              fill_spot(board, pos, char)
              is_legal(board, pos)
              game_won(board)
              game_over(board)
              acc += 1





def main():
    #board = build_board()
    #char = "X" or "O"
    #display_board(board)
    #fill_spot(board, 7, char)
    #is_legal(board, 7)
    #game_won(board)
    #game_over(board)
    play_game()


if __name__ == '__main__':
    main()


