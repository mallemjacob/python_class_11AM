# The Collatz Sequence

# 1. Write a function named collatz() that has one parameter named number.

# 2. If number is even, then collatz() should print number // 2 and return this value.

# 3. If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


while True:
    try:
        print('Enter a number: ')
        userInput = int(input())  # '3' -->
        while True:
            if userInput == 1:
                break
            else:
                return_value = collatz(userInput)  # 2
                userInput = return_value  # 2
        break
    except ValueError:
        print('Input must be interger, not any other datatype.')

# Home work
# ------------
# Add try except to collatz problem.


# FizzBuzz
# if divisible by 3 and 5 print "fizzbuzz"
# if divisible by 3, print "fizz"
# if divisible by 5, print "buzz"
