'''The concluding exercise for the first day of Bootcamp'''

'''Problem 1.2: Using string methods
In Lesson 7, we wrote a function to compute the reverse complement of a sequence.
a) Write that function again, still using a for loop, but do not use the built-in reversed() function.'''
'I decided to slice with -1 step instead str[::-1]'
# def complement_base_DNA(input_base, material = 'DNA'):
#     """Returns the Watson-Crick complement of a base."""
#     for base in input_base:
#         if base == ('A' or 'a'):
#             if material == 'DNA':
#                 return 'T'
#             elif material == 'RNA':
#                 return 'U'
#         elif base == (('T' or 'U') or ('t' or 'u')):
#             return 'A'
#         elif base == ('G' or 'g'):
#             return 'C'
#         elif base == ('C' or 'c'):
#             return 'G'
# def reverse_complement(seq, material = 'DNA'):
#     """Compute reverse complement of a sequence."""
#     rev_seq = ''
#     complement_reverse = ''
#     for nucleic_acid in seq[::-1]:
#         rev_seq += nucleic_acid
#     for base in rev_seq:
#         complement_reverse += complement_base_DNA(base, material=material)
#     return complement_reverse
# seq = 'AGCCCGGACGAGCACGTTTTTTTTTT'
# print(reverse_complement(seq, material='RNA')[::-1] + '\n' + (len(seq)* '|') + '\n' + seq)
'''b) Write the function one more time, but without any for loops.'''
# def complement_base_DNA(input_sequence):
#     """Returns the Watson-Crick complement of a base."""
#     input_base_lower = input_sequence.lower()
#     g_to_c = input_base_lower.replace('g', 'C')
#     c_to_g = g_to_c.replace('c', 'G')
#     a_to_t = c_to_g.replace('a', 'T')
#     t_to_a = a_to_t.replace('t', 'A')
#     return(t_to_a.upper())
# def reverse_complement(seq):
#     """Compute reverse complement of a sequence."""
#     return complement_base_DNA(seq)[::-1]
# seq = 'AGGGGGTTTTTCCCCCAAAAATATATA'
# print(reverse_complement(seq))
# print(reverse_complement(seq)[::-1] + '\n' + (len(seq)* '|') + '\n' + seq)

'''Problem 1.3: Longest common substring
Write a function that takes two sequences and returns the longest common substring.
A substring is a contiguous portion of a string. For example:
Substrings of ATGCATAT:
TGCA
T
TAT

Not substrings of ATGCATAT:
AGCA              # Skipped T
CCATA             # Added another C
Hello, world.     # Has nothing to do with the input sequence'''

# def longest_common_substring(s1, s2):
#     """Return one of the longest common substrings"""
#
#     # Make sure s1 is the shorter
#     if len(s1) > len(s2):
#         s1, s2 = s2, s1
#
#     # Start with the entire sequence and shorten
#     substr_len = len(s1)
#     while substr_len > 0:
#         # Try all substrings
#         for i in range(len(s1) - substr_len + 1):
#             if s1[i:i + substr_len] in s2:
#                 return s1[i:i + substr_len]
#
#         substr_len -= 1
#
#     # If we haven't returned, there is no common substring
#     return ''

'''Problem 1.4: RNA secondary structure validator
In this problem, we will write a function that takes an RNA sequence and an RNA secondary structure and decides if the secondary structure is possible given the sequence. Remember, single stranded RNA can fold back on itself and for base pairs. An RNA secondary structure is simply the list of base pairs that are present. We will represent the base pairs in dot-parentheses notation. For example, a sequence/secondary structure pair would be
0123456789
GCATCTATGC
(((....)))

For convenience of discussion, I have labeled the indices of the bases on the top row.
In this case, base 0, a G, pairs with base 9, a C. Base 1 pairs with base 8, and base 2 pairs with base 7.
Bases 3, 4, 5, and 6 are unpaired. (This structure is aptly called a "hairpin.")
So, I hope the dot-parentheses notation is clear.
An open parenthesis is paired with the parenthesis that closes it. Dots are unpaired.
So, the goal of our function is to check all base pairs present in a secondary structure
and see if they are with G-C, A-U, or (optionally) G-U.
a) Write a function to make sure that the number of closed parentheses is equal to the number of
open parentheses, a requirement for a valid secondary structure.
It should return True if the parentheses are valid and False otherwise.'''


def valid_fold_check(RNA_fold_seq):
    '''Returns true in case a folding sequence is valid. I.e. has equal numbers of '(' and ')' '''
    count = 0
    for i in RNA_fold_seq:
        if i == ')':
            count -= 1
            if count < 0:
                return False
        elif i == '(':
            count += 1
    if count == 0:
        return True
    else:
        return False


# print(valid_fold_check(')(()()(((())((.........))))'))

'''b) Write a function that converts the dot-parens notation to a tuple of 2-tuples representing the base pairs.
We'll call this function dotparen_to_bp(). An example input/output of this function would be:
dotparen_to_bp('(((...)))')

((0, 9), (1, 8), (2, 7))

Hint: You might find the pop() method of lists useful.'''
# def dotparen_to_bp(sequence):
count = 0
sequence = '(((..)))...((.......))..((..))..(((.....)))'
for i, j in enumerate(sequence):
    if j == '(':
        # print(i, j)
        for x, y in enumerate(sequence[i:]):
            print('this is x', x, 'and this is y', y)
            # print('this is i', i, 'and this is j', j)
            if sequence[x] == '(':
                count += 1
            elif y == ')':
                count -= 1
                if count == 0:
                    print('this is i', i, 'and this is j', j)
                    print(i, x )
                    break
# return list_closed
# seq_fold = '(((..)))...((.......))..((..))..(((.....)))'
# print(valid_fold_check(seq_fold))
# print(dotparen_to_bp(seq_fold))
'''c) Because of sterics, the minimal length of a hairpin loop is three bases. A hairpin loop is a series of unpaired bases that are closed by a base pair. For example, the secondary structure (.(....).) has a single hairpin loop of length 4. So, the structure ((((..)))) is not valid because it has a hairpin loop of only two bases.
Write a function that verifies that a list of base pairs (as outputted by dotparen_to_bp()) satisfies the hairpin requirement.
d) Now write your validator function. The function definition should look like this:
def rna_ss_validator(seq, sec_struc, wobble=True):

It should return True if the sequence is commensurate with a valid secondary structure and False otherwise. The wobble keyword argument is True if we allow wobble pairs (G paired with U). Here are some expected results:
Returns True:
rna_ss_validator('GCAUCUAUGC', '(((....)))')
rna_ss_validator('GCAUCUAUGU', '(((....)))')
rna_ss_validator('GCAUCUAUGU', '(.(....).)')

Returns False:
rna_ss_validator('GCAUCUACGC', '(((....)))')
rna_ss_validator('GCAUCUAUGU', '(((....)))', wobble=False)
rna_ss_validator('GCAUCUAUGU', '(.(....)).')
rna_ss_validator('GCCCUUGGCA', '(.((..))).')
'''
