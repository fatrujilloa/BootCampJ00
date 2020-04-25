import  sys, string

if len(sys.argv) == 1:
    print ("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit()
elif len(sys.argv) == 2:
    print ("Input error: too few arguments\n\nUsage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit()
elif len(sys.argv) > 3:
    print ("Input error: too many arguments\n\nUsage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit()
a = sys.argv[1]
b = sys.argv[2]
try:
    a = int(a)
    b = int(b)
except:
    print ("Input error: only numbers\n\nUsage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit()
op_names = ['Sum:', 'Difference:', 'Product:', 'Quotient:', 'Remainder:']
op_results = [str(a + b), str(a - b), str(a * b), str(a / b) if b != 0 else "ERROR (div by zero)", str(a % b) if b != 0 else "ERROR (modulo by zero)"]
for i in range(0, 5):
    print ('%-13s %s' % (op_names[i], op_results[i]))