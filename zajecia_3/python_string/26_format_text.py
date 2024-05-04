import textwrap
def cesar_decrypt(sentence, width_num):
    return textwrap.fill(sentence, width=width_num)    
    
    
            
sentence = input('Type something: ')
width = int(input('Type num: '))
print(sentence)
print("Outcome: ", cesar_decrypt(sentence, width))
