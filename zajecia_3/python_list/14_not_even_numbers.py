def noteven(all_num):
    final = []
    for i in range(0,len(all_num)):
        if all_num[i]%2==1:
            final.append(all_num[i])
    return(final)

all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(all_nums)
print('Not even nums:', noteven(all_nums))