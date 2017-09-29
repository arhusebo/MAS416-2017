import matplotlib.pyplot as plt

R = 20
L = 4
C = .0025

TIME_DURATION = 3
TIME_DELTA = .0001
REPORT_INTERVAL = 10

time = 0
reportCounter = REPORT_INTERVAL

v = 0
vDot = 12/.5
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
    if v <= 12:
        v += vDot * TIME_DELTA
    else:
        v = 12
    i += iDot * TIME_DELTA

plt.plot(timeData, iData)
plt.grid()
plt.show()
