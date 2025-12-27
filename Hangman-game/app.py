import random

# Step 1: Predefined words
words = ["book", "laptop", "reading", "coding", "developer"]

# Step 2: Choose a random word
secret_word = random.choice(words)

# Step 3: Initialize variables
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

# Step 4: Game loop
while attempts > 0:
    display_word = ""

    # Show current word state
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        break

    # Take user input
    guess = input("Guess a letter: ").lower()

    # Validate guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

# Step 5: Game over
if attempts == 0:
    print("\n❌ Game Over! The word was:", secret_word)