
def reverse_if_four(sentence):
    final = ''
    if len(sentence) % 4 == 0:
        for i in range (len(sentence)-1, 0, -1):
            final += sentence[i]
    else:
        final = sentence

    return final

sentence = input("Write a sentence : ")
print("Outcome:" + reverse_if_four(sentence))
