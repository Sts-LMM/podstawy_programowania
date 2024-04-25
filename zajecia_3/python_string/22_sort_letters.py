
def sort_letters(sentence):
    word_list = list(sentence) # changing string into list
    word_list.sort()            # sorting list
    sorted_string = ''.join(word_list)  #appending letters from list into string
    return sorted_string
sentence = input("Write a sentence : ")
print("Outcome: ", sort_letters(sentence))
