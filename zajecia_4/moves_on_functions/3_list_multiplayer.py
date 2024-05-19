def multiply(all_nums): 
    final = 1
    for i in range(len(all_nums)):
            final = final* all_nums[i]
    return final


all_nums = []
while True:
    try:
        num_to_sum = int(input("Write num to sum (enter letter to end list): "))
        all_nums.append(num_to_sum)
    except ValueError:
        break

print(all_nums)
print("Sum:", multiply(all_nums))