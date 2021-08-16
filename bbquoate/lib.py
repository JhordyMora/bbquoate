import requests

def get_bbquote():

    result = requests.get("https://breaking-bad-quotes.herokuapp.com/v1/quotes").json()
    return f'{result[0]["quote"]} \n {result[0]["author"]}'

if __name__ == "__main__":
    print(get_bbquote())
