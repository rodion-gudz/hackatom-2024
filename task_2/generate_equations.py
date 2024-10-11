import random
import os


def mutmul(arr, dep):
    if dep == 1:
        return sum(arr)
    r = []
    for i in range(len(arr)):
        r.append(arr[i] * mutmul(arr[i + 1:], dep - 1))
    return sum(r)


def spow(v, p):
    if p == 0:
        return ""
    if p == 1:
        return v
    return v + '^' + str(p)


def polynom(roots):
    mroots = [-i for i in roots]
    coefs = [mutmul(mroots, i + 1) for i in range(len(mroots))]
    r = [spow("x", len(mroots))]
    for i, c in enumerate(coefs):
        s = str(c) + spow("x", len(coefs) - i - 1)
        r += [s]
    r = '+'.join(r)
    r = r.replace("+-", "-")
    return r


# Создаём директорию для сохранения изображений и файлов с уравнениями
if not os.path.exists('equations_png'):
    os.makedirs('equations_png')

# Создаём файл для записи уравнений
equations_text_file = open('equations_text.txt', 'w')


# Ваш список значений для создания уравнений
# answers = [104, 116, 116, 112, 115, 58, 47, 47, 119, 119, 119, 46, 121, 111, 117, 116, 117, 98, 101, 46, 99, 111, 109,
#            47, 119, 97, 116, 99, 104, 63, 118, 61, 100, 81, 119, 52, 119, 57, 87, 103, 88, 99, 81, 38, 97, 98, 95, 99,
#            104, 97, 110, 110, 101, 108, 61, 82, 105, 99, 107, 65, 115, 116, 108, 101, 121, 38, 38, 99, 116, 102, 95,
#            102, 111, 114, 95, 114, 111, 109, 97, 123, 107, 116, 111, 95, 112, 114, 111, 99, 104, 105, 116, 97, 108, 95,
#            116, 111, 116, 95, 115, 100, 111, 107, 104, 110, 101, 116, 125]

def ascii_to_decimal_roots(input_string):
    # Преобразуем каждый символ в строке в шестнадцатеричное значение
    hex_values = [hex(ord(char))[2:].upper() for char in input_string]

    # Преобразуем шестнадцатеричные значения в десятичные
    decimal_values = [int(h, 16) for h in hex_values]

    # Возвращаем список десятичных корней
    return decimal_values


answers = ascii_to_decimal_roots(
    'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley&&flag{HW_IS_DONE_AXAXAXAXAXAXAXAXAXA)}')

# Генерация уравнений
for z in range(len(answers)):
    roots = [answers[z] for i in range(random.randint(2, 5))]  # Случайное количество одинаковых корней
    equation = polynom(roots)
    equation = equation.replace('^', '**').replace('-', ' - ').replace('+', ' + ') + ' = 0'  # + str(answers[z])
    new_equation = ''
    for i in range(len(equation)):
        if equation[i] != 'x':
            new_equation += equation[i]
        else:
            if i != 0:
                new_equation += '*' + equation[i]
            else:
                new_equation += equation[i]
    equation = new_equation
    print(equation)
