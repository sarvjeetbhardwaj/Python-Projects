import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#converting to dictionary
data_dictionary={}
for letter,code in zip(data.letter,data.code):
    data_dictionary[letter]=code

#creating the code word

is_string=False

while not is_string:
    name=input('Enter your name :\n').upper()
    try:
        for letters in name:
            if letters not in data_dictionary.keys():
                raise Exception
    except:
        print('All values should be strings')
    else:
        for letter in name:
            for k in data_dictionary.keys():
                if letter == k:
                    print(data_dictionary[letter])
        is_string=True















