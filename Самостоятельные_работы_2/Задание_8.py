list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменяйте местами значения согласно условию

index = 0
value = list_numbers[index]

for i,  new_list in enumerate(list_numbers):
    if  new_list >= value:
        value = new_list
        index = i
list_numbers[index], list_numbers[-1] = list_numbers[-1], list_numbers[index]
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
