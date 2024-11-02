import math

# Initialize the game board
board = [" " for _ in range(9)]

def display_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

def check_winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(b[i] == player for i in condition) for condition in win_conditions)

def minimax(b, depth, is_maximizing):
    # Check for terminal states (win, lose, or draw)
    if check_winner(b, "O"):
        return 1
    elif check_winner(b, "X"):
        return -1
    elif " " not in b:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

def play_game():
    print("Hi, this is a tic-tac-toe game; please choose a position to place an 'X' on the following board")
    display_board()
    
    while True:
        # Player move
        move = int(input("Choose a position (1-9): ")) - 1
        if board[move] == " ":
            board[move] = "X"
            print("End of round:", move + 1)
        else:
            print("Position taken. Choose another.")
            continue

        # Display board after player move
        display_board()
        
        # Check if player won
        if check_winner(board, "X"):
            print("Player wins!")
            break
        elif " " not in board:
            print("It's a draw!")
            break

        # AI move
        ai_move()
        display_board()
        
        # Check if AI won
        if check_winner(board, "O"):
            print("AI wins!")
            break
        elif " " not in board:
            print("It's a draw!")
            break
play_game()