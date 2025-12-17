salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов



total_spend = 0
current_spend = spend

for month in range(months):
    if month == 0:
        total_spend += current_spend
    else:
        total_spend += current_spend
        current_spend *= (1 + increase)

total_salary = salary * months

money_capital = total_spend - total_salary

money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital} руб.")
