def reverse(all_nums): 
    return all_nums[::-1]

text = str(input("Type to get reverse: "))

print("Your text:", text)
print("Changed text:", reverse(text))