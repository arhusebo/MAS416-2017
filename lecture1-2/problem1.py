import math
import matplotlib.pyplot as plt

# General and excericise defined constants
G = 9.81
L = 0.7
TIME_START = 0
TIME_DURATION = 8
TIME_STEP = 0.001
PHI_START = math.pi/4
PHIDOT_START = 2
REPORT_INTERVAL = 10

# Program variables
time = TIME_START
phi = PHI_START
phiDot = PHIDOT_START
phiDotDot = 0
counter = REPORT_INTERVAL

# Data lists
timePlots = []
phiPlots = []

# Main simulation loop
while time < TIME_START + TIME_DURATION:
    # Calculate second derivatives
    phiDotDot = -G/L*math.sin(phi)
    # Append plot values every REPORT_INTERVAL
    if counter == REPORT_INTERVAL:
        counter = 0;
        timePlots.append(time)
        phiPlots.append(180*phi/math.pi)
    # Apply motion this iteration
    phi += phiDot * TIME_STEP
    phiDot += phiDotDot * TIME_STEP
    time += TIME_STEP
    counter += 1

# Plot data
plt.plot(timePlots, phiPlots)
plt.grid()
plt.show()
