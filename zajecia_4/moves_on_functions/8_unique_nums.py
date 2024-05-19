def unique_numbers(all_nums):
    final = []
    for num in all_nums:
        if num not in final:
            final.append(num)
    return final

all_nums = []
while True:
    try:
        num_to_add = int(input("Write num to return biggest num you wrote: (enter letter to end list): "))
        all_nums.append(num_to_add)
    except ValueError:
        break

print("All numbers:", all_nums)
print("Unique numbers:", unique_numbers(all_nums))
