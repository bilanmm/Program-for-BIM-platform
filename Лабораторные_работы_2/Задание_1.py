from calendar import month

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов



money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
capital = money_capital
month = 0

while capital + salary >= spend:
    month += 1
    capital = capital + salary - spend
    if month > 1:
        spend = spend * (1 + increase)
print("Количество месяцев, которое можно протянуть без долгов:", month)
