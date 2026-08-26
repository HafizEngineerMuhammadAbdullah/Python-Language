import mymodule
import datetime

mymodule.greeting("Prof Abdullah")

# Exercise 1
# Perform the given operations
# I. a Python program to square and cube every number in a given list of integers using Lambda.
# The map() function applies a specific action to every item in an iterable. Here, lambda x: x ** 2 defines a quick, anonymous function that takes an input (x) and raises it to the power of 2 (x^2). Wrapping this inside list() converts the transformed map object back into a standard Python list.

# Define the original list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square every number using lambda and map
squared_numbers = list(map(lambda x: x**2, numbers))

# Cube every number using lambda and map
cubed_numbers = list(map(lambda x: x**3, numbers))

# Display the results
print("Original list of integers:")
print(numbers)

print("\nSquare every number of the said list:")
print(squared_numbers)

print("\nCube every number of the said list:")
print(cubed_numbers)


# II. a Python program to find if a given string starts with a given character using Lambda.

# Define a lambda function that takes two arguments: the string (s) and the target character (c)
starts_with = lambda s, c: s.startswith(c)

# Test cases
test_string = "Python"

# Example 1: True condition
char_to_check_1 = "P"
result_1 = starts_with(test_string, char_to_check_1)
print(f"Does '{test_string}' start with '{char_to_check_1}'? {result_1}")

# Example 2: False condition
char_to_check_2 = "p"  # Note: startswith() is case-sensitive
result_2 = starts_with(test_string, char_to_check_2)
print(f"Does '{test_string}' start with '{char_to_check_2}'? {result_2}")


# III. a Python program to extract year, month, date and time using Lambda.
# datetime.datetime.now(): Captures the exact current timestamp.dt.year / dt.month / dt.day: Standard attributes of a datetime object.dt.time(): A method that extracts just the hour, minute, second, and microsecond.Lambda Functions: Act as anonymous, single-line functions that take now as an argument and return the specific attribute.

# Get the current date and time
now = datetime.datetime.now()

# Define lambda functions for extraction
get_year = lambda dt: dt.year
get_month = lambda dt: dt.month
get_day = lambda dt: dt.day
get_time = lambda dt: dt.time()

# Extract and print the components
print(f"Original Datetime: {now}\n")
print(f"Year:  {get_year(now)}")
print(f"Month: {get_month(now)}")
print(f"Day:   {get_day(now)}")
print(f"Time:  {get_time(now)}")


# Exercise 2
# I.
# You have collected information about cities in your province. You decide to store each city’s
# name, population, and mayor in a file. Write a python program to accept the data for a number
# of cities from the keyboard and store the data in a file in the order in which they’re entered.


def store_cities_info():
    with open("cities_info.txt", "w") as f:
        f.write("Name\t\tPopulation\t\tMayor")

    number_of_cities = int(input("How many cities info you want to stored... "))

    for i in range(1, number_of_cities + 1):
        city_name = input(f"Please,Enter the city {i} Name:...")
        city_population = input(f"Please,Enter the population of {city_name} city :...")
        city_mayor = input(f"Kindly,Enter the Mayor Name of {city_name} :...")

        with open("cities_info.txt", "a") as file:
            file.write(f"\n{city_name}\t{city_population}\t{city_mayor}")


store_cities_info()



# File Handling: The with open(...) statement safely opens and closes the file automatically.Order Preservation: The write() method appends each city to the end of the file as soon as you type it, preserving your exact entry order.Flexibility: The while True loop allows you to enter as many cities as you want until you explicitly type exit.

def save_city_data():
    # Open the file in write mode ('w') to create a new file or overwrite existing data
    with open("cities_data.txt", "w") as file:
        print("--- Province City Data Entry ---")

        while True:
            # Get data from the keyboard
            name = input("\nEnter city name (or type 'exit' to quit): ").strip()
            if name.lower() == "exit":
                break

            population = input(f"Enter population for {name}: ").strip()
            mayor = input(f"Enter mayor name for {name}: ").strip()

            # Format the data string
            data_line = f"City: {name} | Population: {population} | Mayor: {mayor}\n"

            # Write the data to the file immediately to maintain entry order
            file.write(data_line)
            print(f"Successfully saved {name} to the file.")

    print("\nData entry complete. File 'cities_data.txt' has been saved.")


# Run the program
if __name__ == "__main__":
    save_city_data()

# II.
# Write a python program to create a data file student.txt and append the message “Now we are
# AI   students”s

with open("students.txt", "w") as f:
    f.write("Now we are AI students!")
