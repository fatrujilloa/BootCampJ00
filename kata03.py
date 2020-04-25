import  sys

phrase = "The right format"

def format():
    print ('%s' % phrase.rjust(42, '-'), end = '')

format()