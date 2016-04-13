__author__ = 'lyndsay.beaver'

# Functions we will create:

#    - solve   --> Runs thru all possible combinations testing each for valid
#    - fill_in --> Create a new formula replacing letters with numbers
#    - valid   --> Tests our filled-in string

import re

def solve(rawFormula):
    """
    rawFormula = "SEND + MORE = MONEY"
    Test all possible translations between Character string and Numbered String
    Return the Solution to the puzzle or None is no solution is found.
    """
    ## Your code here
    pass

def valid(formula):
    """
    Formula is valid only if it has no leading zero on any of it's numbers
    and the formula evaluates as True.
    Returns True or False
    1/0 = 1 --> ERROR, Dividing by Zero
    """
    try:
        return not re.search(r'\b0[0-9]', formula) and eval(formula) is True
    except ArithmeticError:
        return False
    except:
        return False

print valid('1+1==2')
