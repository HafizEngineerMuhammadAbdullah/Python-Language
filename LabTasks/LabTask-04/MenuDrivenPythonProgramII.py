def random_search_algo():
def open_list_search_algo():
def closed_list_search_algo():
def bfs_search_algo():
def dfs_search_algo():
def dijkstras_search_algo():




def main():
    while True:
        print("Menu Driven Python Program:")
        print("===============================")
        print("Which Searching Algorithm do you wanna choose :...")
        print("1. Random Search Algorithm")
        print("2. Closed List Search Algorithm")
        print("3. Open List Search Algorithm")
        print("4. Dijkstra's(Uniform Cost) Search Algorithm")
        print("5. Breadth First Search(BFS) Algorithm")
        print("6. Depth First Search(DFS) Algorithm")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            print("You selected Option 1.")
            # Add functionality for Option 1 here
        elif choice == '2':
            print("You selected Option 2.")
            # Add functionality for Option 2 here
        elif choice == '3':
            print("You selected Option 3.")
            # Add functionality for Option 2 here
        elif choice == '4':
            print("You selected Option 4.")
            # Add functionality for Option 2 here
        elif choice == '5':
            print("You selected Option 5.")
            # Add functionality for Option 5 here
        elif choice == '6':
            print("You selected Option 6.")
            # Add functionality for Option 6 here
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    # from MenuDrivenPythonProgramII import main
    main()


