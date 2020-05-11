"""Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.
Anna Feferman"""

import timeit  # імпортуємо тайміт для перевірки часу виконання

while True:  # зациклюємо програму
    while True:  # зациклюємо перевірку
        try:
            x = int(input('Input number: '))
            break
        except(ValueError, TypeError):
            print('Wrong value!')

    # ітераційний метод знаходження числового кореня
    def dn_iter(n):
        x_str = str(n) # конвертуємо число в стрічку, щоб додавати по одній цифрі за раз
        while len(x_str) > 1:
            n = 0
            for i in x_str:
                n += int(i)
            x_str = str(n)

        return x_str

    # знаходимо суму рекурсивно
    def sum_rec(n):
        if 0 < n < 10:
            return n

        return n % 10 + dn_rec(n // 10)

    # функція, що повторює рекурсивну суму, щоб дійти до 1 кінцевої цифри
    def dn_rec(n):
        if n < 10:
            return n

        return dn_rec(sum_rec(n))

    # в 36 - 43 користувач обирає яким методом шукати корінь
    ans = input('Recursion method - 1\n'
                'Iteration method - anything else\n'
                '')
    if ans == '1':
        print(dn_rec(x))
    else:
        print(dn_iter(x))

    print('Program execution time is ', timeit.timeit(number=100000))  # час виконання програми

    repeat = input(
        'Input 1 if you want to continue. If you do not, input anything else: ')  # питаємо чи користувач
    if repeat == '1':  # хоче повторити програму
        continue
    else:
        break
