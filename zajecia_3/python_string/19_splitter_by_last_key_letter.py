def cutted_sentence(letter_key, link):
   answear = link.rsplit(letter_key, 1)[0]
   return answear

link = 'https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-19.php'
print('Edytujesz ten link' + link)
letter_key = ""
while len(letter_key) != 1:
    letter_key= input("What last letter you want to deleate (ENTER 1 KEY): ")
print ("Outcome:" + cutted_sentence(letter_key, link))