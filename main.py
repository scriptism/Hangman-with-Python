import random
print("Welcome to Hangman!")
words = ["hacker", "bounty", "python"]
secret_word = random.choice(words)
print(secret_word)
display_word = []
for letter in secret_word:
    display_word += "-"
print(display_word)

game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    print(display_word)

    if "-" not in display_word:
        print("Congratulations! You've guessed the word!")
        game_over = True

