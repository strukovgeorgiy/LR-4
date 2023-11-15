# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """ Считываем содержимое csv файла"""
with open(INPUT_FILENAME, "r") as input_file:
    reader = csv.DictReader(input_file)
    data = [i for i in reader]

    """ Сериализация в файл с отступами равными 4"""
with open(OUTPUT_FILENAME, "w") as out_file:
    json.dump(data, out_file, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
