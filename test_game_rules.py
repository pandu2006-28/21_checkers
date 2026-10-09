
from game import Checkers
from rules import has_capture, simple_move, capture_move

game = Checkers()
game.board = [["."] * 8 for _ in range(8)]

# Red has a capture available.
game.board[4][1] = "R"
game.board[3][2] = "B"
game.board[5][4] = "R"

assert has_capture(game.board, "R")

# This ordinary move is geometrically valid.
assert simple_move(game.board, "R", (5, 4), (4, 5))

# This capture is legal.
assert capture_move(game.board, "R", (4, 1), (2, 3))

print("PASS: Forced-capture test position created.")
print("PASS: Ordinary move is available geometrically.")
print("PASS: Legal capture is available.")
print("NOTE: Interactive enforcement must be verified separately.")
