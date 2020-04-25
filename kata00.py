import  sys

t = (19,42,21)
def format():
    print ('The %i numbers are' % len(t), *t)

format()