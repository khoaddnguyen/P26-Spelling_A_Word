# 1. Create dictionary in format of: {"A" : "Apple", "B": "Bento"}
# 2. Create a list of the phonetic code words from a word that the user inputs

# HINTS:
# {new_key:new_value for (index, row) in df.iterrows()}
# data_frame.to_dict()

import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

# 1. Create dictionary in format of: {"A" : "Apple", "B": "Bento"}

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# 2. Create a list of the phonetic code words from a word that the user inputs

def generate_phonetic():
    word = input("Enter a name: ").upper()
    try:
        phonetic_outputs = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please input only letters in the alphabet.")
        generate_phonetic()  # repeat error message as needed
    else:
        print(phonetic_outputs)

generate_phonetic()
