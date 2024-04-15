def multiplied_list(x,y,z): 
    array = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

    return(array)


a = int(input("Write num to get * shape build:"))
b = int(input("Write num to get * shape build:"))
c = int(input("Write num to get * shape build:"))
print(multiplied_list(a,b,c))