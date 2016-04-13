__author__ = 'lyndsay.beaver'
import re
def noFirstZero(formula):
    ## formula is a string
    return not re.search(r'\b0[0-9]', formula)

def test_noFirstZero(L):
    for formula in L:
        print formula, noFirstZero(formula)

L = ['123','456','023','543 0453', '087 65', '00', '432 123']
test_noFirstZero(L)