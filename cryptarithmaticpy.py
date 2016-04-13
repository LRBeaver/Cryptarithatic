__author__ = 'lyndsay.beaver'
## Cryptarithmetic   (aka Verbal arithmetic)
## The science and art of creating and solving cryptarithms.
## A cryptarithm is a genre of mathematical puzzle in which the
## digits are replaced by letters of the alphabet or other symbols.
## The world's best known alphametic puzzle is undoubtedly SEND + MORE = MONEY.
## It was created by H. E. Dudeney and first published in the July 1924 issue

## of Strand Magazine associated with the story of a kidnapper's ransom demand.

#      SEND         9567
#    + MORE       + 1085
#     -----        -----
#     MONEY        10652

# - Each letter or symbol represents only one digit throughout the problem;
# - When letters are replaced by their digits, the resultant arithmetical
#   operation must be correct;
# - The numerical base, unless specifically stated, is 10;
# - Numbers must not begin with a zero;
# - There must be only one solution to the problem.

# When hand solving you would first find all 0,1, and 9's. When you get stuck
# you would then do: --  generate-and-test

# original equation - String Characters [a-zA-Z]
# equation under test - String Numbers [0-9]
# letters
# numbers
# Table of Letters - Numbers
# Evaluating the string.


# 'SEND + MORE = MONEY'
#
# '1234 + 5672 = 86329' is this True
#
# {'s':'1'}

## Tools
# eval (evil)
# translate()

#print eval (1234 + 5672 = 86329)
#print 1234 + 5672

## string.maketrans(from, to)
##      Return a translation table suitable for passing to translate(),
##      that will map each character in from into the character at the
##      same position in to; from and to must have the same length.

## string.translate(s, table[, deletechars]) ***** Not In Python 3.x ******
##      Delete all characters from s that are in deletechars (if present),
##      and then translate the characters using table, which must be a
##      256-character string giving the translation for each character value,
##      indexed by its ordinal. If table is None, then only the character
##      deletion step is performed.


# import string
#
# table = string.maketrans('ABCDEF', '123456')
# print 'BED FACED'.translate(table)

import string

enc_table = string.maketrans('ABCDEF', 'ZXTRSF')
dec_table = string.maketrans('ZXTRSF', 'ABCDEF')

enc = 'BED FACED'.translate(enc_table)

print enc
dec = enc.translate(dec_table)
print dec





