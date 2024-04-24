def fibonacii(min,max):
    x1=0
    x2=1
    replace = 0
    while True:
        replace = x1
        x1=x2
        x2 = x1 + replace
        if(x1<min):
            continue
        elif(x1>max):
            break
        else:
            print(x1,end=" ")


fibonacii(0,50)