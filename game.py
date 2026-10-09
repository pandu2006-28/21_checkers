
from board import initial_board, move_piece, SIZE
from rules import (
    simple_move,
    capture_move,
    promote,
    has_pieces,
    has_legal_move,
)


class Checkers:
    def __init__(self):
        self.board = initial_board()
        self.player = "R"

    def print_board(self):
        print("\n   " + " ".join(str(c) for c in range(SIZE)))

        for r, row in enumerate(self.board):
            print(f"{r}  " + " ".join(row))

    def run(self):
        print("Checkers — move: sr sc er ec (or q to quit)")

        while True:
            self.print_board()

            raw = input(f"{self.player}> ").strip().lower().split()

            if raw == ["q"]:
                print("Game ended.")
                return

            if len(raw) != 4:
                print("Enter four coordinates.")
                continue

            try:
                sr, sc, er, ec = map(int, raw)
            except ValueError:
                print("Coordinates must be numbers.")
                continue

            if not all(0 <= x < SIZE for x in (sr, sc, er, ec)):
                print("Outside board.")
                continue

            start = (sr, sc)
            end = (er, ec)

            if self.board[sr][sc] not in (
                self.player,
                self.player + "K",
            ):
                print("That is not your piece.")
                continue

            if capture_move(self.board, self.player, start, end):
                move_piece(self.board, start, end)
                print(f"{self.player} captures a piece.")

            elif simple_move(self.board, self.player, start, end):
                move_piece(self.board, start, end)
                print(f"{self.player} moves to ({er}, {ec}).")

            else:
                print("Invalid move.")
                continue

            promote(self.board)

            # Switch to the opponent.
            self.player = "B" if self.player == "R" else "R"

            # Check whether the opponent has any pieces.
            if not has_pieces(self.board, self.player):
                winner = "R" if self.player == "B" else "B"
                self.print_board()
                print(f"{winner} wins! The opponent has no pieces left.")
                return

            # Check whether the opponent can make any legal move.
            if not has_legal_move(self.board, self.player):
                winner = "R" if self.player == "B" else "B"
                self.print_board()
                print(f"{winner} wins! The opponent has no legal moves.")
                return
