def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_even_numbers(sample_list)) 
