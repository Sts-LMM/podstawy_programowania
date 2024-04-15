def biggest_num_taker(code_list): 
    words_counter = 0
    for i in range (0, len(code_list)):
        if (len(code_list[i]) >= 2 and code_list[i][0] == code_list[i][-1]):
            words_counter += 1
    return words_counter


code_list = ['bob', 'nooo', 'pope', 'popo', 'ballet', 'toot']
print(code_list)
print('That many words matched the :', biggest_num_taker(code_list))