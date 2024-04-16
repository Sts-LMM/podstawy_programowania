import itertools

def permutations(all_nums): 
    final = list(itertools.permutations(all_nums))
    return final


all_nums = []
while True:
    try:
        num_to_sum = int(input("Write num to make permutation of list made from those numbers (enter letter to end list): "))
        all_nums.append(num_to_sum)
    except ValueError:
        break
print(all_nums)
print('All possibilities:', permutations(all_nums))