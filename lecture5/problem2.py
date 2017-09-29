import matplotlib.pyplot as plt

R = 200
C = .00006


TIME_DURATION = .5
TIME_DELTA = .0001
REPORT_INTERVAL = 10

time = 0
reportCounter = REPORT_INTERVAL

v = 0
vDot = 12/.3
i_1 = 0
i_1Dot = 0
i_2 = 0
i_2Dot = 0
v_C = 24
v_CDot = 0

i_1Data = []
i_2Data = []
v_CData = []
timeData = []

while time <= TIME_DURATION:

    i_1 = v / R
    i_2 = (v - v_C) / R
    v_CDot = i_2 / C

    if reportCounter == REPORT_INTERVAL:
        i_1Data.append(i_1)
        i_2Data.append(i_2)
        v_CData.append(v_C)
        timeData.append(time)
        reportCounter = 0

    reportCounter += 1
    time += TIME_DELTA

    v_C += v_CDot * TIME_DELTA
    if v <= 12:
        v += vDot * TIME_DELTA
    else:
        v = 12
    i_1 += i_1Dot * TIME_DELTA
    i_2 += i_2Dot * TIME_DELTA

plt.plot(timeData, i_1Data)
plt.plot(timeData, i_2Data)
#plt.plot(timeData, v_CData)
plt.grid()
plt.show()
