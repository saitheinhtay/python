"""Bitmap Message, by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, artistic"""

import sys

# (!) Try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of this string:
# (You can also copy and paste this string from
# https://inventwithpython.com/bitmapworld.txt)
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""


print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end='')
    print()
