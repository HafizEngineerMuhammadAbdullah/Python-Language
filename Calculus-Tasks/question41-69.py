from sympy import symbols, ln, sqrt, diff, limit, Symbol, Function, Eq, exp, cos, sin, atan
from sympy.abc import x, y, z, u, v, w, r, theta

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

# ===== PROBLEM SOLUTIONS =====

# --- Problem 41 ---
f_41 = ln(x + sqrt(x**2 + y**2))
print_problem(41, "partial derivative", f_41,
             derivatives={"∂f/∂x": diff(f_41, x)},
             evaluations={"∂f/∂x at (3,4)": diff(f_41, x).subs({x:3, y:4}).simplify()})

# --- Problem 43 ---
f_43 = y/(x + y + z)
print_problem(43, "partial derivative", f_43,
             derivatives={"∂f/∂y": diff(f_43, y)},
             evaluations={"∂f/∂y at (2,1,-1)": diff(f_43, y).subs({x:2, y:1, z:-1}).simplify()})

# --- Problem 45 ---
h = Symbol('h')
f_45 = x*y**2 - x**2*y
print_problem(45, "limit definition of partial derivatives", f_45,
             derivatives={
                 "∂f/∂x (limit)": limit((f_45.subs(x, x+h) - f_45)/h, h, 0),
                 "∂f/∂y (limit)": limit((f_45.subs(y, y+h) - f_45)/h, h, 0)
             })

# --- Problem 47 ---
z_func = Function('z')(x, y)
eq_47 = Eq(x**2 + 2*y**2 + 3*z_func**2, 1)
print_problem(47, "implicit differentiation", eq_47,
             derivatives={
                 "∂z/∂x": (-diff(eq_47.lhs, x)/diff(eq_47.lhs, z_func)).simplify(),
                 "∂z/∂y": (-diff(eq_47.lhs, y)/diff(eq_47.lhs, z_func)).simplify()
             })

# --- Problem 49 ---
eq_49 = Eq(exp(z_func), x*y*z_func)
print_problem(49, "implicit differentiation", eq_49,
             derivatives={
                 "∂z/∂x": (y*z_func/(exp(z_func) - x*y)).simplify(),
                 "∂z/∂y": (x*z_func/(exp(z_func) - x*y)).simplify()
             })

# --- Problem 51 ---
print("\n" + "="*50)
print("PROBLEM 51: CHAIN RULE APPLICATIONS")
print("="*50)

# Part (a)
z_51a = Function('f')(x) + Function('g')(y)
print_problem("51a", "chain rule application", z_51a,
             derivatives={
                 "∂z/∂x": diff(z_51a, x),
                 "∂z/∂y": diff(z_51a, y)
             })

# Part (c)
z_51c = Function('f')(x/y)
print_problem("51c", "chain rule application", z_51c,
             derivatives={
                 "∂z/∂x": diff(z_51c, x),
                 "∂z/∂y": diff(z_51c, y)
             })

# --- Problem 53 ---
f_53 = x**3*y**2 + 2*x**4*y
print_problem(53, "second partial derivatives", f_53,
             derivatives={
                 "∂²f/∂x²": diff(f_53, x, 2),
                 "∂²f/∂y²": diff(f_53, y, 2),
                 "∂²f/∂x∂y": diff(diff(f_53, x), y)
             },
             checks={"Clairaut's theorem": diff(diff(f_53, x), y) == diff(diff(f_53, y), x)})

# --- Problem 55 ---
w_55 = sqrt(u**2 + v**2)
print_problem(55, "second partial derivatives", w_55,
             derivatives={
                 "∂²w/∂u²": diff(w_55, u, 2).simplify(),
                 "∂²w/∂v²": diff(w_55, v, 2).simplify(),
                 "∂²w/∂u∂v": diff(diff(w_55, u), v).simplify()
             })

# --- Problem 57 ---
z_57 = atan((x + y)/(1 - x*y))
print_problem(57, "second partial derivatives", z_57,
             derivatives={
                 "∂²z/∂x²": diff(z_57, x, 2).simplify(),
                 "∂²z/∂y²": diff(z_57, y, 2).simplify(),
                 "∂²z/∂x∂y": diff(diff(z_57, x), y).simplify()
             })

# --- Problem 59 ---
u_59 = x**4*y**3 - y**4
print_problem(59, "clairaut's theorem verification", u_59,
             derivatives={
                 "∂u/∂x": diff(u_59, x),
                 "∂u/∂y": diff(u_59, y)
             },
             checks={"u_xy == u_yx": diff(u_59, x, y) == diff(u_59, y, x)})

# --- Problem 61 ---
u_61 = cos(x**2*y)
print_problem(61, "clairaut's theorem verification", u_61,
             derivatives={
                 "∂u/∂x": diff(u_61, x),
                 "∂u/∂y": diff(u_61, y)
             },
             checks={"u_xy == u_yx": diff(u_61, x, y) == diff(u_61, y, x)})

# --- Problem 63 ---
f_63 = x**4*y**2 - x**3*y
print_problem(63, "third order derivatives", f_63,
             derivatives={
                 "∂³f/∂x³": diff(f_63, x, 3),
                 "∂³f/∂y∂x∂y": diff(f_63, y, x, y)
             })

# --- Problem 65 ---
f_65 = x**4*y**3 - x**3*y
print_problem(65, "second partial derivatives", f_65,
             derivatives={
                 "∂²f/∂x²": diff(f_65, x, 2),
                 "∂²f/∂y²": diff(f_65, y, 2)
             },
             checks={"Clairaut's theorem": diff(diff(f_65, x), y) == diff(diff(f_65, y), x)})

# --- Problem 67 ---
u_67 = exp(r)*sin(theta)
print_problem(67, "third order derivative", u_67,
             derivatives={"∂³u/∂r²∂θ": diff(u_67, r, 2, theta)})

# --- Problem 69 ---
w_69 = x/(y + 2*z)
print_problem(69, "third order mixed partials", w_69,
             derivatives={
                 "∂³w/∂x∂y∂z": diff(w_69, x, y, z),
                 "∂³w/∂x∂z∂y": diff(w_69, x, z, y)
             },
             checks={"Equality": diff(w_69, x, y, z) == diff(w_69, x, z, y)})