# initial value
Jeff = "1. Yay, Bye"
print(Jeff)

# change value
Jeff = "2. Yubo is fat"
print(Jeff)

# multi- line string
Jeff = '''3. Hello my name is Jeff
I like to eat BREAKFAST!!'''
print(Jeff)

# dialogue
Jeff = '4. Jeff said "Hello my name is Jeff"'
print(Jeff)

# use single quotes to include double quotes
Nathan = '5. I said "I\'m very good at typing\"'
print(Nathan)

# use escape character to include double quotes
Nathan = "6. I said, \"I'm very good at typing\""
print(Nathan)

# embed value in strings
weight = 'one ton'
yubo = '7. The stranger said, "I am Yubo and I weigh %s"'
print(yubo % weight)
weight = '100000 pounds'
print(yubo % weight)
print(yubo % 3454324)
print(yubo % "356765458 pounds")

# embed two values in a string
yubo = '8. Then Yubo said "I used to weigh %s in march, now I weigh %s!"'
print(yubo % (2142143, 23456789876))
march_weight = 2142143
now_weight = 23456789876
print(yubo % (march_weight, now_weight))

# Make a letter!!
spaces = 110 * ' '
grid = '1234567890' * 13
print(grid)
print("%s418 Alliance circle" % spaces)
print("%sCary, NC" % spaces)
print("%sUnited States of America" % spaces)

# story
yubo_walking = 'Yubo walked up to a stranger and said, %s'
yubo_talking = '"Hello, my name is Yubo."'
spaces = 55 * ' '
print("%sThe Story of Yubo" % spaces)
print()
print(yubo_walking % yubo_talking)

# lists are totally better than strings!
fat_list = ['oil', 'cream cheese', 'ice cream', 'cake mix', 'sugar', 'patties']
print(fat_list[2])

bad_list = [1, 2, 3, 4]
print(bad_list)

good_list = [3, 4, 5, 6]
print(good_list)

print(1)
print(2)

Git_tests = [56, 43, 32, 45]
print(Git_tests)

push_pull = ['Git', 'is', 'so', 'awesome']
print(push_pull)

Git_tests.append(89)
print(Git_tests)
Git_tests.append('hi')
Git_tests.append('yay')
print(Git_tests)
del Git_tests[0]
print(Git_tests)

# combining lists
combine_1 = [1, 2, 3, 4]
combine_2 = ['Hello', 'my', 'name', 'is', 'Jeff']
combine_3 = combine_1 + combine_2
print(combine_3)
list_1 = [1, 2]
print(list_1 * 5)

# tuples
fibs = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
print(len(fibs))

# Maps
Family_age = {'Nathan': 12, 'Maddie': 15}
print(Family_age['Nathan'])
Family_age['Yubo'] = 46
print(Family_age)
Family_age['Sharon'] = 43
print(Family_age)

# Complaining about turtle
Complaint = ['Why', 'can', 'I', 'not', 'get', 'turtle!?']
print(Complaint)

# if and else statements
age = 25
if age > 20:
    print('you are too old!')

age = 20
if age == 19:
    print('Hi my name is Jeff!!')
else:
    print('Top secret can\'t tell you!!')

# requirement
# 1. <13 - small kid
# 2. 13 to 19 - teenager
# 3. 20 to 39 - young adult
# 4. 40 to 55 - middle age
# 5. 56 and up - elder
age = 45
if age < 13:
    print('You are a small kid')
elif age < 20:
    print(' You are a teenager')
elif age < 40:
    print('You are a young adult')
elif age < 56:
    print('You are a middle aged person')
else:
    print('You are an elder')

# loops
for x in range(0, 5):
    print('hello')
for c in range(1, 10, 2):
    print('hello %s' % c)
for y in range(7, 100, 7):
    print(y)
for j in range(8, 100, 8):
    print(j)
for l in range(3, 50, 3):
    print(l)
Fat = ['Yubo', 'is', 'very', 'fat']
for x in Fat:
    print(x)

print('\n\nLoop Exercise #1 - favorite activites')
print('=' * 70)

# Loop exercise 1
# From the Python for Kids book
# #3 My favorite activities
# (print out number along with the activity)
#  1 - Video game
#  2 - Watch TV
#  3 - Soccer
#  4 - Football
fav_activities = ['Video game', 'Watch TV', 'Soccer', 'running', 'Python']
print(fav_activities)
rank = 1
for x in fav_activities:
    print('%s.' % rank, x)
    rank = rank + 1

print('\n\nLoop Exercise #2 - my weight on the moon')
print('=' * 70)
# Loop exercise 2
# From the Python for Kids book
# #4 Your weight on the moon
# 1. Your weight grows 1 kg every year
# 2. moon weight is 0.165 times your earth weight
# 3. Print out your earth weight and moon weight each year
# for the next 15 nears
weight = 40  # current weight in 2018
year = 2018
str = "%s - earth weight: %s, moon weight: %.3f"
for x in range(0, 20):
    print(str % (year + x, weight, weight * 0.165))
    weight = weight + 1

print('\n\nLoop Exercise #3 - square of numbers')
print('=' * 70)
# Loop exercise 3
# Given a variable, say side=3, print out a square of numbers
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9

# HINT: using end='' will keep the next print in the same line
side = 3
print('side = ', side)
print('1', end=', ')
print('2', end=', ')
print('3')
print('4', end=', ')
print('5', end=', ')
print('6')
print('7', end=', ')
print('8', end=', ')
print('9')

# The above is the manual way of printing the square
# Now, it's Nathan's turn to write a real program
side = 4
# Here's the program to print out the square
# ...
# ...
print('side = ', side)
for x in range(0, side):
    for y in range(0, side):
        n = side * x + y + 1
        print(n, end=', ')
    print()

# double loop practice
print('side = ', side)
for x in range(0, side):
    for y in range(0, side):
        n = side * y + x + 1
        print(n, end=', ')
    print()

# probability exercise
shirt = ['red', 'yellow', 'white', 'orange', 'grey']
pants = ['blue', 'black', 'green']

# Expected output:
# red shirt, blue pants
# red shirt, black pants
# ...
# There are 6 combination
str = '%s. %s shirt, %s pants'
n = 1
for x in shirt:
    for y in pants:
        print(str % (n, x, y))
        n = n + 1
print('There are %s combos' % (n - 1))

# triple loops
shoes = ['nike', 'addidas']
shirt = ['red', 'yellow', 'white', 'orange', 'grey']
pants = ['blue', 'black', 'green']
# red shirt, blue pants, nike shoes
# red shirt, black pants, ...
# ...
print()
print()
print('Triple loop challenge DIY')
print('=' * 70)
print()
k = 1
string = '%s. %s shoes, %s shirts, %s pants'
for x in shoes:
    for y in shirt:
        for z in pants:
            print(string % (k, x, y, z))
            k = k + 1
print('There are %s combos' % (k - 1))

print('\nLoop to find denominators')
print('=' * 70)

n = 20
# print out all denominators of n
# 1, 2, 4, 5, 10, 20
#
# To test if i is divisble by n:
#   if (n % i == 0)
i = 5
if (n % i == 0):
    print('%s is a denominator of %s' % (i, n))
else:
    print('no lucK')

n = 4
m = 0
for x in range(1, n + 1):
    if (n % x == 0):
        print(x, end=', ')
        m = m + 1
        if (m % 20 == 0):
            print()
print()
print('There are %s factors of %s' % (m, n))

# Loop exercise: check for prime number
# check if n is a prime number
# if a number has only 2 factors (1 and itself),
# then it's a prime number
# The program should print the following:
#    113 is a prime number
# or 113 is not a prime number
# ========Enjoy================================
if (m < 2):
    print('%s is not a prime or composite number' % n)
elif (m == 2):
    print('%s is a prime number' % n)
else:
    print('%s is a composite number' % n)


# Function: def
def isOdd(x):
    if (x % 2 == 0):
        return False
    else:
        return True


print('4 is odd:', isOdd(4))
print('5 is odd:', isOdd(5))


# Please implement isPrime(x)
# so that isPrime(5) will return True
# and isPrime(6) will return false
def isPrime(x):
    for y in range(2, x):
        if(x % y == 0):
            return False
    return True


x = 0
print('%s is prime' % x, isPrime(x))