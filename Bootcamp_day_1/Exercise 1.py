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

str_1 = 'ABCDEFGHIJKLMNAAAA'
str_2 = 'ABDEFGGHEFGHIJKLMN'
empty = ''
i = 0
j = 0
while str_1[i] == str_2[j]:
    print(str_1[i])
    j += 1
    i += 1


print(empty)