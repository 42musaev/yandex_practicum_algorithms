import re

word = str(input())


def palindrome(string: str) -> bool:
    string = re.sub(r'[^a-zA-Z0-9а-яА-Я]', '', string).lower()
    print(string == string[::-1])


palindrome(word)
