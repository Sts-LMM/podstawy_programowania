def code(sentence):
    word = ''
    if len(sentence) >= 3:
      if sentence[-3:] == 'ing':
         word = sentence + "ly"
      else:
         word = sentence + "ing"
      return word
    else:
       return("Sentence is too short")

adding_ing_or_ly = input("Write a sentence to see what happens: ")
print(code(adding_ing_or_ly))