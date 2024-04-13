def shotcut(sentance): 
   if len(sentance)>=2:
    shortcut = sentance[:2]+sentance[-2:]
    return shortcut
   else:
     return ("Sentance too short to create shortcut!")


sentance_to_count = input("Write a sentance to shorten: ")
print(shotcut(sentance_to_count))