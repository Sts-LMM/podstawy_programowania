def multiplied_list(list, longer_than): 
    final_list = []
    for i in range(0, len(list)):
        if len(list[i]) > longer_than:
            final_list.append(list[i])
    return final_list



code_list = ['bob', 'nooo', 'pope', 'handmade', 'ballet', 'tootor', 'pizzeria', 'ballet', 'toothpaste', 'police']
print('List of words: ', code_list)
longer_than = int(input("Write num to get words longer than that:"))

print('Your list of words longer than ', longer_than,": ", multiplied_list(code_list, longer_than))