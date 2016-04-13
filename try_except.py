__author__ = 'lyndsay.beaver'

# Try
# Except

userdefined = 'b'

try:
    a = int(userdefined)
except ValueError:
    a = int(1)
    print 'Error', str(a)
except Exception:
    a = int(0)
    print 'Error', str(a)
else: #finally:
    print a
