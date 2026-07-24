import sympy as sp

# Define variables
x, y, z, t, a, b, c, d = sp.symbols('x y z t a b c d')

# List of (question_number, function, variables_to_diff)
questions = [
    (31, x*z - 5*x**2 * y**3 * z**4, (x, y, z)),
    (33, sp.log(x + 2*y + 3*z), (x, y, z)),
    (35, x*y * sp.asin(y*z), (x, y, z)),
    (37, x**2 * y * sp.cos(z/t), (x, y, z, t)),
]

for num, func, vars_ in questions:
    print(f"Problem {num}: f = {func}")
    for var in vars_:
        d = sp.diff(func, var)
        print(f"  d/d{var} = {sp.simplify(d)}")
    print()