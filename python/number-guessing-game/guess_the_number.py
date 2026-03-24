"""
A number guessing game!

Game Setup:
- Get random number
- Get user player input
- define player guess limit
- track number of player guesses

Game Loop:
- Loop to ask repeated guesses
- Break loop on correct guess
- Print: 'too high' / 'too low' / 'correct'
- ask to continue

Replay / Exit
- Break loop when guess limit reached
- Clean game over or game exit
"""

from __future__ import annotations

# =========================
# Standard Library Imports
# =========================

import random

# ==================
# Helper functions:
#===================

def _prompt_play() -> str:
    """Ask the player if they wish to play. Return a string of 'yes' or 'no'"""

    print("""Welcome to Guess My Digit.

I will think of a number, and you will have to guess it, within five attempts.
          
Do you want to play?
""")
    
    while True:
        player_answer = input("> ").lower().strip()

        if player_answer == "yes":
            return player_answer
        elif player_answer == "no":
            return player_answer
        else:
            print("Sorry! That is not a valid input. I am going to need a 'yes' or a 'no' from you.")

def _get_difficulty() -> str:
    """Prompt user for difficulty input
    
    Valid input are 'easy', 'standard', 'hard', or 'nightmare'. Reprompt until valid input is given.

    Returns:
        str: A valid difficulty level.
    """
    print("""That's the spirit! There are four modes. Please choose wisely!

Easy: I think of a number between 1 and 10.
          
Standard: I think of a number between 1 and 25.
          
Hard: I think of a number between 1 and 50.
          
Nightmare: I think of a number between 1 and 100.        
""")
    while True:
        valid_difficulty = input ("Please choose your desired difficulty experience: Easy, Standard, Hard, or Nightmare:\n> ").lower().strip()

        if valid_difficulty in ["easy", "standard", "hard", "nightmare"]:
            return valid_difficulty
        else:
            print("I am sorry. That is not a valid difficulty selection. Please choose between: Easy, Standard, Hard, or Nightmare.")

def _map_difficulty_range(valid_difficulty) -> tuple[int, int]:
    """Takes a valid difficulty and returns tuple containing the minimum and maximum values."""

    if valid_difficulty == "easy":
        return (1, 10)
    elif valid_difficulty == "standard":
        return (1, 25)
    elif valid_difficulty == "hard":
        return (1, 50)
    elif valid_difficulty == "nightmare":
        return (1, 100)
    # unreachable if input is valid
    else:
        raise ValueError(f"{valid_difficulty} is an invalid difficulty.")
    
def _get_random_number (min_value, max_value) -> int:
    """Generates a random integer between the given minimum and maximum values."""

    return random.randint(min_value, max_value)

def _prompt_play_again() -> str:
    print("Would you like to play again?")

    while True:
        continue_play = input("Yes or No?\n> ").lower().strip()

        if continue_play == "yes":
            return continue_play
        elif continue_play == "no":
            return continue_play
        else:
            print("Sorry! I need a 'yes' or 'no' on this one!")

# ===================
# Main Gameplay Loop
# ===================

def number_guessing_loop(min_value, max_value) -> None:
    """Runs the main gameplay loop
    
    Generates a target number, processes player guesses, provides feedback, and tracks the number of attempts.
    """

    target_number = _get_random_number(min_value, max_value)
    guess_count = 0
    max_attempts = 5

    while True:
        player_guess = input("Give me a number! Let's see if it's the one I am thinking of.\n> ")
        try:
            player_guess = int(player_guess)
        except ValueError:
            print("Sorry, that is not a valid response! Gonna need a number from you")
            continue

        guess_count += 1

        if player_guess == target_number:
            print("Congratulations! That is the number I was thinking of. Are you psychic!?")
            return
        
        if guess_count >= max_attempts:
            print(f"Darn! Out of attempts. The number was {target_number}")
            return
        
        if player_guess > target_number:
            print("Oof! Not quite. Too high! Give it another Go!")
        else:
            print("Gah! Too low. Try again!")

# ==============
# Main Function
# ==============

def main() -> None:
    """Prepare the game setup and start the gameplay loop."""
    
    while True:
        player_choice = _prompt_play()

        if player_choice == "no":
            print("I understand. Please come back if you change your mind! I'll be here!")
            return
    
        if player_choice == "yes":
            difficulty = _get_difficulty()
            min_value, max_value = _map_difficulty_range(difficulty)
        
            number_guessing_loop(min_value, max_value)

        play_again = _prompt_play_again()

        if play_again == "no":
            print("Thanks for playing. I hope we can do it again soon!")
            return
        
if __name__ == "__main__":
    main()
