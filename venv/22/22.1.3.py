from collections import Counter

alf = 'abcdefghijklmnopqrstuvwxyz'


def replace_duplicates(s):
    for i in s:
        if s.count(i) > 1:
            s = s.replace(s[s.index(i)], alf[(alf.index(s[s.index(i)]) + 1) % len(alf)], 1)
            s = s.replace(s[s.index(i)], '', 1)
            s = replace_duplicates(s)
            break
    return s


result_string = replace_duplicates('zxyphjtvyiikdo')
counter_obj = Counter(result_string)
sorted_obj = sorted(counter_obj.items())

print(sorted_obj)
