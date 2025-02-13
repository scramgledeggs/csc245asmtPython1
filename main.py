from random import random, randint

print('Hello, World!')

#*----------------------------------------------*#

print('5 + 10 = ', 5 + 10)
print('20 - 7 = ', 20 - 7)
print('3 * 8 = ', 3 * 8)
print('25 / 5 = ', 25 / 5)

#*----------------------------------------------*#

x = 19
print('I am ', x, 'years old')

#*----------------------------------------------*#

celTemp = float(input('Temperature in celsius: '))
farTemp = (celTemp * 9/5) + 32
print('Temperature in Fahrenheit: ', farTemp)

#*----------------------------------------------*#

num1 = int(input('Enter a number: '))

if num1 % 2 == 1 :
    print(num1,'is odd.')
else:
    print(num1,'is even.')

# *----------------------------------------------*#

num2 = int(input('Enter a number: '))

if num2 > 0:
    print(num2,'is positive.')

elif num2 < 0:
    print(num2,'is negative.')

else:
    print(num2,'is zero.')

# *----------------------------------------------*#

numbers = [2, 6, 9, 4]
numbers.append(10)
numbers.remove(2)
print(len(numbers))
numbers.sort()
print(numbers)

# *----------------------------------------------*#

num3 = int(input('Enter a number:'))
y = num3

for x in range(1, num3):
    y = y*x
    print(y)
else:
    print('The factorial of ', num3, 'is', y)

# *----------------------------------------------*#

num4 = int(input('Enter a number:'))

for x in range(1,11):
    print(num4, ' x ', x, ' = ', num4*x)

# *----------------------------------------------*#

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x=0
for x in range(len(numbers)):
    y=y+x

print("The sum of the numbers is:", y)

# *----------------------------------------------*#

num5 = randint(1, 20)
x = -1
print("I'm thinking of a number between 1 and 20. Try to guess it!")

while num5 != x:
    x = int(input('Your guess: '))
    if x > num5:
        print('Too high. Guess again.')
    elif x < num5:
        print('Too low. Guess again.')
    elif x == num5:
        print('Correct! The number was ', num5)
    else:
        print("??? If you got this you probably didn't put in a number. Guess again.")

# *----------------------------------------------*#

string1 = input('Enter a string: ')
vowels = "aeiouAEIOU"

charL = list(string1)
q = sum(charL.count(vowel) for vowel in vowels)

print('There are', q, 'vowels in', string1)

# *----------------------------------------------*#

for x in range(1, 100):
    if x % 5 == 0 & x % 3 == 0:
        print('FizzBuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')
    else:
        print(x)

# *----------------------------------------------*#

string2 = input('Enter a string: ')
z = list(string2)
z.reverse()
string2 = ''.join(z)
print(string2)

# *----------------------------------------------*#
