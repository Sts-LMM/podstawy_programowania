def multiplied_dictionary(dictionary_1):
     multiplied = 1
     for x in dictionary_1:
          multiplied = dictionary_1[x] * multiplied
     return multiplied

dictionary_1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
print(dictionary_1)
print("Final value: ", multiplied_dictionary(dictionary_1))
