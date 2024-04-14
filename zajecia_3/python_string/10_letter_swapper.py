def letter_swapper(sentence):
    result = sentence[-1:] + sentence[1:-1]+ sentence[:1]

    return result

sentence = input("Write a sentance: ")

print("Your word: ", sentence)
print("Your swapped word: ", letter_swapper(sentence))