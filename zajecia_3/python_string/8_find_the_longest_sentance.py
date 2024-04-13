def find_longest_word(words_list):
    top = [0,'']
    for n in words_list:
        if len(n)>top[0]:
            top[0] = len(n)
            top[1] = n

    return(top[0],top[1])

result = find_longest_word(["PHP", "Exercises", "Backend"])

print("\nLongest word: ", result[1])
print("Length of the longest word: ", result[0])