# Exception Handling


# print(2 + "hi")


# def dviByzero(p):
#     try:
#         return 2 / p
#     except ZeroDivisionError:
#         return "Can not divide by zero"


# print(dviByzero(1))
# print(dviByzero(2))
# print(dviByzero(0))
# print(dviByzero(5))


# try:
#     print(2 + "hi")
# except TypeError:
#     print('Can not concanetane 2 different data types')


while True:
    print('Enter a number: ')
    userInput = int(input())  # 0

    try:
        print(2 / userInput)
        break
    except ZeroDivisionError:
        print('Can not divide by zero. Try again.')
