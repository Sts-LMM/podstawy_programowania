def count_case_characters(s):
    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

# Sample usage
sample_string = 'Toast za fajNych Ludzi Nie boJACYch sie Zycia'
upper_count, lower_count = count_case_characters(sample_string)
print(f"No. of Upper case characters : {upper_count}")
print(f"No. of Lower case Characters : {lower_count}")
