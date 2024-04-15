def multiplied_list(code_list): 
    final = code_list[:]
    final.pop(5)
    final.pop(4)
    final.pop(0)
    return final


code_list = ['bob', 'no', 'pope', 'handmade', 'ballet', 'tootor', 'pizzeria', 'ballet', 'police']
print(code_list)

print('After slicing list: ', multiplied_list(code_list), )