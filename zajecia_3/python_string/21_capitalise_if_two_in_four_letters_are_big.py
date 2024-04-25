
def capitalise_if_two_in_four_letters_are_big(sentence):
    counter = 0 
    for i in range(0,4,1):
        if(sentence[i] == sentence[i].upper()):
            counter = counter + 1
    if (counter >= 2):
        return sentence.upper()
    else:
        return sentence
sentence = input("Write a sentence : ")
print("Outcome: ", capitalise_if_two_in_four_letters_are_big(sentence))
