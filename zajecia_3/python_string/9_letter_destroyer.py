def cut_the_word(sentence, number):
    result = sentence[:number-1] + sentence[number:]

    return result

sentence = input("Write a sentance: ")

number = 0
while number <= 0:
    number = int(input("Write what letter you want to deleate (greater than 0): "))


print("Your word: ", sentence)
print("Your shortend word: ", cut_the_word(sentence,number))