def generate_2d_array(rows, columns):
    two_d_array = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(i * j)
        two_d_array.append(row)
    return two_d_array

rows = 3
columns = 4

result = generate_2d_array(rows, columns)
print("Result:", result)
