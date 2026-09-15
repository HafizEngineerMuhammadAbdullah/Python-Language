# Save this file as test_bug.py
def calculate_double(numbers):
    total = 0
    for num in numbers:
        # Intentional bug: adding the number instead of doubling it
        total += num * 2
    return total

my_list = [1, 2, 3]
result = calculate_double(my_list)
print(f"Result: {result}")
