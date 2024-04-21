def min_and_max(num_dictionary):
    key_max = max(num_dictionary.keys(), key=(lambda k: num_dictionary[k]))
    key_min = min(num_dictionary.keys(), key=(lambda k: num_dictionary[k]))

    print('Maximum Value: ',num_dictionary[key_max])
    print('Minimum Value: ',num_dictionary[key_min])

num_dictionary = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
print("Original dictionary:")
print(num_dictionary)

min_and_max(num_dictionary)


