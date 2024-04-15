def sum_list(all_nums): 
    final = sum(all_nums)
    return final


all_nums = []
while True:
    try:
        num_to_sum = int(input("Write num to sum (enter letter to end list): "))
        all_nums.append(num_to_sum)
    except ValueError:
        break

print(all_nums)
print("Sum:", sum_list(all_nums))