import  sys
from    random  import  randint

a = 0
x = randint(1, 99)
print ('This is an interactive guessing game!\nYou have to enter a number between 1 and 99 '
    'to find out the secret number.\nType \'exit\' to end the game.\nGood luck!\n')
n = x + 1
while (n != x):
    n = input('What\'s your guess between 1 and 99?\n')
    if n == 'exit':
        sys.exit()
    try:
        n = int(n)
    except:
        print ('That\'s not a number\n')
        a = a + 1
        continue
    if n > x:
        print ('Too high!\n')
        a = a + 1
    elif n < x:
        print ('Too low!\n')
        a = a + 1
    elif n == x:
        print ('Congratulations, you\'ve got it!\nYou won in %i attempts!' % a)
        sys.exit()
    