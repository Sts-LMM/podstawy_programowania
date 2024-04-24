def data_and_type_printer(type_and_data):
    for i in range(len(type_and_data)):
        print(type_and_data[i], type(type_and_data[i]))
    return 0


datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
print("Data to analize:",datalist)
print("")
print("")
data_and_type_printer(datalist)