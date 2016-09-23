''' In this section we will cover the topic of functions and how to create them in python'''

'''A function in defined using the def keyword'''
def ratio(x, y):
    """The ratio of `x` to `y`."""
    return x / y
''' Whenever a function is defined the indentation goes back to the left, indicating the definition
of a function is complete. Also note that the doc-string is immediately after the function definition.
In the next line of the function, we see a return keyword.
Whatever is after the return statement is, you guessed it, returned by the function.
Any code after the return is not executed becuase the function has already returned!'''
''' After writing a function we can call it'''
print(ratio(2, 57))
''' No need to have arguments in the return statement'''
def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    """Simpler program than Deep Thought's, I bet."""
    return 42
print(answer_to_the_ultimate_question_of_life_the_universe_and_everything())
''' There does not need to be a return statement. In case there is none (or in case it is not executed),
the return statement is the keyword None meaning nothing in python language'''
def think_too_much():
    """Express Caesar's skepticism about Cassius"""

    print("""Yond Cassius has a lean and hungry look,
He thinks too much; such men are dangerous.""")

variable_name = think_too_much()

think_too_much()

print('rubaduba', variable_name)

'''NEVER NAME YOUR OWN FUNCTIONS THE SAME AS THE BUILT IN FUNCTIONS OF PYTHON
https://docs.python.org/3.5/library/functions.html - A LIST OF BUILT IN FUNCTIONS'''

'''Also we will have a hard time trying to rename keywords that are built in, such as True and False
A complete list of these are found here - https://docs.python.org/3.5/reference/lexical_analysis.html#keywords'''

'''Now I will try to write a function that makes a reverse complement of an input sequence
It is important to split functions into as small bits as possible. We should write small concise functions
so that we can call them independently. (we write modules)'''
def complement_base_DNA(input_base, material = 'DNA'):
    """Returns the Watson-Crick complement of a base."""
    for base in input_base:
        if base == ('A' or 'a'):
            if material == 'DNA':
                return 'T'
            elif material == 'RNA':
                return 'U'
        elif base == (('T' or 'U') or ('t' or 'u')):
            return 'A'
        elif base == ('G' or 'g'):
            return 'C'
        elif base == ('C' or 'c'):
            return 'G'
def reverse_complement(seq, material = 'DNA'):
    """Compute reverse complement of a sequence."""
    rev_seq = ''
    complement_reverse = ''
    for nucleic_acid in reversed(seq):
        rev_seq += nucleic_acid
    for base in rev_seq:
        complement_reverse += complement_base_DNA(base, material=material)
    return complement_reverse
seq = 'AGCCCGGACGAGCACGTTTTTTTTTT'
print(reverse_complement(seq, material='RNA')[::-1] + '\n' + (len(seq)* '|') + '\n' + seq)

'''We can feed keyword arguments (like the material is just above) in shape of tuples if we just add a *
in front of them'''