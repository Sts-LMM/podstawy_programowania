
def remove_slash_n(sentence):
    without_slash_n = sentence.rstrip('\n')
    return without_slash_n

sentence = 'sentance with\n'
print(sentence)
print("Outcome: ", remove_slash_n(sentence))
