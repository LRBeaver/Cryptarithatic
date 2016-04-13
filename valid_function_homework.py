__author__ = 'lyndsay.beaver'

# Functions we will create:

#    - solve   --> Runs thru all possible combinations testing each for valid
#    - fill_in --> Create a new formula replacing letters with numbers
#    - valid   --> Tests our filled-in string

import re
import math

def valid(formula):
    """
    Formula is valid only if it has no leading zero on any of it's numbers
    and the formula evaluates as True.
    Returns True or False
    """
    try:
        def noFirstZero(formula):
        ## formula is a string
        return not re.search(r'\b0[0-9]', formula) and eval(formula) is True

    except ArithmeticError:
        return False ## your code here
    except:
        return False ## your code here

print valid('1+1==2')