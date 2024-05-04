def avg_calculator(x):
    if (len(x)==0):
        return 0
    else:
        avg = sum(x)/len(x) # sum of all the grades devided by ammount of them
        return avg
        
grades = [4.5,2.5,3.0,6.0,5.5]

print("Avg grade:", avg_calculator(grades))  