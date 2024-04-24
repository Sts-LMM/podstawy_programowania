def uno_revese(word_to_reverce):
    for i in range(len(word_to_reverce)):
        print(word_to_reverce[i], end = "")
    print("")

    for i in range(len(word_to_reverce)-1,-1,-1):
        print(word_to_reverce[i], end = "")
    print("")
    return 0  

spell_backwards = str(input("Enter the word and i will spell it backwards: "))
uno_revese(spell_backwards)