def printing_iterations(dictionary_1):
     for x, y in dictionary_1.items():
          print('For:',x,' -> ',y)
     return 0

dictionary_1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
print(dictionary_1)
printing_iterations(dictionary_1)
