def lowercase(text):
    final_text = text.lower()
    return final_text


test_data = input("Enter password and get it lowercased: ")
print("Before: ",test_data)
result = lowercase(test_data)
print("After:", result)
