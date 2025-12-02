#!/usr/bin/env python3
import random
import os

# ------------------------------------------------------------------
#  CONFIGURATION
# ------------------------------------------------------------------
WORDS = ["hacker", "bounty", "python"]
MAX_TRIES = 6

# ------------------------------------------------------------------
#  ASCII HANGMAN PICS
# ------------------------------------------------------------------
HANGMAN_PICS = [
    """
  +---+
      |
      |
      |
     ===""",
    """
  +---+
  O   |
      |
      |
     ===""",
    """
  +---+
  O   |
  |   |
      |
     ===""",
    """
  +---+
  O   |
 /|   |
      |
     ===""",
    """
  +---+
  O   |
 /|\\  |
      |
     ===""",
    """
  +---+
  O   |
 /|\\  |
 /    |
     ===""",
    """
  +---+
  O   |
 /|\\  |
 / \\  |
     ===""",
]

# ------------------------------------------------------------------
#  GAME LOGIC
# ------------------------------------------------------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_guess(guessed_set):
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
        elif guess in guessed_set:
            print("You already guessed that letter.")
        else:
            return guess

def play_round():
    secret = random.choice(WORDS)
    display = ["-"] * len(secret)
    guessed = set()
    misses = 0

    while misses < MAX_TRIES:
        clear_screen()
        print(HANGMAN_PICS[misses])
        print("Word:  ", " ".join(display))
        print("Misses:", ", ".join(sorted(guessed - set(secret)))

        if "-" not in display:
            print("\n🎉 Congratulations! You guessed the word!")
            return True

        guess = get_guess(guessed)
        guessed.add(guess)

        if guess in secret:
            for idx, ch in enumerate(secret):
                if ch == guess:
                    display[idx] = guess
        else:
            misses += 1

    # Out of tries
    clear_screen()
    print(HANGMAN_PICS[misses])
    print("Word:  ", " ".join(display))
    print("\n💀 Game over! The word was:", secret)
    return False

# ------------------------------------------------------------------
#  MAIN LOOP
# ------------------------------------------------------------------
def main():
    print("Welcome to Hangman!")
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()  