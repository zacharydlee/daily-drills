"""Project File: Rock Paper Scissors

A simple CLI game. The user chooses Rock, Paper, or Scissors, and the computer selects a random choice. 

The program determines a winner based on the rulse of the game. 
"""
from __future__ import annotations

# =========================
# Standard Library Imports
# =========================

import random

# =================
# Helper Functions
# =================

CHOICES = ["rock", "paper", "scissors"] # global choices variable

def _player_plays() -> str:
    """Helper function that prompts player choice to play the game."""

    while True:
        play_game = input("Hey there! Up for a game of Rock, Paper, Scissors?\n> ").lower().strip()   

        if play_game not in ["yes", "no"]:
            print("Sorry! I didn't catch that. Do you want to play? Yes or No:\n> ")
        else:
            return play_game

def _get_player_choice() -> str: 
    """Helper function to get player's choice of either Rock, Paper, or Scissors"""

    while True:
        player_choice = input("Rock, Paper, or Scissors?\n> ").lower().strip()

        if player_choice not in CHOICES:
            print("Sorry! That is not a valid play response. Please choose: Rock, Paper, or Scissors")
        else:
            return player_choice
        
def _get_computer_choice() -> str:
    """Helper function to create the computer's choice from either Rock, Paper, or Scissors."""

    computer_choice = random.choice(CHOICES)
    return computer_choice


def _determine_winner(player: str, computer: str) -> str:
    """Helper function to compare the computer choice against the player choice, and determine a winner."""

    WINNING_MOVES = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if player == computer:
        return "tie"
    elif WINNING_MOVES[player] == computer:
        return "win"
    else:
        return "lose"
        
# ==============
# Main Function
# ==============

def play_rps() -> None:
    """Main gameplay loop. Determines if the player wishes to play, runs the loop and prompts if the player wishes to continue."""

    play_game = _player_plays()

    if play_game != "yes":
        print("I understand! Come back if you change your mind!")
        return
    
    # main gameplay loop starts here.
    while True:
        player = _get_player_choice()
        computer = _get_computer_choice()

        result = _determine_winner(player, computer)

        if result == "tie":
            print(f"It's a tie game! We both threw {computer}")
        elif result == "win":
            print(f"Bah! Your {player} beats my {computer} You win!")
        else:
            print(f"Yes! My {computer} beats your {player} I win!")

        play_again = input("That was a good game! Up for another round?\n >").lower().strip()
        
        if play_again != "yes":
            print("Thanks for playing! See you next time!")
            break
