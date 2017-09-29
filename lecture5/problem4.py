import matplotlib.pyplot as plt
import math

J = .00025
V = 12
R = .4
L = .03
K = .1
M_fr = .2
OMEGA_fr = 20

TIME_DURATION = 2
TIME_DELTA = .0001
REPORT_INTERVAL = 10

omega_m = 0
omega_mDot = 0
i = 0
iDot = 0

time = 0
reportCounter = REPORT_INTERVAL

omega_mData = []
timeData = []

while time <= TIME_DURATION:

    M_L = M_fr * math.tanh(omega_m / OMEGA_fr)
    M_m = K * i
    omega_mDot = (M_m - M_L) / J
    iDot = (V-R*i-K*omega_m)/L

    if reportCounter == REPORT_INTERVAL:
        omega_mData.append(omega_m)
        timeData.append(time)
        reportCounter = 0

    reportCounter += 1
    time += TIME_DELTA

    omega_m += omega_mDot * TIME_DELTA
    i += iDot * TIME_DELTA

plt.plot(timeData, omega_mData)
plt.grid()
plt.show()
