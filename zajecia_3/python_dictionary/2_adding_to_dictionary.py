def add_to_dictionary(d,addon):
    d.update({len(d):int(addon)})
    print(d)
    return True
d = {0: 0, 1: 2, 2: 1,3: 4, 4: 3}
	
print('Original dictionary:', d)
addon = input("Add number:")

if(add_to_dictionary(d,addon)):
    print('Number added!')
else:
    print('Something bad happened!')
print(d)