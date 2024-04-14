def even(sentence):
    final = ''
    for i in range(0, len(sentence)):
        if i % 2 == 0:
            final = final + sentence[i]
    return final

to_shorten = input("Write a sentence to get back half of it: ")
print(even(to_shorten))
