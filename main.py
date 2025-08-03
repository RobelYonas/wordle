import words


def similarity(word, guess):

    result = {}

    correct_letter = {(i, letter)
                      for i, (letter, correct) in enumerate(zip(guess, word))
                      if letter == correct}
    only_letter_correct = {letter for _, letter in correct_letter}
    misplaced_letter = (set(guess) & set(word)) - only_letter_correct
    mistake = set(word) - set(guess)

    result["correct"] = only_letter_correct
    result["misplaced"] = misplaced_letter
    result["wrong"] = mistake

    return result, correct_letter


def game_over(word):
    print(f"The word was {word}")


def main():

    valid_guess = 5
    word = words.get_word()
    guess_words = ['_' * len(word)]*5

    while valid_guess > 0:
        guess = words.check_word()

        for i in range(6):
            guess_words[i] = guess.upper()
            result, correct_word = similarity(guess, word)

        for index, letter in correct_word:
            guess_words[index] = letter
        print(guess_words)
        print(f"Misplaced: {result['misplaced']}, Wrong: {result['wrong']}")

        if guess == word:
            print("Correct answer")
            break

    game_over(word)


if __name__ == "__main__":
    main()
