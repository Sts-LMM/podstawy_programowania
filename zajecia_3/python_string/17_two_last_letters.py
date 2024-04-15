def last_letters(sentence):
    final = ''
    for i in range(0,4):
        final += sentence[-2:]

    return final

sentence= input("Write a sentence: ")
print ("Outcome:" + last_letters(sentence))