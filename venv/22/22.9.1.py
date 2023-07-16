import random


def qsort_random(array, left, right):
    p = random.choice(array[left:right])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def find(element, array):
    x = binary_search(array, element, 0, len(array) - 1)
    if array[0] < element <= array[len(array) - 1]:
        if element in array:
            print(f'Индекс меньшего элемента = {x - 1} индекс большего/самого элемента = {x}')
        else:
            while x is False:
                element -= 1
                x = binary_search(array, element, 0, len(array))
            print(f'Индекс меньшего элемента = {x} индекс большего/самого элемента = {x + 1}')
    elif element <= array[0]:
        print(f'Индекс меньшего элемента отсутствует, индекс большего/самого элемента = 0')
    else:
        print(f'Индекс меньшего элемента {len(array) - 1}, индекс большего/самого элемента отсутствует')


while True:
    try:
        array = [int(i) for i in input('Введите последовательность чисел через пробел: ').split()]
        while len(array) < 2:
            print('Некорректный ввод, минимальное количество введенных чисел через пробел - 2')
            array = [int(i) for i in input('Введите последовательность чисел через пробел: ').split()]
        element = int(input('Введите любое число: '))
    except ValueError:
        print('Некорректный ввод попробуйте еще раз')
    else:
        break

qsort_random(array, 0, len(array) - 1)
find(element, array)
