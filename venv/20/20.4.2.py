file = input('Введите имя файла: ')
alf = 'abcdefghijklmnopqrstuvwxyz'
ans = dict()

with open(file + '.txt', 'r', encoding='utf8') as f:
    text = f.read().lower()

for i in text.split():
    if i[0] not in alf:
        continue
    if not i.isalpha():
        while not i[len(i) - 1] in alf:
            i = i[:len(i) - 1]
    if len(i) <= 3 or i in ans:
        continue
    else:
        ans[i] = text.count(i)

print(max(ans, key=ans.get))
print(max(ans.keys(), key=len))