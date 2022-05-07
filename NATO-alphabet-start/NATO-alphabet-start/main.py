import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

name = input('enter your name ').upper()

d = {}

for letter in name:
    d[letter] = df[df['letter'] == letter]['code']

print(d)