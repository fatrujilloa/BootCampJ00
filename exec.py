import  sys

s = ""
for i in range(1, len(sys.argv)):
    s = s + " " + sys.argv[i]
print (s[::-1])