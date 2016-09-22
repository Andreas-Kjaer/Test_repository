"""to determine the type of some variable, you can do type(variable)
fx you can do:"""
print(type(3))
print(type(3.4))
print(type('hvad er jeg'))

''' using tripple allows you to type
over several lines, unlike single quotes '''
'single quotes only allows you to write on a single line' \
'and you thus need to add a newline in order to write on the next line with its own pair of quotes'

print ('hmm')


"""operators are encoded in python and holds the known mathematical meaning for most of them
such as the plus, minus and division"""

some_variable = 5 + 5
print(some_variable)
another_variable = some_variable - 3
print(another_variable)
third_variable = another_variable * some_variable
print(third_variable)
'''using one slash gives a float'''
last_variable = third_variable / 3.1
print(last_variable)
print(type(last_variable))
'''using double rounds the number down, but the type is still a float'''
last_variable = third_variable // 3.1
print(last_variable)
print(type(last_variable))

'''you can use operators on strings similarly to what is described above'''
print('I\'m now going to concatenate this string' + ' -- with this string')

''' we cannot substract, divide or multiply strings, of course. But we CAN multiply strings with integers
as such:'''
print('this string will now be trippled | ' * 3)

''' different operators are the known plus (+), minus (-), division (/), exponentiation (**),
 bitwise from decimal to binary (^), modulus (%), divide and discard remainder (//)'''

'say that you want to convert a string type, which is a number. You can do:'

my_str = '42'
my_int = int(my_str)
print(type(my_int))

'you can also convert it back to a string by:'
my_str_again = str(my_int)
print(type(my_str_again))

'when you try to convert floats to integers it just discards the numbers on the right of the dot'
my_int_from_float = int(42.7)
print(my_int_from_float)

'''apart from the arithmetic operators discussed above (the plus, minus etc) there are other types
such as relational operators in which we ask the question, what is a compared to b
double equal signs says whether the statement a is equal to b is true or not'''

print('this is a relational operator output', 5 == 5)
print('this is a relational operator output with a false statement', 5 == 4)

''' the output type is boolean, that is, it is either true or false. This can be quite dangerous for floats
as floats are sometimes not correct.
Because floats are described by a finite number of bytes, some floats are not perfect.
An example of such a situation is seen below'''

print('an example where floats are not working as they should', 2.2 + 3.1)
print('this means, that when asking for true or false for 2.2 + 3.1 == 5.3 you get false', 2.2 + 3.1 == 5.3)

''' THAT IS WHY YOU SHOULD GENERALLY NEVER USE == WITH FLOATS'''

'''other relational operators include != (is not equal to), < (is less than), > (is greater than), >= (is greater
than or equal to) etc.'''

''' Characters in python are unicode characters. This means every letter has a different number. We
can get information about the number by using a built-in function called ord'''

print(ord('a'))
print('is a equal to the number 97?', ord('a') == 97)
print('because characters has a number we can compare strings like DNA sequences'
      , 'AGTCATA' == 'AGTCATA', 'AGTCATA' == 'AGTCA')

print('be aware that when chaining relational operators they only compare neighbours', 4 < 6 > 1)

'''another type of operators are identity operators. They tell you whether two variables take up
the same space in memory (i.e. it tells you whether two input varables are really the same variable!).
This is different from == because == tells you if two variables have the same value, not if they are the same thing'''
str_1 = 'Hello, world.'
str_2 = 'Hello, world.'

print(str_1 == str_2, str_1 is str_2)

a = 2
b = 2
print(a is b)

'''another type of operator are the logical operator. These are AND, OR and NOT.
AND means if both a and b are true, return true. If OR is used, either one of two needs to be true in order
for OR to return true, and NOT returns true if the input is false'''

print('using \'and\' command', True and True, True and False, False and False)
print('using \'or\' command', True or True, True or False, False or False)
print('using \'not\' command', (not True) and True, not (False and True), not False or True)

'''remember that True and False have values 1 and 0'''

print(True + True, True + False, False + False)

'''Conditional statements. In the below example codon == AUG is the condition
else is a clause which is used in case the condition returns false. You can nest conditionals
instead of doing else and making a new line for a new if condition, you can make it shorter
by writing elif (not done below for clarity)'''
codon = 'AGA'
if codon == 'AUG':
    print('the codon is', codon, '... A start codon')
    print('Any lines with the same level of indentation will be evaluated together')
else:
    if codon == 'UGA' or codon == 'UAA' or codon == 'UAG':
        print(codon, 'is a stop codon')
    else:
        print(codon, 'is not a start nor stop codon')


