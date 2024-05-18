from sympy import *
from sympy import symbols, solveset, S, Eq

def count_solutions():
    """Count the number of distinct solutions for the equation| | x-1 | -2 | = m/100"""
    x, m = symbols('x m')
    equation = Eq(abs(abs(x - 1) - 2), m/100)
    solutions = solveset(equation, x, domain=S.Reals)
    return len(solutions)

# Iterate through possible values of m from 1 to 100
solutions_count = [count_solutions() for m in range(1, 101)]

# Find the values of m for which the equation has 4 distinct solutions
values_of_m = [m for m, count in enumerate(solutions_count, 1) if count == 4]

print(values_of_m)
