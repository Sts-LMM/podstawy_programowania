def first_last_five(all_nums):
    final = []
    final.append(all_nums[:5])
    final.append(all_nums[-5:])
    final2 = []
    for sublist in final:
        for num in sublist:
            final2.append(num ** 2)
    return final2

all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
print(all_nums)
print('squares list:', first_last_five(all_nums))
