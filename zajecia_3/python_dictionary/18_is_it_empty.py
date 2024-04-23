
def is_it_empty(x):
    print(x)
    if not x:
        print("Dictionary is empty")
    else:
        print("Dictionary is not empty")
    return 0

dict ={}
dict_test={1:2,2:3}
is_it_empty(dict)
is_it_empty(dict_test)