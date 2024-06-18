def open_file(filename):
    encoding = input("Input the encoding (ASCII, UTF-16, UTF-8) for the file: ").strip()

    try:
        with open(filename, 'r', encoding=encoding) as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except UnicodeDecodeError:
        print("Error: Encoding issue occurred while reading the file.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid encoding. Please choose from 'ASCII', 'UTF-16', or 'UTF-8'.")

file_name = input("Input the file name: ").strip()
open_file(file_name)
