import matplotlib.pyplot as plt
import math

R = 20
L = 4
C = .0025
V = 12
OMEGA = 5

TIME_DURATION = 5
TIME_DELTA = .0001
REPORT_INTERVAL = 10

time = 0
reportCounter = REPORT_INTERVAL

v = 0
vDot = 0
i = 0
iDot = 0
v_C = 0
v_CDot = 0

iData = []
timeData = []

while time <= TIME_DURATION:

    v_R = i * R
    v_L = v - v_R - v_C
    v_CDot = i / C
    iDot = v_L/L

    if reportCounter == REPORT_INTERVAL:
        iData.append(i)
        timeData.append(time)
        reportCounter = 0

    reportCounter += 1
    time += TIME_DELTA

    v_C += v_CDot * TIME_DELTA

    v = V * math.sin(OMEGA * time)
    i += iDot * TIME_DELTA

plt.plot(timeData, iData)
plt.grid()
plt.show()
