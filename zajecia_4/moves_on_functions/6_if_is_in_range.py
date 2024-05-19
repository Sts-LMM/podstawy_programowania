def test_range(n,min,max):
    if n in range(min, max):
        print(f"{n} is in the range between {min} and {max}.")
    else:
        print("The number is outside the given range.")

num = int(input("Write num to know if it is in range: "))
range_min = int(input("Write min num: "))
range_max = int(input("Write max num: "))
test_range(num,range_min,range_max)
