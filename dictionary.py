import json
from difflib import get_close_matches 


# read the data
data = json.load(open('data.json'))


# process user input, return result
def vocab(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = (input('Did you mean {} if YES enter Y, if NO enter N: '.format(get_close_matches(word, data.keys())[0]))).lower()
        if yn == 'y' or yn == 'yes':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'n' or yn == 'no':
            return 'The word you entered does not exist'
        else:
            return 'No selection...Try again!'
    else:
        return 'Word not in the dictionary, try again!'


# get input from user
user_input = input('Please enter a word: ')
outputs = vocab(user_input.lower())


if isinstance(outputs, list):
    for output in outputs:
        print(output)
else:
    print(outputs)



