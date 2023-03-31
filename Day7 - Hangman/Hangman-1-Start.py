import random
import Hangman_Art
import Hangman_Word

print(Hangman_Art.logo)



chosen_word = random.choice(Hangman_Word.word_list)
word_lenght = len(chosen_word)

lives = 6

display = []

for _ in range(word_lenght):
    display += "_"

print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(chosen_word)
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(Hangman_Art.stages[lives])
    print(guess)
