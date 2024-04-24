def nums_seperator(tuple_to_check):
    odd_num  = 0
    even_num = 0
    for i in range(len(tuple_to_check)):
        if (tuple_to_check[i] % 2 == 0):    #is it even?
            even_num = even_num + 1         # it is? add to even counter
        else:                               # it isn't?
            odd_num = odd_num + 1           # add to odd counter
    print("Odd nums: ",odd_num)
    print("Even nums: ",even_num)

all_the_nums = (1,2,3,4,5,6,7,8,9,0,12,13,15,17,25,76,23,74,94,72,56,38)
nums_seperator(all_the_nums)