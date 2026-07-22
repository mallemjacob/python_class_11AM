
# def greet(name):
#     return 'Hi ' + name


# retune_value_1 = greet('mouse')
# retune_value_2 = greet('cat')


# print(retune_value_1)
# print(retune_value_2)

# Default arguments


# def hello(name="Stranger", age=0):
#     print("Hi there " + name)
#     print("you are " + str(age) + " years old.")


# hello()

# # Keyword arguments
# hello(age=21, name='mouse')


# hello()
# hello(age=21, name='mouse')


# Variable-length arguments


# def adder(*n):  # args = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#     total = 0
#     for i in n:
#         total = total + i  # 1
#     return total


# return_value = adder(11, 26, 33, 42, 57)

# print(return_value)


# total = 0
# for i in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     total = total + i


# print(total)


# **kwargs - Variable-length keyword arguments


# It takes multiple keyword arguments and stores it in kwargs parameter
def greet(**kwargs):
    # Looping through the kwargs dictionary
    for k, v in kwargs.items():
      # k represents key and v represents value
        print(k, v)


greet(name='Mouse', age=2, color='grey')


# function definiton
# function calling
# return statement
# arguments
# parameters
# default arguments
# keyword arguments
# variable length arguments
# comments
