import os
from sorters import sort_by_type
from sorters import sort_by_size
from sorters import sort_by_date_modified

def print_banner():
    # Prints a banner with the application name in ASCII art
    print("""
███████╗██╗██╗     ███████╗    ███████╗ ██████╗ ██████╗ ████████╗███████╗██████╗ 
██╔════╝██║██║     ██╔════╝    ██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
█████╗  ██║██║     █████╗      ███████╗██║   ██║██████╔╝   ██║   █████╗  ██████╔╝
██╔══╝  ██║██║     ██╔══╝      ╚════██║██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
██║     ██║███████╗███████╗    ███████║╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                    
    """)

def main_menu():
    # Display the main menu options to the user
    print("Welcome to File Sorter")
    print("Please choose an option:")
    print("1. Sort files by type")
    print("2. Sort files by size")
    print("3. Sort files by date modified")
    print("4. Exit")
    choice = input("Enter your choice (1, 2, 3, 4): ")
    return choice

def get_directory():
    # Prompt the user to enter a directory path to sort files, or 'exit' to terminate
    while True:
        directory = input("Enter the directory path to sort files or 'exit' to terminate: ")
        if directory.lower() == "exit":
            exit(1)
        elif os.path.isdir(directory):
            return directory
        else:
            print("Directory does not exist. Please enter a valid path.")

def main():
    # Main application logic
    print_banner()  # Display the application banner
    while True:
        user_choice = main_menu()
            
        if user_choice == '1':
            print("You chose to sort files by type.")
            directory = get_directory()
            sort_by_type(directory)  # Call sort_by_type function with the user-provided directory
        elif user_choice == '2':
            print("You chose to sort files by size.")
            directory = get_directory()
            sort_by_size(directory)  # Call sort_by_size function with the user-provided directory
        elif user_choice == '3':
            print("You chose to sort files by date modified.")
            directory = get_directory()
            sort_by_date_modified(directory)  # Call sort_by_date_modified function with the user-provided directory
        elif user_choice == '4':
            print("Exiting the application. Goodbye!")
            break  # Exit the loop and terminate the application
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly