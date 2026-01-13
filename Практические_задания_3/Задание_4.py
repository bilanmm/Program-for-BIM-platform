# TODO Напишите функцию `calculate_parking_load`
def calculate_parking_load(total_parking_spaces, occupied_parking_spaces):
    load_parking = (occupied_parking_spaces / total_parking_spaces) * 100
    return round(load_parking)
total_spaces = 100
occupied_spaces = 50
results = calculate_parking_load(total_spaces, occupied_spaces)
print(f"Парковка загружена на: {results:}%")