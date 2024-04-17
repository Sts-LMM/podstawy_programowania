def if_exist(random_dictionary,is_it_there):
     if(random_dictionary.get(is_it_there) is not None):
          return(random_dictionary[is_it_there])
     else:
          return("Does not exist")

random_dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
is_it_there = int(input('Type num and ill print "definition":'))
print('Dictionary:',random_dictionary) 
print("The defiinition for num: ", is_it_there, "\n", if_exist(random_dictionary,is_it_there))