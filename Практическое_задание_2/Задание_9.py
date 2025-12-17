# Список словарей со студентами и их оценками
students = [
    {"name": "Маша", "grade": 4},
    {"name": "Петя", "grade": 3},
    {"name": "Саша", "grade": 5},
    {"name": "Кирилл", "grade": 2},
    {"name": "Оля", "grade": 4},
]

# TODO Распечатать имена студентов с оценками выше тройки

for stud in students:
    if stud["grade"] > 3:
        print(f"{stud["name"]}. Оценка: {stud["grade"]}")
