def multiplied_list(all_nums): 
    all_nums.sort()
    final =all_nums[-1]
    return final


all_nums = []
while True:
    try:
        num_to_sum = int(input("Write num to get the largest (enter letter to end list): "))
        all_nums.append(num_to_sum)
    except ValueError:
        break
print(all_nums)
print('Highiest num:', multiplied_list(all_nums))