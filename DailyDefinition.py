import requests
import json
from random_word import RandomWords
from termcolor import colored

# Declare api key and url w/ key inserted 
apiKey = "3c523796-be7a-43c0-801f-7d52cef2d9a0"

for i in range(1,5):
    r = RandomWords()
    randomWord = r.get_random_word(hasDictionaryDef = "true")
    url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}".format(randomWord, apiKey)
    
    # Send request to api
    apiRequest = requests.get(url).json()

    if len(apiRequest) == 1:
        break
    else:
        pass

    if i == 5:
        print("Timed out")

# Create dictionary from request
data = dict(apiRequest[0])

# Pull the wanted values from dictionary
word = data["meta"]["id"]
definition = data["shortdef"][0]
if word.isalnum():
    print(colored(word.capitalize(), 'yellow'), ":", colored(definition.capitalize(), 'green') + ".")
else:
    word = word.split(':', 1)
    print(colored(word[0].capitalize(), 'yellow'), ":", colored(definition.capitalize(), 'green') + ".")