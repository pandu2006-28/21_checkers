
SIZE = 8


def simple_move(board, player, start, end):
    sr, sc = start
    er, ec = end

    direction = -1 if player == "R" else 1
    piece = board[sr][sc]

    if piece not in (player, player + "K"):
        return False

    if board[er][ec] != ".":
        return False

    if abs(er - sr) != 1 or abs(ec - sc) != 1:
        return False

    # Kings can move forward and backward.
    if piece.endswith("K"):
        return True

    return er - sr == direction


def capture_move(board, player, start, end):
    sr, sc = start
    er, ec = end

    piece = board[sr][sc]
    direction = -1 if player == "R" else 1

    if piece not in (player, player + "K"):
        return False

    if board[er][ec] != ".":
        return False

    if abs(er - sr) != 2 or abs(ec - sc) != 2:
        return False

    # Kings can capture in both directions.
    if not piece.endswith("K") and er - sr != 2 * direction:
        return False

    mr = (sr + er) // 2
    mc = (sc + ec) // 2
    middle_piece = board[mr][mc]

    return middle_piece not in (".", player, player + "K")


def promote(board):
    for c in range(SIZE):
        if board[0][c] == "R":
            board[0][c] = "RK"

        if board[SIZE - 1][c] == "B":
            board[SIZE - 1][c] = "BK"


def has_pieces(board, player):
    """Check whether the player has any pieces remaining."""
    return any(
        piece in (player, player + "K")
        for row in board
        for piece in row
    )


def has_legal_move(board, player):
    """Check whether the player has at least one legal move."""
    direction = -1 if player == "R" else 1

    for r in range(SIZE):
        for c in range(SIZE):
            piece = board[r][c]

            if piece not in (player, player + "K"):
                continue

            directions = [-1, 1] if piece.endswith("K") else [direction]

            for dr in directions:
                for dc in (-1, 1):
                    # Check a one-square diagonal move.
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < SIZE
                        and 0 <= nc < SIZE
                        and board[nr][nc] == "."
                    ):
                        return True

                    # Check a two-square diagonal capture.
                    mr, mc = r + dr, c + dc
                    nr, nc = r + 2 * dr, c + 2 * dc

                    if not (
                        0 <= mr < SIZE
                        and 0 <= mc < SIZE
                        and 0 <= nr < SIZE
                        and 0 <= nc < SIZE
                    ):
                        continue

                    middle_piece = board[mr][mc]

                    if (
                        board[nr][nc] == "."
                        and middle_piece != "."
                        and middle_piece not in (player, player + "K")
                        and (piece.endswith("K") or dr == direction)
                    ):
                        return True

    return False
