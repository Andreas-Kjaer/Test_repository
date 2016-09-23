'''working with iterations from justin bois bootcamp, day 1'''

# Make up a random sequence
seq = 'GACAGACUCCAUGCACGUGGGUAUCUGUC'

# Make an empty counter
gc_cont = 0

# Make a sequence length counter
len_seq = 0

# Loop through sequence and count G's and C's
for base in seq:
    len_seq += 1
    if base in 'GCgc':
        gc_cont += 1

# Divided gc_count with the length to get ratio
print((gc_cont / len_seq) * 100, '%')

''' when doing a for loop, the iterator copies the value from the list it is iterating through
Thus we cannot e.g. multiply a list of integers with 2 like this (atleast we cannot save it)
, because it does not save the values. Instead we can use enumerate'''

# We'll do one through 5
my_integers = [1, 2, 3, 4, 5]

# Double each one
for n in my_integers:
    n *= 2

# Check out the result
print(my_integers)
'''using enumerate it works, because we treat each index'''
# Square each one
for i, _ in enumerate(my_integers):
    my_integers[i] *= 2

# Check out the result
print(my_integers)

'''Remember that we can only do this to a list because a list is mutable. Thus Tuples and strings would not work'''
"""In the previous example, we iterated over a sequence. A sequence is one of many iterable objects,
called iterables. Under the hood, the Python interpreter actually converts an iterable to an iterator.
An iterator is a special object that gives values in succession.
A major difference between a sequence and an iterator is that you cannot index an iterator.
This seems like a trivial difference, but iterators make for more efficient computing
under the hood that directly using a sequence.
We can explicitly convert a sequence to an iterator using the built-in function iter(),
but we will not bother with that here because the Python interpreter does this for you automatically
when you use a sequence in a loop."""

'''The range function gives an iterable that enables counting.'''
for i in range(2 ,10, 3):
    print(i, end='  ')

''' We can also use range for making convenient lists or tuples'''
my_easy_list = list(range(10))
print(my_easy_list)
for i, base in enumerate(seq):
    print(i, base)

''' The zip function allows us to iterate over several iterators in one.'''

Names = ('Andreas', 'Thoeger', 'Patrick')
Age = ('Old enough', 'Too old', 'Youngling')
Interests = ('Dark rooms', 'Computers', 'Pipettes')
for i, j, y in zip(Names, reversed(Age), Interests):
    print(i, 'is', j, 'and likes', y)

'''Using a for-loop you set up an iterator. In a while loop you keep going till you meet
a conditional requirement'''

#Making i start at 0
i = 0
#reading through seq in triplets until we meet aug or AUG
while seq[i:i+3] != ('AUG' or 'aug') and i < len(seq):
    i += 1

#print if it does not find anything
if i == len(seq):
    print('The codon of interest was not found in this sequence')
else:
#print the position of the codon
    print('The start codon is at index', i)

'''A break statement in the for loops stops it, and the else statement is skipped'''
x = 1
while x > 0:
    x += 1
    print(x)
    if x == 200:
        break
    else:
        print('This won\'t get printed in the end')




