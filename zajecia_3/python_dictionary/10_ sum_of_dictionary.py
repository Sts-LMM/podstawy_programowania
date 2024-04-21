def sum_of_dictionary(dictionary_1):
     sum = 0
     for x in dictionary_1:
          sum += dictionary_1[x]
     return sum

dictionary_1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
print(dictionary_1)
print("Summary: ", sum_of_dictionary(dictionary_1))
