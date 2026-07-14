# Loops


# while, for

# while i'm teaching class, take notes


# if condition:
#     code

# while condition:
#     code


# if 2 > 1:
#     print('hi')

# while 2 > 1:
#     print('hi')


# i = 1  # 1
# i = i + 1  # 2
# i = i + 1  # 3
# i = i + 1  # 4


# i = 1  # 1

# while 10 >= i:
#     print(i)
#     i = i + 1  # 11


run = True

while run:
    print('hi, welcome, enter your username:')
    username = input()  # 'admin'
    if username == 'admin':  # 'admin' == 'admin'
        print('Enter your password:')
        password = input()  # 'swordfish'
        if password == 'swordfish':
            print('Welcome to your account')
            run = False
        else:
            print('Wrong password!')
    else:
        print('Wrong username')


# break, continue


# while True:
#     print('Enter your name: ')
#     name = input()
#     if name == 'mouse':
#         break
#     else:
#         print('Try again')


# i = 1  # 1

# while 10 >= i:
#     if i == 5:
#         break
#     else:
#         print(i)
#         i = i + 1  # 2


# for loop

# for i in range(1, 11, 3):  # 1,2,3,4,5,6,7,8,9,10
#     print(i)

# for i in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     if i == 6:
#         break
#     else:
#         print(i)
