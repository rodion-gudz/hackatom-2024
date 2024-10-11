import sympy as sp

x = sp.symbols('x')

equations = open('equations.txt').readlines()


def solve_numerically(equation_str):
    try:
        lhs, rhs = equation_str.split('=')
        lhs = sp.sympify(lhs.strip())
        rhs = sp.sympify(rhs.strip())

        equation = sp.Eq(lhs, rhs)

        solutions = sp.solve(equation, x)

        if not solutions:
            solution_numerical = sp.nsolve(equation, x)
            return [solution_numerical]  # Возвращаем как список для согласованности
        return solutions
    except Exception as e:
        return [
            f"Ошибка: {e}. Перезапустите машинку и начните решать сначала) Не забудьте: ответы Вам нужно сдать учителю"]


for i, eq_str in enumerate(equations):
    solutions = solve_numerically(eq_str)

    print(solutions[0])
