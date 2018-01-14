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