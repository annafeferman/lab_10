"""Сформувати функцію для переведення натурального числа з десяткової системи
числення у шістнадцятирічну.
Anna Feferman"""

import timeit

while True:
    while True:
        try:
            n = int(input('Input number: '))
            break
        except TypeError:
            print('Wrong value!')

    hex_symbols = '0123456789ABCDEF' # елементи, наявні в 16-річній системі числення

    # втілюємо рекурсивний алгоритм
    def hex_rec(n):
        n, key = n//16, hex_symbols[n % 16]
        if n:
            return hex_rec(n) + key
        return key

    # втілюємо ітеративний алгоритм
    def hex_iter(n):
        hex_str = ''
        if n == 0:
            return 0
        while n != 0:
            hex_str += hex_symbols[n % 16]
            n = n // 16
        return hex_str[::-1]

    # в 35 - 41 користувач обирає яким методом шукати корінь
    ans = input('Recursion method - 1\n'
                'Iteration method - anything else\n'
                '')
    if ans == '1':
        print(hex_rec(n))
    else:
        print(hex_iter(n))

    print('Program execution time is ', timeit.timeit(number=100000))  # час виконання програми

    repeat = input(
        'Input 1 if you want to continue. If you do not, input anything else: ')  # питаємо чи користувач
    if repeat == '1':  # хоче повторити програму
        continue
    else:
        break