import json


FILENAME = "input.json"


def task() -> int:
    with open (FILENAME, "r", encoding="utf-8") as input_f:
        data = json.load(input_f)

    list_val = [item["contains_improvement_appeals"]for item in data]
    return sum(list_val)
  # TODO Десериализуйте содержимое JSON файла



if __name__ == '__main__':
    print(task())
