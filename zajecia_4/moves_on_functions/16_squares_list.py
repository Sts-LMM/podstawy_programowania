def squares_list(x):
    squares = [i**2 for i in range(1, x)]
    return(squares)

# Example
print(squares_list(int(input("Write num to return biggest num you wrote: "))))

