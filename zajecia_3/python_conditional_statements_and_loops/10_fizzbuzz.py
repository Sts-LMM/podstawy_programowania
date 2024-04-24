def FizzBuzz(min,max):
    for i in range(max):
        if(i%5 == 0 and i%3 == 0):
            print("fizzbuzz",end="")
        elif(i%5 == 0):
            print("fizz",end="")
        elif(i%3==0):
            print("buzz",end="")
        else:
            print(i,end="")
        print("")


FizzBuzz(0,50)