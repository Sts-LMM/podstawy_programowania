def print_alphabet_G():
    for i in range(7):
        for j in range(5):
            if ((j == 1 or j ==2 or j == 3) and (i != 0 and i != 3 and i != 6)) or ((i == 1 or i == 4 or i == 5) and (j > 0 and j < 4)) or ((i == 3) and (j == 1)) or ((i == 0 or i == 6) and (j == 0 or j == 4)) or (i == 2 and j == 4):
                print(" ", end="")
            else:
                print("*", end="")
        print()

# Print the alphabet pattern 'G'
print_alphabet_G()
