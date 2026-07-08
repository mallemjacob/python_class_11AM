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
#     print('hi')
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
