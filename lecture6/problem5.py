from scipy.optimize import minimize

def objective(x):
    return (x[0]-5)**2 + (x[1]-8)**2 + 7

def constraint_b(x):
    return 12-2.4*x[0]-x[1] # >= 0

def constraint_c(x):
    return x[1]-x[0] # = 0

x0 = [1,1]

con_b = {'type': 'ineq', 'fun': constraint_b}
con_c = {'type': 'eq', 'fun': constraint_c}

a = minimize(objective, x0)
b = minimize(objective, x0, constraints=con_b)
c = minimize(objective, x0, constraints=con_c)

print('Using initial guess x={}, y={}'.format(x0[0], x0[1]))
print('a:\n\tx={}, y={}'.format(round(a.x[0], 2), round(a.x[1], 2)))
print('b:\n\tx={}, y={}'.format(round(b.x[0], 2), round(b.x[1], 2)))
print('c:\n\tx={}, y={}'.format(round(c.x[0], 2), round(c.x[1], 2)))
