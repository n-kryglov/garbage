
def reverse(text):
    return text [::-1]

def is_palindrome(text):
    return text == reverse(text)

A = str.lower(input('Введите текст: '))
something = ''.join([a for a in A if a.isalpha()])

if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")