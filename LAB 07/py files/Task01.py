
import heapq

# Simple 4x4 chess-like board for demonstration
# 'w' = white piece, 'b' = black piece, '.' = empty
def initial_board():
    return [
        ['w', 'w', 'w', 'w'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['b', 'b', 'b', 'b']
    ]

# Generate all possible moves for the current player (very simplified)
def generate_moves(board, white_to_move):
    moves = []
    for r in range(4):
        for c in range(4):
            piece = board[r][c]
            if white_to_move and piece == 'w' and r < 3 and board[r+1][c] == '.':
                # White moves forward
                new_board = [row[:] for row in board]
                new_board[r][c] = '.'
                new_board[r+1][c] = 'w'
                moves.append(((r, c, r+1, c), new_board))
            elif not white_to_move and piece == 'b' and r > 0 and board[r-1][c] == '.':
                # Black moves forward
                new_board = [row[:] for row in board]
                new_board[r][c] = '.'
                new_board[r-1][c] = 'b'
                moves.append(((r, c, r-1, c), new_board))
    return moves

# Simple evaluation: difference in piece count
def evaluate_board(board):
    white = sum(cell == 'w' for row in board for cell in row)
    black = sum(cell == 'b' for row in board for cell in row)
    return white - black

# Beam Search for chess-like move prediction
def beam_search_chess(board, beam_width=2, depth_limit=2, white_to_move=True):
    # Each element: (neg_eval_score, [move1, move2, ...], board, white_to_move)
    beam = [(0, [], board, white_to_move)]
    for depth in range(depth_limit):
        candidates = []
        for eval_score, move_seq, b, wtm in beam:
            moves = generate_moves(b, wtm)
            if not moves:
                candidates.append((eval_score, move_seq, b, wtm))
                continue
            for move, new_board in moves:
                score = evaluate_board(new_board)
                # For white, maximize; for black, minimize
                signed_score = score if wtm else -score
                candidates.append((-signed_score, move_seq + [move], new_board, not wtm))
        # Select top-k (lowest neg_eval_score = highest score for white)
        beam = heapq.nsmallest(beam_width, candidates, key=lambda x: x[0])
        if not beam:
            break
    # Choose the best sequence from the final beam
    if beam:
        best = min(beam, key=lambda x: x[0])
        return best[1], -best[0]
    return [], 0

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


board = initial_board()
beam_width = 3
depth_limit = 2
move_seq, eval_score = beam_search_chess(board, beam_width=beam_width, depth_limit=depth_limit, white_to_move=True)
print("Initial board:")
print_board(board)
if move_seq:
    print("Best move sequence:")
    b = [row[:] for row in board]
    wtm = True
    for move in move_seq:
        print(f"{'White' if wtm else 'Black'}: {move}")
        # Apply move
        r1, c1, r2, c2 = move
        b[r2][c2] = b[r1][c1]
        b[r1][c1] = '.'
        print_board(b)
        wtm = not wtm
    print(f"Evaluation score: {eval_score}")
else:
    print("No move sequence found.")

