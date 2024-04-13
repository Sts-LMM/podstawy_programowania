def swapper(first_sentance,seckond_sentance): 
   
   final_word = seckond_sentance[:2] + first_sentance[2:] + ' ' + first_sentance[:2] + seckond_sentance[2:] 

   return (final_word)


first_sentance = input("Write first sentance to swap with seckond: ")
seckond_sentance = input("Write seckond sentance to swap with first: ")
print(swapper(first_sentance,seckond_sentance))