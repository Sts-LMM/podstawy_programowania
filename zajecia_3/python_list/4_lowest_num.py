def lowest_num_taker(all_nums): 
    all_nums.sort()
    final =all_nums[0]
    return final


all_nums = []
while True:
    try:
        num_to_sum = int(input("Write num to get the lowest (enter letter to end list): "))
        all_nums.append(num_to_sum)
    except ValueError:
        break
print(all_nums)
print('Lowest num:', lowest_num_taker(all_nums))