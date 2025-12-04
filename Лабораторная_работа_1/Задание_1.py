numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

sum_numbers = sum(numbers[0:4]+numbers[5:20])
len_numbers = len(numbers)
middle_numbers = (sum_numbers / len_numbers)
numbers[4] = middle_numbers

print("Измененный список:", numbers)

