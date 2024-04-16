def unique_number(list_1,list_2): 
    not_samezies = []
    if len(list_1) >len(list_2):
        longer = len(list_1)
        longer_list = list_1
        shorter = len(list_2)
        shorter_list = list_2
    else: 
        longer = len(list_2)
        longer_list = list_2
        shorter = len(list_1)
        shorter_list = list_1

    for i in range (0, longer):
        for j in range (0,shorter):
            if(shorter_list[j] == longer_list[i]):
                    break                 
        else:
            not_samezies.append(longer_list[i]) 
    return(not_samezies)



list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
list_2 = [18, 23, 3, 5, 20, 21, 15, 16, 24, 25, 13, 9, 11, 4, 1, 10, 17, 7, 12, 2, 14, 8, 6, 19, 22]

print(list_1,list_2)
print('Unique nums in list:', unique_number(list_1,list_2))