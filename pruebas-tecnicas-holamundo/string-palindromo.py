# indica si un string es palindromo

# word = input("Introduce una palabra: ")


# def palindrome(word):
#     if word.isdigit():
#         return print("debes introducir una plabra")

#     else:
#         if word.lower().strip() == word[::-1].lower().strip():
#             return print("Es palíndromo")
#         else:
#             return print("No es palíndromo")


# palindrome(word)


word = input("Introduce una palabra: ")


def palindrome(word):
    if word.isdigit():
        return print("Debes introducir una palabra")
    else:
        word = word.lower().replace(" ", "")
        if word == word[::-1]:
            return print("Es palíndromo")
        else:
            return print("No es palíndromo")


palindrome(word)
