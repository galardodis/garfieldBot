from math import factorial

ans = {}


def add_str():
    ans_str = ''
    for i in sorted(ans):
        if ans[i] == 1:
            ans_str += f'{i} '
        else:
            ans_str += f'{i}^{ans[i]} '
    return ans_str.rstrip().replace(' ', ' * ')


def decomp_1(n, m=2):
    if n < m:
        return
    if m == n:
        if m in ans.keys():
            ans[m] += 1
        else:
            ans[m] = 1
        return

    while n % m == 0:
        n = n // m
        if m in ans.keys():
            ans[m] += 1
        else:
            ans[m] = 1
    else:
        m += 1
        decomp_1(n, m)


def decomp(n):
    n = factorial(n)
    decomp_1(n)
    add_str()
    return add_str()


print(decomp(n=101))
