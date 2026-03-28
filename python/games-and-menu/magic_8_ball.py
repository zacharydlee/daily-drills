"""A program designed to respond to a user question, by chosing, at random, from a list of

predetermined responses. 
"""
from __future__ import annotations

# ================
# Library Imports
# ================

import random
import time

# =================
# Global Variables
# =================

ANSWERS = {
    1: "Yes - definitely",
    2: "It is decidedly so!",
    3: "Without a doubt.",
    4: "Reply hazy, try again...",
    5: "Ask again later.",
    6: "Better not tell you now!",
    7: "My sources say no",
    8: "Outlook not so good!",
    9: "Very doubtful.",
    10: "Not likely.",
    11: "I cannot address this. The question is morally repugnant.",
    12: "Indeed, but I cannot recommend it.",
    13: "Maybe, but do you really want this for yourself? What would Jesus say?",
    14: "No! It will not happen. Reality has spoken. God is displeased.",
    15: "Yes, but you are going to need a lot of soap and bleach. Your eyeballs will not clean themselves."
}

# =================
# Helper Functions
# =================

def _get_user_name() -> str:
    """Helpfer function gets the user's name, validatse input, and returns the name 

    as a string.    
    """

    while True:
        user_name = input("Hello there, stranger! What is your name?\n> ").strip()

        if user_name == "":
            return "Nameless One"
        else:
            return user_name
    
def _player_plays (name: str) -> str:
    """Helper function to ask the player if they would like to play, validates the input and returns the response.
    
    as a string.
    """

    while True:
        player_plays = input(f""" 
Hi there, {name}! Nice to meet you!
                             
I am Mike-8! I can answer any yes or no question you may have!

Would you like to ask me a question?
                        
> 
"""    
    ).lower().strip()
        
        if player_plays not in ["yes", "no"]:
            print(f"I apologize. I really need a 'yes' or a 'no' from you {name}")
        else:
            return player_plays
        
def _get_user_question(name: str) -> str:
    """Fuction to get the user's question, validate it, and return the string."""

    while True:
        user_question = input(f"Alright, {name}! Give me your question!\n> ").lower().strip()

        if user_question in ["", " ", ".", "?"]:
            print(f"{name}, You have to actually ask a question! Ask away!")
        else:
            return user_question
        
def _get_random_number() -> int:
    """Helper function to get a random number and return it."""

    return random.randint(1, 15)
        
def _give_user_answer(name: str, roll: int) -> str:
    """Helper function to grab an answer based on the random number it is given."""

    user_answer = ANSWERS.get(roll, f"{name}, I have no answer for this question!")
    return user_answer

# ===================
# Main Gameplay Loop
# ===================

def mike_8_ball() -> None:
    """Function resposible for the main gameplay loop."""

    name = _get_user_name()
    play = _player_plays(name)

    if play == "no":
        print(f"I understand {name}! Comeback anytime!")
        return
    
    # Game begins here
    while True:
        question = _get_user_question(name)
        roll = _get_random_number()
        answer = _give_user_answer(name, roll)

        print("Give me a moment to ponder!")
        time.sleep(1)
        print(f"""\nAh! {name}, you asked: {question}

Here is my answer:
""")
        print(answer)

        again = input(f"Good question! Would you like to ask something else, {name}?\n> ").lower().strip()

        if again != "yes":
            print(f"I understand. We can save your questions for another time, {name}. Goodbye!")
            break