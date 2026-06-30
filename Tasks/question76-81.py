from sympy import symbols, ln, exp, sqrt, diff, Function, simplify, cos, sin, sinh, cosh

# Define symbolic variables
x, y, z = symbols('x y z')

# ===== Problem 81 =====
print("\n" + "="*50)
print("PROBLEM 81: Verify solution of differential equations")
print("="*50)

# Define the function
z_81 = ln(exp(x) + exp(y))

# First derivatives
z_x = diff(z_81, x)
z_y = diff(z_81, y)

# Verify first equation
eq1 = z_x + z_y
print(f"\nFunction: z = {z_81}")
print(f"\n∂z/∂x + ∂z/∂y = {eq1.simplify()}")
print(f"Verification of first equation: {simplify(eq1) == 1}")

# Second derivatives
z_xx = diff(z_81, x, 2)
z_yy = diff(z_81, y, 2)
z_xy = diff(z_81, x, y)

# Verify second equation
eq2 = z_xx * z_yy - z_xy**2
print(f"\n∂²z/∂x² = {z_xx}")
print(f"∂²z/∂y² = {z_yy}")
print(f"∂²z/∂x∂y = {z_xy}")
print(f"\n(∂²z/∂x²)(∂²z/∂y²) - (∂²z/∂x∂y)² = {eq2.simplify()}")
print(f"Verification of second equation: {simplify(eq2) == 0}")

# ===== Problem 76 =====
print("\n" + "="*50)
print("PROBLEM 76: Solutions of Laplace's equation u_xx + u_yy = 0")
print("="*50)

# Define all functions
functions_76 = {
    "(a) u = x² + y²": x**2 + y**2,
    "(b) u = x² - y²": x**2 - y**2,
    "(c) u = x³ + 3xy²": x**3 + 3*x*y**2,
    "(d) u = ln(√(x²+y²))": ln(sqrt(x**2 + y**2)),
    "(e) u = sin(x)cosh(y) + cos(x)sinh(y)": sin(x)*cosh(y) + cos(x)*sinh(y),
    "(f) u = e⁻ˣcos(y) - e⁻ʸcos(x)": exp(-x)*cos(y) - exp(-y)*cos(x)
}

# Check each function
for desc, func in functions_76.items():
    u_xx = diff(func, x, 2)
    u_yy = diff(func, y, 2)
    laplace = u_xx + u_yy
    print(f"\n{desc}")
    print(f"u_xx = {u_xx}")
    print(f"u_yy = {u_yy}")
    print(f"u_xx + u_yy = {laplace.simplify()}")
    print(f"Is solution? {simplify(laplace) == 0}")

# ===== Problem 77 =====
print("\n" + "="*50)
print("PROBLEM 77: 3D Laplace equation solution")
print("="*50)

# Define the function
u_77 = 1/sqrt(x**2 + y**2 + z**2)

# Calculate second derivatives
u_xx = diff(u_77, x, 2)
u_yy = diff(u_77, y, 2)
u_zz = diff(u_77, z, 2)

# Verify 3D Laplace equation
laplace_3d = u_xx + u_yy + u_zz
print(f"\nFunction: u = {u_77}")
print(f"\nu_xx = {u_xx.simplify()}")
print(f"u_yy = {u_yy.simplify()}")
print(f"u_zz = {u_zz.simplify()}")
print(f"\nu_xx + u_yy + u_zz = {laplace_3d.simplify()}")
print(f"Is solution? {simplify(laplace_3d) == 0}")