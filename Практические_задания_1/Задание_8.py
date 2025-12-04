list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

# TODO найти сумму, количество и среднее арифметическое уникальных чисел

set_num = set(list_)
sum_set_num = sum(set_num)
len_set_num = len(set_num)
middle_set_num = round((sum_set_num / len_set_num), 5)

direct = {"Сумма уникальных чисел:": sum_set_num,
          "Количество уникальных чисел:": len_set_num,
          "Среднее арифметическое уникальных чисел:": middle_set_num
          }

print(direct)