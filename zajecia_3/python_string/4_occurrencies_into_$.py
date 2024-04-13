def into_dollar(sentence):
    get_dollared = ''
    dictionary = {}
    for char in sentence:
        if char in dictionary:
            dictionary[char] += 1
            get_dollared += "$"
        else:
            dictionary[char] = 1
            get_dollared += char
    return get_dollared

sentence_to_dollar = input("Write a sentence to censor '1<' used letters: ")
print(into_dollar(sentence_to_dollar))
