
def star_print(awnser):
    for i in range(awnser):
        for j in range(i):
            print('*',end="")
        print("")

    for i in range(awnser,0,-1):
        for j in range(i):
            print('*',end="")
        print("")

how_many_stars = int(input("Enter the valeue: "))
star_print(how_many_stars)