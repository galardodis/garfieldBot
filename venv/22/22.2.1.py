piece = 0
q = 0
p = 0

while 16 != piece:
    q += 1
    piece += 2

piece = 0

while piece != 16:
    p += 1
    piece += 1

print(f'Количество разрезов по диаметру = {q}')
print(f'Количество разрезов от центра = {p}')
print(f'Отношение p/q = {p/q}')
