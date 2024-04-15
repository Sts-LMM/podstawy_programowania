def multiplied_list(all_nums): 
    final = 1
    for i in range (0, len(all_nums)):
        final *= all_nums[i]
    return final


all_nums = []
while True:
    try:
        num_to_sum = int(input("Write num to multiply (enter letter to end list): "))
        all_nums.append(num_to_sum)
    except ValueError:
        break
print(all_nums)
print('Final:', multiplied_list(all_nums))