import words
from rich.console import Console

console = Console(width=40)


def similarity(guesses, word):

    for guess in guesses:
        styled = []
        if "_" in guess:
            for _ in range(len(word)):
                styled.append("[white on #222222]_[/]")
        else:
            for letter, correct in zip(guess, word):
                if letter == correct:
                    style = "bold white on green"
                elif letter in word:
                    style = "bold white on yellow"
                else:
                    style = "white on #666666"
                styled.append(f"[{style}]{letter}[/]")

        console.print("".join(styled), justify="center")


def game_over(word):
    print(f"The word was {word}")


def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")


def main():

    word = words.get_word()
    guess_words = ['_' * len(word)]*5
    previous_words = []

    for i in range(5):
        refresh_page(headline=f"Guess {i + 1}")
        similarity(guess_words, word)
        guess = words.check_word(previous_words)
        previous_words.append(guess)
        guess_words[i] = guess
        if guess_words[i] == word:
            print("Correct answer")
            break
    game_over(word)


if __name__ == "__main__":
    main()
