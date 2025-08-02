import words

word = words.get_word()

guessedWord = ['_']*len(word)

attempts = 10
word_used = set()

while attempts > 0:

    print("\nCurrent word "+"".join(guessedWord))
    print("Letters guessed: " + ", ".join(word_used))

    guess = input("Your guess; ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Good guess')
    else:
        attempts -= 1
        print("Wrong guess. Left attemps: " + str(attempts))

    word_used.add(guess)

    if '_' not in guessedWord:
        print("\nCongratulations!! You guessed the word: " + word)
        break

    if attempts == 0 and '_' in guessedWord:
        print('Sorry you failed to guess the word:' + word)
        break
