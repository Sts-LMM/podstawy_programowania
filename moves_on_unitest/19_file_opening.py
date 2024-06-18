try:
    with open("filename.txt", "r", encoding="utf-8") as file:
        contents = file.read()
except UnicodeDecodeError:
    print("Error: Unicode decoding error occurred.")
