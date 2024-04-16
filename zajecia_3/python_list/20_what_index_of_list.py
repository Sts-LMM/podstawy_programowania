def list_nums(numbers):
    for i in range (0,len(numbers)):
        print("For index num:",i," number is:",numbers[i])
    return 0


numbers = [2, 3, 5, 6, 7, 11, 12 , 13, 17, 19, 45]
list_nums(numbers)