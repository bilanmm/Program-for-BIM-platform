# TODO Напишите функцию `is_palindrome`

def is_palindrome(word):
    word_clear = ''.join(word.lower().split())
    return word_clear == word_clear[::-1]