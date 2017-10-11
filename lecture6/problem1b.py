from numpy.linalg import solve, LinAlgError

m = [365, 465, 1095]
labels = ['frigde', 'oven', 'washer']
e = [[2,3,1], [3,0,3], [6,9,3]]

try:
    mpe = solve(e, m)
    for i in range(len(mpe)):
        print(labels[i],':',mpe[i])
except LinAlgError:
    print('No unique solution')
