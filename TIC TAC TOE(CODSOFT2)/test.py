import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

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

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, maximizing_player):
    if check_winner(board, "X"):
        return -1
    if check_winner(board, "O"):
        return 1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_score = float("-inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe AI")
    print_board(board)
    
    while not is_full(board):
        row, col = None, None
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Try again.")
        
        board[row][col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        print("AI is making its move...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()