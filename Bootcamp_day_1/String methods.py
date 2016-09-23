''' This section will show various built-in tools to modify strings'''

'''We can use string.count to more efficiently complete a previous task of calculating GC content'''

# Define sequence
seq = 'GACAGACUCCAUGCACGUGGGUAUCAUGUC'

# Count G's and C's
GC_count = seq.count('G') + seq.count('C')
print(GC_count)

'''my_str.string_method_of_choice(*args) is the syntax. functions that are built in like "count"
are called methods. count does not overlap when counting (see below)'''
print('AAAAAAAAAAA'.count('AA'))

'''Also, it is easier to use find to find something e.g. a start codon'''
print(seq.find('AUG'))
print(seq.find('SOMETHING THAT IS NOT PRESENT'))
''' find gives the value -1 when something is not there. This is not good if you want to verify
the presence of something. Use the operator "in" instead, if this is what you wanna do'''
'''We can also search from the other end (the right) with rfind'''
print(seq.rfind('AUG'))

'''We can make all characters in a string capital or lower by .lower and .upper'''
print('LeBron James'.lower())
print('Make me aLl caPS.'.upper())

'''A cool tool is also .join. I use the ' ' section to indicate what goes between each index'''
word_tuple = ('The', 'Dude', 'abides.')
print(' '.join(word_tuple))

''' The format command is also really cool and lets you put strings into your string at places
described by braces {}'''
print('There are {n:08d} states.'.format(n=50))
print('Your file number is {n:d}.'.format(n=23))
print('π is approximately {pi:f}.'.format(pi=3.14))
print('e is approximately {e:.8f}.'.format(e=2.7182818284590451))
print('Avogadro''s number is approximately {N_A:e}.'.format(N_A=6.022e23))
print('ε_0 is approximately {eps_0:.16e} F/m.'.format(eps_0=8.854187817e-12))
print('That {thing:s} really tied the room together.'.format(thing='rug'))

''' A cool place to look is https://docs.python.org/3.5/library/stdtypes.html#string-methods. Here is a list
of all the built-in string methods available'''