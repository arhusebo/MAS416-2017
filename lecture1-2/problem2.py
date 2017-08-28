import math
import matplotlib.pyplot as plt

# User defined constants
APPLIED_F = 0
FORCE_FREQ = 0

# General and excericise defined constants
G = 9.81
K = 40000
C = 500
M = 100
TIME_DURATION = 2
TIME_START = 0
TIME_STEP = 0.0001
Y_START = 0
REPORT_INTERVAL = 10

# Program variables
time = TIME_START
counter = REPORT_INTERVAL
extForce = 0
y = Y_START
yDot = 0
yDotDot = 0

# Data lists
timePlots = []
yPlots = []

# Function returning spring force
def spring(k, x):
    return -k*x

# Function returning damping force
def damper(c, v):
    return c*v

# Main simulation loop
while time < TIME_START + TIME_DURATION:
    # Calculate external forces: F = F_0 * sin(w * T)
    extForce = APPLIED_F * math.sin(FORCE_FREQ * time)
    # Calculate forces and second derivatives
    totalForce = extForce - M * G + spring(K, y) - damper(C, yDot)
    yDotDot = totalForce/M
    # Append plot values every REPORT_INTERVAL
    if counter == REPORT_INTERVAL:
        counter = 0
        timePlots.append(time)
        yPlots.append(y)
    # Apply motion this iteration
    y += yDot * TIME_STEP
    yDot += yDotDot * TIME_STEP
    time += TIME_STEP
    counter += 1

# Plot data
plt.plot(timePlots, yPlots)
plt.grid()
plt.show()
