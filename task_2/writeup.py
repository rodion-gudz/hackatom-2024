from bs4 import BeautifulSoup
import requests
import sympy as sp


def solve_numerically(equation_str):
    x = sp.symbols('x')
    try:
        lhs, rhs = equation_str.split('=')
        lhs = sp.sympify(lhs.strip())
        rhs = sp.sympify(rhs.strip())

        equation = sp.Eq(lhs, rhs)

        solutions = sp.solve(equation, x)

        if not solutions:
            solution_numerical = sp.nsolve(equation, x)
            return [solution_numerical]
        return solutions
    except Exception as e:
        return [f"Ошибка: {e}"]


roots = []
z = requests.get('http://127.0.0.1:6969').text
soup = BeautifulSoup(z, 'html.parser')
hidden_input = soup.find('input', {'type': 'hidden', 'name': 'equation_index'})
equation_index = hidden_input['value'] if hidden_input else None
root = solve_numerically(soup.find('p').text)[0]
roots.append(root)
requests.post('http://127.0.0.1:6969', {'equation_index': equation_index, 'user_answer': root})

while True:
    try:
        z = requests.get('http://127.0.0.1:6969/').text
        soup = BeautifulSoup(z, 'html.parser')
        hidden_input = soup.find('input', {'type': 'hidden', 'name': 'equation_index'})
        equation_index = hidden_input['value'] if hidden_input else None
        root = solve_numerically(soup.find('p').text)
        root = root[0]
        print(root)
        roots.append(root)
        requests.post('http://127.0.0.1:6969', {'equation_index': equation_index, 'user_answer': root})
    except:
        print(z)
        break
print(roots)
def hex_to_ascii(hex_list):
    ascii_string = ''.join([chr(int(h, 16)) for h in hex_list])
    return ascii_string
hex_solves = []
for i in roots:
    hex_solves.append(hex(int(i))[2:].upper())
print(hex_to_ascii(hex_solves))
