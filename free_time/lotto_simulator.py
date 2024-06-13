import random #Stanislaw Muter 163065

def num_entering(min_val, max_val, used_numbers):
    while True:
        try:
            num = int(input(f"Please enter a number between {min_val} and {max_val} that hasn't been used yet: "))
            if num in used_numbers:
                print(f"Number {num} has already been used. Please try again.")
            elif min_val <= num <= max_val:
                print(f"Thank you! You entered {num}.")
                return num
            else:
                print("Number out of range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def draw(how_many_nums, num_limit, lottery_num_range, enter_yourself):
    all_coupons = [[0] * num_limit for _ in range(how_many_nums)]
    if enter_yourself == 2:
        for i in range(how_many_nums):
            available_numbers = list(range(1, lottery_num_range + 1))
            for j in range(num_limit):
                chosen_num = random.choice(available_numbers)
                all_coupons[i][j] = chosen_num
                available_numbers.remove(chosen_num)
    else:
        for i in range(how_many_nums):
            used_numbers = []  
            for j in range(num_limit):
                print(f"You are betting on coupon {i+1}, number {j+1}:")
                chosen_num = num_entering(1, lottery_num_range, used_numbers)
                all_coupons[i][j] = chosen_num
                used_numbers.append(chosen_num)  
    return all_coupons

def money_counting(matching_nums):
    if matching_nums == 0:
        return 0
    else:
        total = pow(10, matching_nums - 1)
        return total

def main():
    while True:
        print("Lotto ticket probability calculator:")
        print("How many numbers are on the lotto card:")
        how_many_nums_in_pool = num_entering(45, 60, [])
        print("Amount of winning numbers:")
        how_many_nums_to_win = num_entering(3, 10, [])
        print("How many coupons do you want to bet:")
        how_many_bets = num_entering(1, 10, [])
        print("Do you want to bet numbers yourself (1 YES, 2 NO):")
        enter_yourself = num_entering(1, 2, [])
    
        coupon_list = draw(how_many_bets, how_many_nums_to_win, how_many_nums_in_pool, enter_yourself)
        print("Generated coupons:")
        for coupon in coupon_list:
            print(coupon)
        print("Now the winning numbers are...")
        winning_numbers = draw(1, how_many_nums_to_win, how_many_nums_in_pool, 2)
    
        for i in range(how_many_nums_to_win):
            print(winning_numbers[0][i])
    
        how_many_matching_nums = []
        wins = 0
        for i in range(how_many_bets):
            matching_nums = 0
            for coupon_num in coupon_list[i]:
                if coupon_num in winning_numbers[0]:
                    matching_nums += 1
            how_many_matching_nums.append(matching_nums)
            if matching_nums > 0:
                wins += 1
                print(f"Coupon {i + 1} matched {matching_nums} numbers. You won {money_counting(matching_nums)}$!")
    
        if wins == 0:
            print("No wins this time. Better luck next time!")
    
        print("Do you want to play again? (1 YES, 2 NO):")
        play_again = num_entering(1, 2, [])
        if play_again == 2:
            break
        else:
            continue
    

main()
