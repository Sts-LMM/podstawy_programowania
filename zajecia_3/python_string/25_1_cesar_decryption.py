
def cesar_decrypt(sentence, shifting):
    cryptText = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for current_letter in sentence:
        if current_letter in uppercase:
            index = uppercase.index(current_letter)
            crypting = (index - shifting) % 26
            cryptText.append(uppercase[crypting])
        elif current_letter in lowercase:
            index = lowercase.index(current_letter)
            crypting = (index - shifting) % 26
            cryptText.append(lowercase[crypting])
        else:
            cryptText.append(current_letter)
    print_string = ''.join(map(str, cryptText))



    return print_string
            

sentence = input('type something: ')
print(sentence)
print("Outcome: ", cesar_decrypt(sentence, 2))
