# Tic-Tac-Toe with Minimax Algorithm
import math

# Board setup (empty spaces represented by '-')
board = ['-' for _ in range(9)]

# Print the Tic-Tac-Toe board
def print_board():
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for empty cells
def is_moves_left():
    return '-' in board

# Check the current board state (winner or draw)
def evaluate():
    # Winning patterns: rows, columns, diagonals
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    
    # Check if there's a winner
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != '-':
            if board[pattern[0]] == 'O':
                return 10  # AI win
            elif board[pattern[0]] == 'X':
                return -10  # Human win
    
    return 0  # No winner

# Minimax algorithm
def minimax(depth, is_max):
    score = evaluate()

    # If AI has won, return score
    if score == 10:
        return score - depth  # Favor quicker wins
    
    # If human has won, return score
    if score == -10:
        return score + depth  # Favor quicker losses

    # If there are no moves left and no winner, it's a draw
    if not is_moves_left():
        return 0

    # Maximizing player (AI)
    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O'
                best = max(best, minimax(depth + 1, False))
                board[i] = '-'
        return best

    # Minimizing player (Human)
    else:
        best = math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = 'X'
                best = min(best, minimax(depth + 1, True))
                board[i] = '-'
        return best

# Find the best move for the AI
def find_best_move():
    best_val = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == '-':
            board[i] = 'O'
            move_val = minimax(0, False)
            board[i] = '-'
            if move_val > best_val:
                best_move = i
                best_val = move_val

    return best_move

# Check if the game is over (win or draw)
def is_game_over():
    return evaluate() != 0 or not is_moves_left()

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while not is_game_over():
        # Human turn (X)
        human_move = int(input("\nEnter your move (1-9): ")) - 1
        if board[human_move] == '-':
            board[human_move] = 'X'
            print_board()

            if is_game_over():
                break

            # AI turn (O)
            print("\nAI is making its move...")
            ai_move = find_best_move()
            board[ai_move] = 'O'
            print_board()

    # Game over, check result
    result = evaluate()
    if result == 10:
        print("AI wins!")
    elif result == -10:
        print("You win!")
    else:
        print("It's a draw!")

# Start the game
play_game()
