import matplotlib.pyplot as plt
from utils import Vec2

G = 9.81
r = 5
m = 1.2
START_POS = Vec2(0, 0)
START_VEL = Vec2(2, 0)
START_ACCEL = Vec2(0, 0)
TIME_START = 0
TIME_DURATION = 5
TIME_DELTA = 0.001
REPORT_INTERVAL = 10

time = TIME_START
reportCounter = 10

pos = START_POS
vel = START_VEL
accel = START_ACCEL

xData = []
yData = []

while time < TIME_START + TIME_DURATION:
    forces = Vec2(0, -G*m)
    accel = forces/m

    if reportCounter == REPORT_INTERVAL:
        reportCounter = 0
        xData.append(pos.x)
        yData.append(pos.y)

    vel += accel * TIME_DELTA
    pos += vel * TIME_DELTA

    reportCounter += 1
    time += TIME_DELTA

plt.plot(xData, yData)
plt.grid()
plt.show()
