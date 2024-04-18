def merging_dictionaries(dictionary_1,dictionary_2):
     dictionary_temporary = dictionary_1.copy()
     dictionary_temporary.update(dictionary_2)
     return dictionary_temporary

dictionary_1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
dictionary_2 = {8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
print(dictionary_1)
print(dictionary_2)
print("Merged dictionary: ",merging_dictionaries(dictionary_1,dictionary_2))
