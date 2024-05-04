def sort_num_list(test_list):
    for i in range(len(test_list)):
        test_list[i] = int(test_list[i])
    test_list.sort()
    return test_list

test_list = input("Enter list of nums separated by spaces: ").split()
sorted_list = sort_num_list(test_list)

print("Sorted list:", sorted_list)
