from numpy import array, matrix, ones
from numpy.linalg import inv

# Estimate the constants of an n'th degree polynomial through regression
def get_estimates(x, y, n):
    X=matrix(array([x**i for i in range(n+1)])).T
    return inv(X.T@X)@X.T@y

# Prints a y-expression using matrix b containing constants for n'th degree polynomial
def print_y(b):
    s='y='
    for i in range(b.size):
        s+=(i>0)*'+'+str(round(b.item(b.size-i-1),1))+(i<b.size-1)*'x'+(i<b.size-2)*('^'+str(b.size-i-1))
    print(s)

x = array(range(1,11))
y = array([10.9, 20.6, 37.1, 60.4, 90.5, 127.4, 171.1, 221.6, 278.9, 343])

print_y(get_estimates(x, y, 1))
print_y(get_estimates(x, y, 2))
