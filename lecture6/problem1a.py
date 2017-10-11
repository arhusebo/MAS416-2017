from numpy.linalg import solve

p = [64, 59, 55, 111]
labels = ['Apples', 'Oranges', 'Bananas', 'Grapes']
f = [[2,3,5,0], [8,1,0,1], [3,0,3,2], [6,8,1,1]]
ppf = solve(f, p)

for i in range(len(ppf)):
    print(labels[i],':',ppf[i])
