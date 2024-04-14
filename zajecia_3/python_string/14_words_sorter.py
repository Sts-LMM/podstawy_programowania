def sorting(sentence):
    dictionary = [word for word in sentence.split(',')]
    
    return (",".join(sorted(list(set(dictionary)))))

words_to_sort = input("Write words seperated by ',' that needs to be sorted: ")
print(sorting(words_to_sort))
