def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)) or all(board[row][col] == 'O' for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'

        while True:
            print_board(board)

            # Get player move
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            # Check if the chosen cell is empty
            if board[row][col] != ' ':
                print("Cell already taken. Try again.")
                continue

            # Make the move
            board[row][col] = current_player

            # Check for a winner
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break  # Exit the inner loop to ask for a rematch

            # Check for a tie
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break  # Exit the inner loop to ask for a rematch

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

        # Ask for a rematch
        play_again = input('Play again? (yes/no): ')
        if play_again.lower() not in ('yes', 'y'):
            exit()  # Exit the outer loop to end the game

if __name__ == "__main__":
    tic_tac_toe()


if __name__ == "__main__":
    tic_tac_toe()