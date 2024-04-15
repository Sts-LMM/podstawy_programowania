def multiplied_list(list): 
    if len(list) == 0:
        return "is empty"
    else:
        return "isn't empty"


code_list = ['bob', 'nooo', 'pope', 'pepe', 'ballet', 'toot', 'pepe', 'ballet', 'toot', 'police']
print(code_list)
print('Your list ', multiplied_list(code_list))