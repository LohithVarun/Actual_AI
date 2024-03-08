board = [" " for _ in range(9)]

def print_board():
  for i in range(3):
    print(" | ".join(board[i*3:(i*3)+3]))
    if i != 2:
      print("-" * 9)

def is_winner(player):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if all(board[i] == player for i in condition):
      return True
  return False

def is_board_full():
  return all(space != " " for space in board)

while True:
  print_board()

  player_1_move = int(input("Player 1 (X), enter your move (1-9): ")) - 1
  if board[player_1_move] != " ":
    print("Invalid move. Please choose an empty space.")
    continue
  board[player_1_move] = "X"

  if is_winner("X"):
    print_board()
    print("Player 1 (X) wins!")
    break

  if is_board_full():
    print_board()
    print("It's a tie!")
    break

  print_board()

  player_2_move = int(input("Player 2 (O), enter your move (1-9): ")) - 1
  if board[player_2_move] != " ":
    print("Invalid move. Please choose an empty space.")
    continue
  board[player_2_move] = "O"

  if is_winner("O"):
    print_board()
    print("Player 2 (O) wins!")
    break

print("Thanks for playing!")
