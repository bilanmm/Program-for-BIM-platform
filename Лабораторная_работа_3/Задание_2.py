# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):

    participants_1 = group1.split(separator)
    participants_2 = group2.split(separator)

    common = set(participants_1).intersection(set(participants_2))

    return sorted(list(common))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_1 = "Иванов,Петров,Сидоров"
participants_2 = "Петров,Сидоров,Смирнов"
print(find_common_participants(participants_1, participants_2))