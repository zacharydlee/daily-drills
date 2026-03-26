"""A basic CLI menu that prints options, takes user inputs 

and begins the selected games. 
"""
from __future__ import annotations

# ================
# Project Imports
# ================

from numbers_guessing_game import play_number_game
from rock_paper_scissors import play_rps

# ==================
# Menu & Game Start
# ==================

def main() -> None:
    while True:

        print("==========  Game Selection ==========")
        print("1.) Guess My Number")
        print("2.) Rock, Paper, Scissors")
        print("3.) Quit")

        choice = input("Please Select a Game!\n> ").lower().strip()

        if choice in ["1", "guess my number"]:
            play_number_game()
        elif choice in ["2", "rock, paper, scissors"]:
            play_rps()
        elif choice in ["3", "quit", "exit"]:
            print("Thanks for stopping by! See you later!")
            break
        else:
            print("Sorry, that is not a valid choice! Please select a game listed above!")

# run it!

if __name__ == "__main__":
    main()
