def rounding(to_round):
    print("Formatted Number: "+"{:.2f}".format(to_round))

num_to_round = float(input("Enter num to round: "))
print("~~~~~~~~~~~~")
print("Before: ",num_to_round)
rounding(num_to_round)
print("~~~~~~~~~~~~")