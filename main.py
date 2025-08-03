import words

word = words.get_word()

guessedWord = ['_']*len(word)

attempts = 10

while attempts > 0:

    print("\nCurrent word "+"".join(guessedWord))

    while True:
        guess = input("Your guess; ").lower()
        if words.check_word(guess):
            break
        else:
            print("Enter a real word")

    list_word = set(guess)

    if any(letter in word for letter in list_word):
        for letter in list_word:
            if letter in word:
                indices = []
                for index, value in enumerate(word):
                    if value == letter:
                        guessedWord[index] = letter
        print('Good guess')
        attempts -= 1
        print("Attempts left: " + attempts)

    if '_' not in guessedWord:
        print("\nCongratulations!! You guessed the word: " + word)
        break

    if attempts == 0 and '_' in guessedWord:
        print('Sorry you failed to guess the word:' + word)
        break
