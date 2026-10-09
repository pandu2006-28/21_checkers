
def move_piece(board, start, end):
    sr, sc = start
    er, ec = end

    # Remember the moving piece.
    piece = board[sr][sc]

    # Remove the jumped opponent during a capture.
    if abs(er - sr) == 2 and abs(ec - sc) == 2:
        mr = (sr + er) // 2
        mc = (sc + ec) // 2
        board[mr][mc] = "."

    # Move the piece and clear its original square.
    board[er][ec] = piece
    board[sr][sc] = "."
