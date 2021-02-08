import time
from src.game import Game

g = Game()

while True:
    g.move()
    g.print_hands()

    if g.is_finished:
        print(f"------> WINNER 👑: {g.winner}")
        break

    time.sleep(2)