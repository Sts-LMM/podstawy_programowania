def shotcut(sentance): 
   shortcut = sentance[:2]+sentance[-2:]
   return shortcut


sentance_to_count = input("Write a sentance to shorten: ")
print(shotcut(sentance_to_count))