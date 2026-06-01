import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row["letter"]:row["code"] for (index, row) in data.iterrows()}
user_input = input("Howdy detective. What is the secret message?")
uppercase = user_input.upper()
user_nato_name = [data_dict[letter] for letter in uppercase]
print(user_nato_name)