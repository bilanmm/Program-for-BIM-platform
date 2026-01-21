# TODO импортировать необходимые молули
  # TODO считать содержимое csv файла
  # TODO Сериализовать в файл с отступами равными 4

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)


        data = list(csv_reader)


    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

with open(OUTPUT_FILENAME) as output_f:
    for line in output_f:
        print(line, end="")