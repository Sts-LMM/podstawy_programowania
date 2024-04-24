def print_alphabet_E():
    for i in range(7):
        for j in range(5):
            if ((j == 1 or j ==2 or j == 3 or j == 4) and (i != 0 and i != 3 and i != 6)) or ((j == 7) and (i != 0 or i != 6)) or((i == 3) and (j == 4)):
                print(" ", end="")
            else:
                print("*", end="")
        print()

# Print the alphabet pattern 'E'
print_alphabet_E()
