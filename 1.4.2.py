"""Сформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
себе).
Anna Feferman"""

import timeit  # імортуємо тайміт

while True:
    while True:
        try:
            n = int(input('Input number: ')) # користувач вводить число
            break
        except (ValueError, TypeError):
            print('Wrong value!')


    def smp_rec(n, min_dilnyk = 2):
        if n == min_dilnyk: # порівнюємо значення числа з характерними величинами
            return "Yes"
        elif n < 2 or n % min_dilnyk == 0: # порівнюємо значення числа з характерними величинами(2)
            return "No"
        return smp_rec(n, min_dilnyk + 1)

    def smp_iter(n, min_dilnyk = 2): # для ітеративного методу використовуємо
        # той самий алгоритм, що і для рекурсії, але не викликаємо функцію ще раз
        # а просто збільшуємо значення, з яким порівнюється стартове число
        if n == min_dilnyk:
            return "Yes"
        elif n < 2 or n % min_dilnyk == 0:
            return "No"
        min_dilnyk += 1
        return "Yes"

    # в 35 - 41 користувач обирає яким методом шукати корінь
    ans = input('Recursion method - 1\n'
                'Iteration method - anything else\n'
                '')
    if ans == '1':
        print(smp_rec(n))
    else:
        print(smp_iter(n))

    print('Program execution time is ', timeit.timeit(number=100000))  # час виконання програми

    repeat = input(
        'Input 1 if you want to continue. If you do not, input anything else: ')  # питаємо чи користувач
    if repeat == '1':  # хоче повторити програму
        continue
    else:
        break