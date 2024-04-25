
def check_if_starts_with(sentence):
    if(sentence.startswith("w3r")):
        return("starts with : w3r")
    elif(sentence.startswith("www")):
        return("starts with : www")
    elif(sentence.startswith("Polska")):
        return("starts with : Polska")
    elif(sentence.startswith("Math")):
        return("starts with : Math")
    else:
        return("starts with : ",sentence[:3])

sentence = input('type something: ')
print(sentence)
print("Outcome: ", check_if_starts_with(sentence))
