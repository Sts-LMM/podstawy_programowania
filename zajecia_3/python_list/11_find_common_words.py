def multiplied_list(code_list, code_list_2): 
    final = 0
    for i in range (0,len(code_list)):
        for n in range (0,len(code_list_2)):
            if code_list[i] == code_list_2[n]:
                final += 1
    return final


code_list = ['bob', 'no', 'pope', 'handmade', 'ballet', 'tootor', 'pizzeria', 'ballet', 'police']
code_list_2 = ['bo', 'noo', 'pop', 'handmad', 'balle', 'tootor', 'pizzeri', 'balle', 'toothpast']
print(code_list)
print(code_list_2)
print('both lists have: ', multiplied_list(code_list, code_list_2), "common words.")