import math
import matplotlib.pyplot as plt

# User defined constants
APPLIED_M = 0
MOMENTUM_FREQ = 0

# General and excericise defined constants
K = 1800
B = 8
J = 2
TIME_DURATION = 4
TIME_START = 0
TIME_STEP = 0.0001
PHI_START = math.pi*25/180
REPORT_INTERVAL = 10

# Program variables
time = TIME_START
counter = REPORT_INTERVAL
extMomentum = 0
phi = PHI_START
phiDot = 0
phiDotDot = 0

# Data lists
timePlots = []
phiPlots = []

# Function returning spring inertia
def spring(k, phi):
    return -k*phi

# Function returning damping inertia
def damper(b, v):
    return b*v

# Main simulation loop
while time < TIME_START + TIME_DURATION:
    # Calculate external forces: F = F_0 * sin(w * T)
    extMomentum = APPLIED_M * math.sin(MOMENTUM_FREQ * time)
    # Calculate forces and second derivatives
    totMomentum = extMomentum + spring(K, phi) - damper(B, phiDot)
    phiDotDot = totMomentum/J
    # Append plot values every REPORT_INTERVAL
    if counter == REPORT_INTERVAL:
        counter = 0
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
