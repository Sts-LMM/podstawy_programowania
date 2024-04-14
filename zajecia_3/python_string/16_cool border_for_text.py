def putting_in(border,sentence):
    x=len(border)//2
    final = border[:x] + sentence + border[x:]

    return final

border = ' '
while len(border)%2 == 1: # Check if the length is odd
    border = input("Write a border (odd length) : ")
sentence = input("Write a sentence: ")
print(putting_in(border,sentence))