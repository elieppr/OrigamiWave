import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import least_squares

def generate(angle):
    a = angle * math.pi / 180
    A = math.tan(a)
    DD = A**4 - 4*A**3 + 6*A**2 - 4*A + 5
    XFN = -(-A**4 + 2*A**3 - 4*A**2 + 2*A - 3)
    YFN = -(A**4 - 2*A**3 - 2*A - 1)
    return XFN / DD, YFN / DD

# --- Data Preparation ---
anglesDegree = [5, 8, 10, 12, 15, 20, 22.5, 25, 28, 30, 32, 35, 38, 40]
points = np.array([generate(a) for a in anglesDegree])
X, Y = points[:, 0], points[:, 1]

# --- Circle Fitting Logic ---
def calc_dist(params, x, y):
    """Calculate the distance of each point from the circle defined by params."""
    xc, yc, R = params
    return np.sqrt((x - xc)**2 + (y - yc)**2) - R

# Initial guess: center at mean of points, radius as distance to first point
x_m, y_m = np.mean(X), np.mean(Y)
initial_guess = [x_m, y_m, np.sqrt((X[0]-x_m)**2 + (Y[0]-y_m)**2)]

# Optimize
result = least_squares(calc_dist, initial_guess, args=(X, Y))
xc_fit, yc_fit, R_fit = result.x

# --- Error Calculation ---
distances = np.sqrt((X - xc_fit)**2 + (Y - yc_fit)**2)
residuals = distances - R_fit
sse = np.sum(residuals**2)
mse = np.mean(residuals**2)

print(f"Circle Center: ({xc_fit:.4f}, {yc_fit:.4f})")
print(f"Circle Radius: {R_fit:.4f}")
print(f"Sum of Squared Errors (SSE): {sse:.10f}")

# --- Plotting ---
plt.figure(figsize=(8, 8)) # Square aspect ratio for a circle

# 1. Data Points
plt.scatter(X, Y, color='blue', label='Data Points', zorder=5)

# 2. Plot the fitted Circle
theta = np.linspace(0, 2*np.pi, 200)
x_circle = xc_fit + R_fit * np.cos(theta)
y_circle = yc_fit + R_fit * np.sin(theta)
plt.plot(x_circle, y_circle, color='red', linewidth=2, label='Circle Fit')

# 3. Plot Center and Origin
plt.scatter(xc_fit, yc_fit, color='black', marker='+', s=100, label='Circle Center')
plt.scatter(0, 0, color='green', marker='x', label='Origin (0,0)')

# Formatting
plt.title("Origami Waves: Circle Fit Analysis")
plt.xlabel("XF")
plt.ylabel("YF")
plt.axis('equal') # Vital to make the circle look like a circle
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.show()