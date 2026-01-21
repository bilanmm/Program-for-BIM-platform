import json


FILENAME = "input.json"


def task() -> dict:
  with open (FILENAME, encoding="utf-8") as input_f:
    data = json.load(input_f)
    return max(data, key=lambda item : item ["score"] )

    ...  # TODO считать содержимое JSON файла

    ...  # TODO найти максимальный элемент по ключу score


if __name__ == '__main__':
    print(task())
