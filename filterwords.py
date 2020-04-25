import  sys

if len(sys.argv) != 3:
    sys.exit('ERROR')
s = sys.argv[1]
n = sys.argv[2]
x = '0'
try:
    x = int(s)
except:
    x = x
finally:
    if x != '0':
        sys.exit('ERROR')
try:
    n = int(n)
except:
    sys.exit('ERROR')
L = []
for w in s.split():
    if len(w) > n:
        L = L + [w]
print (L)
