"""Сформувати функцію для введення з клавіатури послідовності чисел і виведення
її на екран у зворотному порядку (завершаючий символ послідовності – крапка)
Anna Feferman"""

import timeit

while True:
    while True:
        try:
            array = [] # зазначаємо масив
            for i in range(int(input('Input lenght: ')) + 1): # користувач заповнює його поелементно
                array.append(input(f'Input {i+1} number: '))
            while array[-1] != '.': # перевіряємо чи є в кінці крапка
                for i in range(int(input('To end print a point. Input lenght: ')) + 1):
                    array.append(input(f'Input {i + 1} number: '))
            break
        except(ValueError, TypeError):
            print('Wrong values!')


    def vise_versa_iter(n):
        space = '' # створюємо строку, щоб заповнювати її елементами списку в оберненому порядку
        for el in array:
            if el != '.':
                space = el + space
            else:
                break
        return space

    def vise_versa_rec(n):
        if len(n) == 1:
            return n[0]
        else:
            return n[len(n) - 1] + vise_versa_rec(n[0:len(n) - 1]) # за допомогою індексів
        # перебираємо елементи в оберненому порядку


    # в 27 - 33 користувач обирає яким методом шукати корінь
    ans = input('Recursion method - 1\n'
                'Iteration method - anything else\n'
                '')
    if ans == '1':
        print(vise_versa_rec(array))
    else:
        print(vise_versa_iter(array))

    print('Program execution time is ', timeit.timeit(number=100000))  # час виконання програми

    repeat = input(
        'Input 1 if you want to continue. If you do not, input anything else: ')  # питаємо чи користувач
    if repeat == '1':  # хоче повторити програму
        continue
    else:
        break