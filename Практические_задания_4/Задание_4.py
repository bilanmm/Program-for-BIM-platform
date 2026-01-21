import json

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def task() -> None:
  # TODO Десериализуйте содержимое файла из переменной INPUT_FILE
    with open (INPUT_FILE, "r", encoding = "utf-8") as input_file:
        json_str = json.load(input_file)
    with open (OUTPUT_FILE, "w", encoding = "utf-8") as input_file:
        json.dump(json_str, input_file, indent = 4, ensure_ascii = False)

 # TODO Сериализуйте содержимое в файл из переменной INPUT_FILE


if __name__ == '__main__':
    # Нужно для проверки задания
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
