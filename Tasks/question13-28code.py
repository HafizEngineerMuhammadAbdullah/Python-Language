# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
# save this as partials_odd_problems.py
import sympy as sp

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