"""Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
Anna Feferman"""

from random import randint
import timeit

while True:  # зациклюємо програму
    while True:  # зациклюємо перевірку
        try:
            n = int(input('Input number: '))
            break
        except (ValueError, TypeError):
            print('Wrong value!')

    list_res = []  # порожній список заповнюємо в розмірі, що задав користувач
    for i in range(n):
        list_in = []
        for j in range(n):
            list_in.append(randint(0, 20))
        list_res.append(list_in)
    print(f'Your list: {list_res}')


    # обчислення індексу максимального елемента циклом
    def max_iter(list):
        row_idx = 0  # індекс елемента в рядку
        col_idx = 0  # індекс елемента в стовпці
        row = 0  # вказуємо нульовий рядок для початку перебору
        while row != len(list):
            col = 0  # нульовий стовпець для початку перебору
            while col != len(list[row]):
                if list[row][col] > list[row_idx][col_idx]:  # порівнюємо елементи
                    row_idx, col_idx = row, col
                col += 1
            row += 1
        return row_idx, col_idx

    def max_rec(list, col=0, row=0):
        row_idx = 0  # індекс елемента в рядку
        col_idx = 0  # індекс елемента в стовпці
        while row != len(list):
            while col != len(list[row]):
                if list[row][col] > list[row_idx][col_idx]:  # порівнюємо елементи
                    row_idx, col_idx = row, col
        return max_rec(list, col + 1, row + 1)


    # в 50 - 56 користувач обирає яким методом шукати індекс
    ans = input('Recursion method - 1\n'
                'Iteration method - anything else\n'
                '')
    if ans == '1':
        print(max_rec(list_res))
    else:
        print(max_iter(list_res))

    print('Program execution time is ', timeit.timeit(number=100000))  # час виконання програми

    repeat = input(
        'Input 1 if you want to continue. If you do not, input anything else: ')  # питаємо чи користувач
    if repeat == '1':  # хоче повторити програму
        continue
    else:
        break
