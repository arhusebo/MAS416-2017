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
PHI1_START = math.pi*25/180
PHI2_START = math.pi*-25/180
PHI1DOT_START = 0
PHI2DOT_START = 0
REPORT_INTERVAL = 10

# Program variables
time = TIME_START
counter = REPORT_INTERVAL
extMomentum = 0

phi1 = PHI1_START
phi1Dot = PHI1DOT_START
phi1DotDot = 0

phi2 = PHI2_START
phi2Dot = PHI2DOT_START
phi2DotDot = 0

# Data lists
timePlots = []
phi1Plots = []
phi2Plots = []

# Function returning spring inertia
def spring(k, phi, phi0 = 0):
    return -k*(phi-phi0)

# Function returning damping inertia
def damper(b, omega, omega0 = 0):
    return b*(omega-omega0)

# Main simulation loop
while time < TIME_START + TIME_DURATION:
    # Calculate external forces: F = F_0 * sin(w * T)
    extMomentum = APPLIED_M * math.sin(MOMENTUM_FREQ * time)
    # Calculate forces and second derivatives
    netMomentum2 = extMomentum + spring(K, phi2, phi1) - damper(B, phi2Dot, phi1Dot)
    netMomentum1 = spring(K, phi1, phi2) - damper(B, phi1Dot, phi2Dot) + spring(K, phi1) - damper(B, phi1Dot)
    phi1DotDot = netMomentum1/J
    phi2DotDot = netMomentum2/J
    # Append plot values every REPORT_INTERVAL
    if counter == REPORT_INTERVAL:
        counter = 0
        timePlots.append(time)
        phi1Plots.append(180*phi1/math.pi)
        phi2Plots.append(180*phi2/math.pi)
    # Apply motion this iteration
    phi1 += phi1Dot * TIME_STEP
    phi1Dot += phi1DotDot * TIME_STEP
    phi2 += phi2Dot * TIME_STEP
    phi2Dot += phi2DotDot * TIME_STEP
    time += TIME_STEP
    counter += 1

# Plot data
plt.plot(timePlots, phi1Plots)
plt.plot(timePlots, phi2Plots)
plt.grid()
plt.show()
