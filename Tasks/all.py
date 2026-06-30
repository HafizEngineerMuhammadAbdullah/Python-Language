# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import sympy as sp
from sympy import symbols, ln, sqrt, diff, limit, Symbol, Function, Eq, exp, cos, sin, atan, sinh, cosh, log, solve

# ======================================================
# Section 1: Odd Problems (13–27)
# ======================================================
x, y, t, r, theta, p, q, u, v = sp.symbols('x y t r theta p q u v')
a, b, c, d = sp.symbols('a b c d')

results = []

# Problem 13
f13 = x**2 * y**3
results.append(("13: f = x^2 y^3", sp.diff(f13, x), sp.diff(f13, y)))

# Problem 15
f15 = y**5 - 3*x*y
results.append(("15: f = y^5 - 3xy", sp.diff(f15, x), sp.diff(f15, y)))

# Problem 17
f17 = sp.exp(-t) * sp.cos(sp.pi * x)
results.append(("17: f(x,t) = e^{-t} cos(pi x)", sp.diff(f17, x), sp.diff(f17, t)))

# Problem 19
z19 = (2*x + 3*y)**10
results.append(("19: z = (2x+3y)^10", sp.diff(z19, x), sp.diff(z19, y)))

# Problem 21
f21 = x / y
results.append(("21: f = x/y", sp.diff(f21, x), sp.diff(f21, y)))

# Problem 23
f23 = (a*x + b*y) / (c*x + d*y)
results.append(("23: f = (a x + b y)/(c x + d y)", sp.diff(f23, x), sp.diff(f23, y)))

# Problem 25
g25 = (u**2 * v - v**3)**5
results.append(("25: g = (u^2 v - v^3)^5", sp.diff(g25, u), sp.diff(g25, v)))

# Problem 27
R27 = sp.atan(p * q**2)
results.append(("27: R(p,q) = arctan(p q^2)", sp.diff(R27, p), sp.diff(R27, q)))

for label, d1, d2 in results:
    print(label)
    print("  d/d(first var) =", sp.simplify(d1))
    print("  d/d(second var) =", sp.simplify(d2))
    print()

# ======================================================
# Section 2: Problems 31–37
# ======================================================
x, y, z, t, a, b, c, d = sp.symbols('x y z t a b c d')

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

# ======================================================
# Section 3: Problems 41–69
# ======================================================
def print_problem(problem_num, description, func, derivatives=None, evaluations=None, checks=None):
    """Print problem solution in a standardized format"""
    print(f"\n{'='*50}")
    print(f"PROBLEM {problem_num}: {description.upper()}")
    print(f"{'='*50}")
    print(f"\nFunction: {func}")
    
    if derivatives:
        print("\nDerivatives:")
        for name, deriv in derivatives.items():
            print(f"{name} = {deriv}")
    
    if evaluations:
        print("\nEvaluations:")
        for name, val in evaluations.items():
            print(f"{name} = {val}")
    
    if checks:
        print("\nVerifications:")
        for name, check in checks.items():
            print(f"{name}: {check}")

# Variables for this section
x, y, z, u, v, r, theta = symbols('x y z u v r theta')
z_func = Function('z')(x, y)
h = Symbol('h')

# Problem 41
f_41 = ln(x + sqrt(x**2 + y**2))
print_problem(41, "partial derivative", f_41,
             derivatives={"∂f/∂x": diff(f_41, x)},
             evaluations={"∂f/∂x at (3,4)": diff(f_41, x).subs({x:3, y:4}).simplify()})

# Problem 43
f_43 = y/(x + y + z)
print_problem(43, "partial derivative", f_43,
             derivatives={"∂f/∂y": diff(f_43, y)},
             evaluations={"∂f/∂y at (2,1,-1)": diff(f_43, y).subs({x:2, y:1, z:-1}).simplify()})

# Problem 45
f_45 = x*y**2 - x**2*y
print_problem(45, "limit definition", f_45,
             derivatives={
                 "∂f/∂x (limit)": limit((f_45.subs(x, x+h) - f_45)/h, h, 0),
                 "∂f/∂y (limit)": limit((f_45.subs(y, y+h) - f_45)/h, h, 0)
             })

# Problem 47
eq_47 = Eq(x**2 + 2*y**2 + 3*z_func**2, 1)
print_problem(47, "implicit differentiation", eq_47,
             derivatives={
                 "∂z/∂x": (-diff(eq_47.lhs, x)/diff(eq_47.lhs, z_func)).simplify(),
                 "∂z/∂y": (-diff(eq_47.lhs, y)/diff(eq_47.lhs, z_func)).simplify()
             })

# Problem 49
eq_49 = Eq(exp(z_func), x*y*z_func)
print_problem(49, "implicit differentiation", eq_49,
             derivatives={
                 "∂z/∂x": (y*z_func/(exp(z_func) - x*y)).simplify(),
                 "∂z/∂y": (x*z_func/(exp(z_func) - x*y)).simplify()
             })

# Problem 51a
z_51a = Function('f')(x) + Function('g')(y)
print_problem("51a", "chain rule", z_51a,
             derivatives={"∂z/∂x": diff(z_51a, x), "∂z/∂y": diff(z_51a, y)})

# Problem 51c
z_51c = Function('f')(x/y)
print_problem("51c", "chain rule", z_51c,
             derivatives={"∂z/∂x": diff(z_51c, x), "∂z/∂y": diff(z_51c, y)})

# Problem 53
f_53 = x**3*y**2 + 2*x**4*y
print_problem(53, "second derivatives", f_53,
             derivatives={"∂²f/∂x²": diff(f_53, x, 2),
                          "∂²f/∂y²": diff(f_53, y, 2),
                          "∂²f/∂x∂y": diff(diff(f_53, x), y)},
             checks={"Clairaut's theorem": diff(diff(f_53, x), y) == diff(diff(f_53, y), x)})

# Problem 55
w_55 = sqrt(u**2 + v**2)
print_problem(55, "second derivatives", w_55,
             derivatives={"∂²w/∂u²": diff(w_55, u, 2).simplify(),
                          "∂²w/∂v²": diff(w_55, v, 2).simplify(),
                          "∂²w/∂u∂v": diff(diff(w_55, u), v).simplify()})

# Problem 57
z_57 = atan((x + y)/(1 - x*y))
print_problem(57, "second derivatives", z_57,
             derivatives={"∂²z/∂x²": diff(z_57, x, 2).simplify(),
                          "∂²z/∂y²": diff(z_57, y, 2).simplify(),
                          "∂²z/∂x∂y": diff(diff(z_57, x), y).simplify()})

# Problem 59
u_59 = x**4*y**3 - y**4
print_problem(59, "Clairaut's theorem", u_59,
             derivatives={"∂u/∂x": diff(u_59, x), "∂u/∂y": diff(u_59, y)},
             checks={"u_xy == u_yx": diff(u_59, x, y) == diff(u_59, y, x)})

# ======================================================
# Section 4: Problems 76–81 (Laplace & verification)
# ======================================================
print("\n" + "="*50)
print("PROBLEM 76: Laplace equation solutions")
print("="*50)

x, y, z = symbols('x y z')
functions_76 = {
    "(a) u = x² + y²": x**2 + y**2,
    "(b) u = x² - y²": x**2 - y**2,
    "(c) u = x³ + 3xy²": x**3 + 3*x*y**2,
    "(d) u = ln(√(x²+y²))": ln(sqrt(x**2 + y**2)),
    "(e) u = sin(x)cosh(y) + cos(x)sinh(y)": sin(x)*cosh(y) + cos(x)*sinh(y),
    "(f) u = e⁻ˣcos(y) - e⁻ʸcos(x)": exp(-x)*cos(y) - exp(-y)*cos(x)
}
for desc, func in functions_76.items():
    print(f"\n{desc}")
    print("u_xx + u_yy =", (diff(func, x, 2) + diff(func, y, 2)).simplify())

# Problem 77 (3D Laplace)
u_77 = 1/sqrt(x**2 + y**2 + z**2)
laplace_3d = diff(u_77, x, 2) + diff(u_77, y, 2) + diff(u_77, z, 2)
print("\nProblem 77: Laplace in 3D:", laplace_3d.simplify())

# Problem 81
z_81 = ln(exp(x) + exp(y))
print("\nProblem 81: Verification")
print("∂z/∂x + ∂z/∂y =", (diff(z_81, x) + diff(z_81, y)).simplify())

# ======================================================
# Section 5: Problems 87–89 (Gas Law)
# ======================================================
P, V, T, n, m, k, R, a, b = symbols('P V T n m k R a b')

# Problem 87
print("\nProblem 87: Van der Waals")
vdw_eq = Eq((P + n**2*a/V**2) * (V - n*b), n*R*T)
P_vdw = solve(vdw_eq, P)[0]
print("P =", P_vdw)
print("dP/dV =", diff(P_vdw, V).simplify())
print("dP/dT =", diff(P_vdw, T).simplify())

# Problem 88
print("\nProblem 88: Ideal Gas Law")
ideal_gas_eq = Eq(P*V, m*R*T)
P_ideal = solve(ideal_gas_eq, P)[0]
V_ideal = solve(ideal_gas_eq, V)[0]
T_ideal = solve(ideal_gas_eq, T)[0]
product_88 = diff(V_ideal, P) * diff(P_ideal, T) * diff(T_ideal, V)
print("(dV/dP)*(dP/dT)*(dT/dV) =", product_88.simplify())

# Problem 89
print("\nProblem 89: Ideal Gas Law Verification")
dP_dT_89 = diff(P_ideal, T)
dV_dT_89 = diff(V_ideal, T)
product_89 = P * dV_dT_89 + V * dP_dT_89
print("P*(dV/dT) + V*(dP/dT) =", product_89.simplify())
