def into_dictionary(test_keys,test_values):
     print("Two lists mapped into dictionary")
     return dict(zip(test_keys, test_values))

test_keys = ['red', 'green', 'blue']
test_values = ['#FF0000', '#008000', '#0000FF']
color_dictionary= (into_dictionary(test_keys,test_values))
print(color_dictionary)
