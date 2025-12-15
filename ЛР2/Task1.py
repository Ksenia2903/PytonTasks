money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
money_capital += salary
while money_capital > spend:
    money_capital -= spend
    money_capital += salary
    months += 1
    spend = spend*(1+increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)
