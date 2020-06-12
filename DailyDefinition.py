import requests
import json
from random_word import RandomWords
# Declare api key and url w/ key inserted 
apiKey = "3c523796-be7a-43c0-801f-7d52cef2d9a0"
r = RandomWords()
randomWord = r.get_random_word(hasDictionaryDef = "true")
url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}".format(randomWord, apiKey)

# Send request to api
apiRequest = requests.get(url).json()

# Create dictionary from request
data = dict(apiRequest[0])

# Pull the wanted values from dictionary
word = data["meta"]["id"]
definition = data["shortdef"][0]

print(word, " : ", definition)