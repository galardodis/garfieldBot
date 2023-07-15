goal = 16
piece = 0
p = 0
q = 0

while piece != goal:
    if piece == goal-1:
        piece += 1
        break
    if piece == 3 or piece % 4 == 3 or piece >= goal - 4:
            p += 1
            piece += 1
    else:
        p += 2
        piece += 1


piece = 0

while piece != goal:
    if not piece:
        q += 1
        piece += 2
    else:
        q += 1
        piece = piece + piece

print(f'Количество разрезов листочкам = {p}')
print(f'Количество разрезов складывая = {q}')
print(f'Отношение p/q = {p / q}')
