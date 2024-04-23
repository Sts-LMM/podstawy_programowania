def converter_C_and_F(temperature):
    if temperature[-1:].upper() == 'C':
        c = int(temperature[:-1])
        temp = (c *9 +32*5)/5
        print(c,"Celcius equals to ",temp,"Farenheit")

        return 
    elif temperature[-1:].upper() == 'F':
        f = int(temperature[:-1])
        temp = (f-32)*5/9
        print(f,"Farenheit equals to ",temp,"Celcius")
        return 
    else:
        print("Please enter the valeue correctly")
        return

user_input = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
converter_C_and_F(user_input)