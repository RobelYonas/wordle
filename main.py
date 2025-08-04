import words
from rich.console import Console

console = Console(width=40)


def similarity(word, guess):

    for i in guess:
        styled = []

        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in correct:
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

    valid_guess = 5
    word = words.get_word()
    guess_words = ['_' * len(word)]*5

    while valid_guess > 0:
        i = 0
        refresh_page(headline="Guess")
        guess_words[i] = words.check_word()
        similarity(guess_words[i], word)
        if guess_words[i] == word:
            print("Correct answer")
            break
        ++i
    game_over(word)


if __name__ == "__main__":
    main()
