# TODO Напишите функцию calculate_average_age для расчета среднего возраста студентов

def calculate_average_age(students_dict):
    student = students_dict.values()
    student_all = sum(student) / len(student)
    return student_all

students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}


print(f"Средний возраст студентов: {calculate_average_age(students_dict)}")  # TODO Распечатайте средний возраст студентов
