def words_counter(sentence):
    dictionary = {}
    words = sentence.split()
    for word in words:
        word = word.strip('.,!?"').lower()
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

sentence_to_count = input("Write a sentence to count the words: ")
print(words_counter(sentence_to_count))
