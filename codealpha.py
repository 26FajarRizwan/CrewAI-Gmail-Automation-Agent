"""
╔══════════════════════════════════════════════════════╗
║         HANGMAN GAME — CodeAlpha Internship          ║
║         Task 1 | Python Programming                  ║
╚══════════════════════════════════════════════════════╝
"""

import random

# ─── Predefined word list (5 words) ───────────────────
WORDS = ["python", "hangman", "laptop", "jungle", "matrix"]

# ─── Hangman ASCII art stages (0 = safe, 6 = dead) ───
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def display_state(word, guessed_letters, wrong_count):
    """Print current game state to console."""
    print(HANGMAN_STAGES[wrong_count])

    # Show word with blanks
    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )
    print(f"  Word: {display_word}")
    print(f"  Wrong guesses left: {6 - wrong_count}")

    # Show incorrect letters guessed so far
    wrong_letters = [l for l in guessed_letters if l not in word]
    if wrong_letters:
        print(f"  Incorrect letters: {', '.join(sorted(wrong_letters))}")
    print()


def get_player_guess(guessed_letters):
    """Prompt the player for a valid, new single letter."""
    while True:
        guess = input("  Enter a letter: ").strip().lower()

        if len(guess) != 1:
            print("  ⚠  Please enter exactly ONE letter.")
        elif not guess.isalpha():
            print("  ⚠  Letters only — no numbers or symbols.")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
        else:
            return guess


def play_hangman():
    """Main game loop."""
    print("\n" + "=" * 50)
    print("      Welcome to HANGMAN — CodeAlpha Edition")
    print("=" * 50)

    # Pick a random word
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_count = 0
    max_wrong = 6

    print(f"\n  A secret word has been chosen ({len(word)} letters).")
    print("  Guess it one letter at a time. You have 6 chances.\n")

    # ─── Game loop ────────────────────────────────────
    while wrong_count < max_wrong:
        display_state(word, guessed_letters, wrong_count)

        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"  ✅  Nice! '{guess}' is in the word.\n")
        else:
            wrong_count += 1
            remaining = max_wrong - wrong_count
            print(f"  ❌  '{guess}' is NOT in the word. {remaining} chance(s) left.\n")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            display_state(word, guessed_letters, wrong_count)
            print("=" * 50)
            print(f"  🎉  YOU WON!  The word was: '{word.upper()}'")
            print("=" * 50 + "\n")
            return

    # ─── Lose condition ───────────────────────────────
    print(HANGMAN_STAGES[max_wrong])
    print("=" * 50)
    print(f"  💀  GAME OVER!  The word was: '{word.upper()}'")
    print("=" * 50 + "\n")


def main():
    """Entry point — supports replay."""
    while True:
        play_hangman()
        again = input("  Play again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Thanks for playing! — CodeAlpha Internship\n")
            break


if __name__ == "__main__":
    main()