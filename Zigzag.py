# ********
#  ********
#   ********
#    ********
#     ********
#      ********
#     ********
#    ********
#   ********
#  ********
# ********

import time


def zigzag(word, speed):

    count = 0
    direction = True

    for i in range(30):
        print(' ' * count, end='')
        print(word)
        time.sleep(speed)

        if direction:
            if count == 5:
                direction = False
            else:
                count = count + 1
        else:
            if count == 0:
                direction = True
            else:
                count = count - 1


zigzag('*******', 0.2)


# Homework
# Make zigzap pattern 25 times
