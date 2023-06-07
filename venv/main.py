per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

money = int(input())


for i in per_cent.values():
    deposit.append(int(i * money * 0.01))

print(deposit)

print('Максимальная сумма, которую вы можете заработать —', max(deposit))

