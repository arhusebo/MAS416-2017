import math
from scipy.optimize import fsolve
phi_1 = [0, math.pi/2, math.pi, 3*math.pi/2]
L_1 = 1
L_2 = 3
L_3 = 4
x_D = 3.5
y_D = -2

def psi(p, phi_1):
    x = L_1*math.cos(phi_1) + L_2*math.cos(p[0]) - L_3*math.cos(p[1]) - x_D
    y = L_1*math.sin(phi_1)+ L_2*math.sin(p[0]) - L_3*math.sin(p[1]) - y_D
    return x, y

phis = []

x0 = [math.pi*30/180,math.pi*90/180]

for phi in phi_1:
    sol = fsolve(psi, x0, args=phi)
    #for i in range(len(sol)):
    #    sol[i]*=180/math.pi
    #    sol[i]%=360
    phis.append(sol)

#for i, phi in enumerate(phis):
#    print(180*phi_1[i]/math.pi,phi)

#print(phis)
out = 'phi1 [deg]\tphi2 [deg]\tphi3 [deg]'
for i, pair in enumerate(phis):
    out += ('\n{}\t\t{}\t\t{}'.format(180/math.pi*phi_1[i], round((180/math.pi*pair[0])%360,2), round((180/math.pi*pair[1])%360),2))
print(out)
