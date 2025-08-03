import requests


def get_word():
    url = "https://random-word-api.herokuapp.com/word"

    response = requests.get(url)
    return "".join(response.json())


def check_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    response = requests.get(url)

    result = True if response.status_code == 200 else False

    return result