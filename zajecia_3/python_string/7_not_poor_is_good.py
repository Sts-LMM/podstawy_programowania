def if_good(sentence):
    where_not = sentence.find('not')
    
    where_poor = sentence.find('poor')

    if where_poor > where_not and where_not > 0 and where_poor > 0:
        sentence = sentence.replace(sentence[where_not:(where_poor+4)], 'good')
        return sentence
    else:
        return sentence

  
not_poor = input("Write a sentence to see what happens: ")
#print(if_good('The lyrics is not that poor!'))  test
#print(if_good('The lyrics is poor!'))           test
print(if_good(not_poor))       