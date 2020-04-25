import  sys

if len(sys.argv) != 2:
    print ("ERROR")
    sys.exit()
n = sys.argv[1]
try:
    n = int(n)
except:
    sys.exit()
if n == 0:
    print ("I'm zero.")
elif n % 2 == 0:
    print ("I'm even.")
else:
    print ("I'm odd.")