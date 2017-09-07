import math
import matplotlib.pyplot as plt
from utils import Vec2

G = 9.81
r = 0.05
m = 1.2
k = 7000
b = 150
START_POS = Vec2(r, r)
START_VEL = Vec2(2, 0)
START_ACCEL = Vec2(0, 0)
START_FORCE = Vec2(0, 0)
TIME_START = 0
TIME_DURATION = 5
TIME_DELTA = 0.0001
REPORT_INTERVAL = 10

ballPos = START_POS
ballVel = START_VEL
ballAccel = START_ACCEL

time = TIME_START
reportCounter = 10

xData = []
yData = []

def bounceForce(k, b, stretch, vel):
    return k*abs(stretch)-b*vel*math.sqrt(abs(stretch))

while time < TIME_START + TIME_DURATION:
    forces = Vec2(0, -G*m)
    if ballPos.x + r >= 3:
        forces += bounceForce(k, b, ballPos.x-(3-r), -ballVel.x) * Vec2(-1, 0)
    elif ballPos.x - r <= 0:
        forces += bounceForce(k, b, r-ballPos.x, ballVel.x) * Vec2(1, 0)
    if ballPos.y - r <= -3:
        forces += bounceForce(k, b, (-3+r)-ballPos.y, ballVel.y) * Vec2(0, 1)

    ballAccel = forces/m

    if reportCounter == REPORT_INTERVAL:
        reportCounter = 0
        xData.append(ballPos.x)
        yData.append(ballPos.y)

    ballPos += ballVel * TIME_DELTA
    ballVel += ballAccel * TIME_DELTA

    reportCounter += 1
    time += TIME_DELTA

plt.plot(xData, yData)
plt.grid()
plt.show()
