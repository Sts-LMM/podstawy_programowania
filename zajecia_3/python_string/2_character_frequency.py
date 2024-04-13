def char_frequency(sentance): 
   dictionary = {}
   for n in sentance:
    keys = dictionary.keys()

    if n in keys:
        dictionary[n] += 1
    else:
        dictionary[n] = 1
   
   return dictionary

sentance_to_count = input("Write a sentance to cout letters: ")
print(char_frequency(sentance_to_count))