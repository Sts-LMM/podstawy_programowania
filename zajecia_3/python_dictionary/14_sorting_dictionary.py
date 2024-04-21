def sort(color_dictionary):
    print("Dictionary sorted!")
    return dict(sorted(color_dictionary.items(), key=lambda x: x[1]))

color_dictionary = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'}
print("Original dictionary:")
print(color_dictionary)
sorted_dictionary = sort(color_dictionary)
print("Sorted dictionary:")
print(sorted_dictionary)
