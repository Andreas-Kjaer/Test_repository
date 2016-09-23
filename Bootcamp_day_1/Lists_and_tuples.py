''' Investigating list and tuples as part of the first day in Bootcamp'''

my_list = [1, 2, 3, 4]
print(type(my_list))

my_string = 'hello world'
print(list(my_string)[2:5])
print(list(my_string)[::2])

'''we can use membership operators to ask whether something is in our list or not'''

print('l' in my_string, 'z' in list(my_string), 'l' in list(my_string), 'z' not in list(my_string))

# Make a list of stop codons
stop_codons = ['UAA', 'UAG', 'UGA']

# Specify codon
codon = 'UGG'

# Check to see if it is a start or stop codon
if codon == 'AUG':
    print('This codon is the start codon.')
elif codon in stop_codons:
    print('This codon is a stop codon.')
else:
    print('This codon is neither a start nor stop codon.')

'''lists are mutable. Meaning I can change the value at a given index.
When changing lists, the id doesnt change (same place in memory. This is unlike
redefining a variable e.g. changing a = 2 to a = 3, which makes a new position in memory'''

my_list[2] = 'I just decided to put this as nr. 2!'
print(my_list)

''' unlike lists, tuples are immutable. To make a tuple you must put a comma after the number, and
let it all be in parenthesis'''

print(type(tuple(my_list)))
my_list_as_tuple = tuple(my_list)
print(my_list_as_tuple)

'''always try to use tuples, and only make them into lists when you need to change something.
After you are done, make the list back into a tuple to avoid mistakes'''