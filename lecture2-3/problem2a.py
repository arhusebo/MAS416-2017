from utils import Vec2, Body
import math
import matplotlib.pyplot as plt

g = 9.81
m = 1200
J = 400
k = 300000
b = 25000
a = 1.6
h = 0.4
r = 0.4
STARTPOS_VEHICLE = Vec2(0, 0.4+h+r)

TIME_START = 0
TIME_DURATION = 5
TIME_DELTA = 0.001
REPORT_INTERVAL = 10

time = TIME_START
reportCounter = 10

# because the vehicle has no rotational inertia in this problem, the suspension forces are considered equal in A and B
# the value "suspesionForcePerWheel" (in simulation loop) is the force of one wheel
# the vehicle body has this value applied to its forces twice, once for each wheel
# this is the value that is plotted on the Y-axis

vehicle = Body(m, STARTPOS_VEHICLE)

timeData = []
forceData = []

def suspensionForce(k, b, delta, vel):
    return -k*delta+b*vel*math.sqrt(abs(delta))

while time < TIME_START + TIME_DURATION:
    # Apply forces
    vehicle.force.y = -g*vehicle.mass
    suspesionForcePerWheel = 0
    if vehicle.pos.y-h-r <= 0:

        suspesionForcePerWheel = suspensionForce(k, b, (vehicle.pos.y-h-r), -vehicle.vel.y)

    vehicle.force.y += 2*suspesionForcePerWheel

    # Update bodies
    vehicle.update(TIME_DELTA)

    if reportCounter == REPORT_INTERVAL:
        reportCounter = 0
        timeData.append(time)
        forceData.append(suspesionForcePerWheel)

    reportCounter += 1
    time += TIME_DELTA

plt.plot(timeData, forceData)
plt.grid()
plt.show()
