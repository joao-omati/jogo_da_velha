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

def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if not available_moves(board):
        return 0
    
    if is_maximizing:
        best_score = -float("inf")
        for (r, c) in available_moves(board):
            board[r][c] = "O"
            score = minimax(board, depth + 1, False)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for (r, c) in available_moves(board):
            board[r][c] = "X"
            score = minimax(board, depth + 1, True)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    move = None
    for (r, c) in available_moves(board):
        board[r][c] = "O"
        score = minimax(board, 0, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Bem-vindo ao Jogo da Velha!")
    print_board(board)
    
    while True:
        # Jogador "X"
        move = None
        while move not in available_moves(board):
            try:
                move = tuple(map(int, input("Digite sua jogada (linha e coluna, ex: 1 2): ").split()))
            except ValueError:
                pass
        board[move[0]][move[1]] = "X"
        print_board(board)
        if check_winner(board, "X"):
            print("Você venceu!")
            break
        if not available_moves(board):
            print("Empate!")
            break
        
        # IA "O"
        print("Vez da IA...")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("A IA venceu!")
            break
        if not available_moves(board):
            print("Empate!")
            break

if __name__ == "__main__":
    main()
