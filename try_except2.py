__author__ = 'lyndsay.beaver'

# Try
# Except

userdefined = 'b'

class MyException(Exception):
    pass

try:
    #a = int(userdefined)
    raise MyException('My Exception Error')
except ValueError:
    a = int(1)
    print 'Error', str(a)
except Exception as e:
    a = int(0)
    print 'Error', str(a), str(e)
except:
    print 'Error -1'
else:
    print a
