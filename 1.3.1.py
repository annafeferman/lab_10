""""Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n.
Anna Feferman"""

import timeit  # імпортуємо тайміт для перевірки часу виконання

while True:  # зациклюємо програму
    while True:  # зациклюємо перевірку
        try:
            x = int(input('Input number: '))
            break
        except(ValueError, TypeError):
            print('Wrong value!')


    def factorial_rec(n):  # створюємо фукнцію, що використовує рекурсію для факторіалу
        if n == 0:
            return 1
        return n * factorial_rec(n - 1)


    def factorial_iter(n):  # функція, що знаходить факторіал ітеративно
        x_factorial = 1
        if x != 0 or x != 1:
            for i in range(1, x + 1):
                x_factorial *= i
        else:
            print('1')
        return x_factorial


    # в 29 - 35 користувач обирає яким методом шукати факторіал
    ans = input('Recursion method - 1\n'
                'Iteration method - anything else\n'
                '')
    if ans == '1':
        print(f'{x}! = {factorial_rec(x)}')
    else:
        print(f'{x}! = {factorial_iter(x)}')

    print('Program execution time is ', timeit.timeit(number=100000))  # час виконання програми

    repeat = input(
        'Input 1 if you want to continue. If you do not, input anything else: ')  # питаємо чи користувач
    if repeat == '1':  # хоче повторити програму
        continue
    else:
        break

# сравнить эффективность рекурсии и итеративного метода затруднительно без использования больших
# объемов данных. Для этого в програме запущено измерение скорости (В конце каждого выполнения),
# которое говорит о скорости. Что на счет реализации, это субъективно, но мне, за редким исключением,
# практически всегда проще прописать код циклом, а не рекурсией. К тому же, с итерациями не возникает
# таких проблем как StackOverFlow или слишком долгое выполнение кода, как, к примеру, в задании 1.3.3.