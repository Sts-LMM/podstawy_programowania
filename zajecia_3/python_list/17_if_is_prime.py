def check_if_all_prime(numbers):
  for number in numbers:
    if not is_prime(number):
      return False

  return True


def is_prime(number):

  if number <= 1:
    return False

  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False

  return True


numbers = [2, 3, 5, 6, 7, 11, 12 , 13, 17, 19, 45]

if check_if_all_prime(numbers):
  print("All numbers are prime.")
else:
  print("Not all numbers are prime.")
