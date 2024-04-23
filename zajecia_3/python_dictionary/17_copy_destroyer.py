def no_for_copies(dictionary):
    unique = {}
    for key, value in dictionary.items():
        if value not in unique.values():
            unique[key] = value
    return unique

dictionary_1 = {1: 1, 2: 4, 3: 49, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 16, 12: 144, 13: 169, 14: 255, 15: 225}
changed = no_for_copies(dictionary_1)
print (dictionary_1)
print (changed)