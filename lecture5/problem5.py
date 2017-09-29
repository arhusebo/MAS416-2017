import matplotlib.pyplot as plt
import math

J = .005
V_p = 220
R_s = 2
R_r = 2.5
L_s = .025
L_r = 0.015
f_s = 50
M_fr = 3
OMEGA_fr = 20
P = 2

TIME_DURATION = 1
TIME_DELTA = .0001
REPORT_INTERVAL = 10

M_m = 0
omega_s = (2/P)*2*math.pi*f_s
omega_m = 0
omega_mDot = 0
s = 0

time = 0
reportCounter = REPORT_INTERVAL

torqueData = []
timeData = []

while time <= TIME_DURATION:

    s = (omega_s - omega_m) / omega_s
    M_L = M_fr * math.tanh(omega_m / OMEGA_fr)
    if not s == 0:
        M_m = (3 * R_r * V_p**2)/(s*omega_s*(((R_s+R_r/s)**2)+(omega_s**2)*(L_s+L_r)**2))
    omega_mDot = (M_m - M_L) / J

    if reportCounter == REPORT_INTERVAL:
        torqueData.append(M_m)
        timeData.append(time)
        reportCounter = 0

    reportCounter += 1
    time += TIME_DELTA

    omega_m += omega_mDot * TIME_DELTA

plt.plot(timeData, torqueData)
plt.grid()
plt.show()
