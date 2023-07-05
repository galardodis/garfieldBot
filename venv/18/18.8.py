def conference_cost():
    cost_min = 990
    cost_max = 1390
    total_prise = int()
    number_of_persons = int(input('Сколько вам нужно билетов? '))
    for i in range(number_of_persons):
        age = int(input(f'Сколько лет участнику №{i+1}? '))
        if age < 18:
            total_prise += 0
        elif 18 <= age < 25:
            total_prise += cost_min
        else:
            total_prise += cost_max
    if number_of_persons > 3:
        total_prise = total_prise - total_prise * 0.1
    return f'Итого к оплате {total_prise}р.'

print(conference_cost())