try:
    f = open("demo.txt", "r")
    data = f.read()
    print(data)
    print(type(data))
    f.close()  # Always close the file
except FileNotFoundError:
    print("Error: The file 'demo.txt' does not exist in this directory.")
