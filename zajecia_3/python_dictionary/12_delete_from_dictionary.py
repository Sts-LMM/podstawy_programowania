def to_delete_in_dictionary(test_dictionary,to_delete):
     if(to_delete in test_dictionary):
          test_dictionary.pop(to_delete)
          print("Valeue removed") 
     else:
          print("Wrong key! Valeue cannot be deleted")
     return 0

test_dictionary = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
to_delete = int(input("enter KEY valeue to delete: "))
print(test_dictionary)
to_delete_in_dictionary(test_dictionary,to_delete)
print(test_dictionary)

