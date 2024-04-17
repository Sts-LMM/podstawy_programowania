def the_power_of(random_dictionary):
     pow2 = {}
     for i in range (1,random_dictionary+1):
          pow2.update({i:(i*i)})
     print(pow2)
     return True

how_many_to_the_power_of_two = int(input("Enter a number: "))
the_power_of(how_many_to_the_power_of_two)
