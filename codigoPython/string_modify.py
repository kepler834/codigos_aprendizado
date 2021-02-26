# Mariano Araújo Moura
# mariano.moura@ufpa.br

vowels = ("a","e","i","o","u","A","E","I","O","U")

def delete_vowels(text):
    text = list(text)
    for i in text:
        if i in vowels:
            text[text.index(i)] = ''
    return ''.join(text)

def insert_dot(text):
    text = list(text)
    return '.'.join(text)+"."

def lower_case(text):
    return text.lower()

string_input = input("insert a string: ")
string_input = delete_vowels(string_input)
string_input = insert_dot(string_input)
string_input = lower_case(string_input)
print(string_input)