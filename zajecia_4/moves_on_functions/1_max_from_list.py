def max_out_of_list(all_nums): 
    max_num = all_nums[0]
    for i in range(len(all_nums)):
        if all_nums[i] > max_num:
            max_num = all_nums[i]
    return max_num


all_nums = []
while True:
    try:
        num_to_sum = int(input("Write num to return biggest num you wrote: (enter letter to end list): "))
        all_nums.append(num_to_sum)
    except ValueError:
        break

print(all_nums)
print("Highiest one:", max_out_of_list(all_nums))