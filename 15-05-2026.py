# Importing Modules


# A Short Program: Guess the Number

# random module
# import sys
# import random

# randomNumber = random.randint(1, 10)

# is_guessed = False

# for i in range(1, 7):  # 1,2,3,4,5,6
#     print('I am thinking of a number between 1 and 10.')
#     userGuess = int(input())

#     if userGuess > randomNumber:
#         print("You guess is too high")
#     elif userGuess < randomNumber:
#         print("You guess is too low")
#     else:
#         print('You guessed correctly')
#         is_guessed = True
#         break

# if is_guessed:
#     print("You guessed in " + str(i) + " steps.")
# else:
#     print("Didnt guessed correctly. Try again.")


# sys module

# import sys

# while True:
#     print('Type exit to exit')
#     user_input = input()
#     if user_input == 'exit':
#         sys.exit()


# print('The end')


import webbrowser

while True:
    print('Enter a url to open the website or type exit to exit:')
    url = input()
    if url == 'exit':
        break
    else:
        webbrowser.open(url)


# Homework
# Give user options to choose from with serial numner and the wrbist name. wrtie a loop to ask user to type a number and based on the number open the website in the browser.
