import requests


def get_word():
    url = "https://random-word-api.herokuapp.com/word?length=5"

    response = requests.get(url)
    return "".join(response.json())


def check_word():
    while True:
        word = input("Enter the word: ").lower()
        if requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").status_code == 200:
            return word
        print("Invalid word")
