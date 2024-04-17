def all_dictionary(random_dictionary):
     for dict_key, dict_value in random_dictionary.items(): # .items(): = dictionary -> list
          print(dict_key, '->', dict_value)	

random_dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
all_dictionary(random_dictionary)
