def open_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write("This is a test write operation.\n")
            print(f"Successfully wrote to the file: {filename}")
    except PermissionError:
        print("Error: Permission denied to open the file.")
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError as e:
        print(f"Error: {e}")

file_name = input("Input a file name: ")
open_file(file_name)
