import os
from sorters.sort_by_type import sort_by_type
from sorters.sort_by_size import sort_by_size
from sorters.sort_by_date_modifed import sort_by_date_modified

def print_banner():
    print("""
███████╗██╗██╗     ███████╗    ███████╗ ██████╗ ██████╗ ████████╗███████╗██████╗ 
██╔════╝██║██║     ██╔════╝    ██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
█████╗  ██║██║     █████╗      ███████╗██║   ██║██████╔╝   ██║   █████╗  ██████╔╝
██╔══╝  ██║██║     ██╔══╝      ╚════██║██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
██║     ██║███████╗███████╗    ███████║╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                    
    """)

def main_menu():
    print("Welcome to File Sorter")
    print("Please choose an option:")
    print("1. Sort files by type")
    print("2. Sort files by size")
    print("3. Sort files by date modified")
    print("4. Exit")
    choice = input("Enter your choice (1, 2, 3, 4): ")
    return choice

def get_directory():
    while True:
        directory = input("Enter the directory path to sort files or exit to terminate: ")
        if directory == "exit":
            exit(1)
        elif os.path.isdir(directory):
            return directory
        else:
            print("Directory does not exist. Please enter a valid path.")

def main():
    print_banner()
    while True:
        user_choice = main_menu()
            
        if user_choice == '1':
            print("You chose to sort files by type.")
            directory = get_directory()
            sort_by_type(directory)
        elif user_choice == '2':
            print("You chose to sort files by size.")
            directory = get_directory()
            sort_by_size(directory)
        elif user_choice == '3':
            print("You chose to sort files by date modified.")
            directory = get_directory()
            sort_by_date_modified(directory)
        elif user_choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()