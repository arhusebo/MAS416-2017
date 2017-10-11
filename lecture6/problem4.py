import pandas
from numpy import matrix
from numpy.linalg import inv

dpath = "data/data.dat"
dcols = ['time', 'theta', 'thetadot', 'thetadotdot']

J = 2
phi_0 = 0
M_t = 0

data = pandas.read_csv(dpath, header=None, delim_whitespace=True, names=dcols)

X = matrix([data['theta'].as_matrix(), data['thetadot'].as_matrix()]).T
Y = -J*data['thetadotdot'].as_matrix()
b=inv(X.T@X)@X.T@Y

print('b={}, k={}'.format(round(b.item(1),1), round(b.item(0),1)))
