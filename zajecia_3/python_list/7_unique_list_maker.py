def unique(all_nums): 
    lenght_of_list = len(all_nums)
    unique_words = []
    for i in range (0, lenght_of_list):
        if  all_nums[i] not in unique_words:
            unique_words.append(all_nums[i])
    return unique_words




code_list = ['bob', 'nooo', 'pope', 'popo', 'ballet', 'toot', 'popo', 'ballet', 'toot', 'police']
print(code_list)
print('That many words matched the :', unique(code_list))