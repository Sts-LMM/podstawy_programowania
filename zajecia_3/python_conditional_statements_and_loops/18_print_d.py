def print_alphabet_D():
    for i in range(7):
        for j in range(5):
            if ((j == 1 or j ==2 or j == 3) and (i != 0 and i != 6)) or ((i>0 and i<6) and (j > 0 and j < 4)) or((i == 0 or i == 6) and (j == 4)):
                print(" ", end="")
            else:
                print("*", end="")
        print()

# Print the alphabet pattern 'D'
print_alphabet_D()
