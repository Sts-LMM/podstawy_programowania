def chech_if_divisable_by_x_and_y(min,max,x,y):
    for i in range (min-1,max+1):
        if (i % x ==0 and i % y == 0):
            print("Number ", i, "is divisable by ",x," and ",y)
        else:
            print("Number ", i, "is NOT divisable by ",x," and ",y)
    return

chech_if_divisable_by_x_and_y(1500,2700,5,7)