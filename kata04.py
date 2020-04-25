import  sys

t = (0, 4, 132.42222, 10000, 12345.67)
def format():
    print ('day_%02i, ex_%02i : %.2f, %s, %s' % (t[0], t[1], t[2], "{:.2e}".format(t[3]), "{:.2e}".format(t[4]))) 

format()