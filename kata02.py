import  sys

t = (3,30,2019,9,25)
def format():
    print ('%02i/%02i/%i %02i:%02i' % (t[3] % 12, t[4] % 31, t[2], t[0] % 24, t[1] % 60))
format()