def multiplied_list(all_nums): 
    final = sorted(all_nums, key=lambda el: el[1])
    return final


all_nums = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(all_nums)
print('Highiest num:', multiplied_list(all_nums))