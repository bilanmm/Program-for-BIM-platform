# TODO реализовать функцию
def get_unique_words(num):
    words = list(set(num.split()))
    words.sort()
    return words

print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
