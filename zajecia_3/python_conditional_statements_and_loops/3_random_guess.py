import random

def guess_the_num(awnser):
    users_guess = int(input("This silly games mission is to guess random number from 1 to 10: "))
    num_of_try = 1
    while(users_guess != awnser):
        users_guess = int(input("Try again to guess random number from 1 to 10: "))
        num_of_try = num_of_try + 1
        print("Your guess is: ",users_guess)
    print("You got it! It only took you: ",num_of_try," guesses.")
key_num = int(random.randrange(1,10))
guess_the_num(key_num)
print("Correct number is: ", key_num )