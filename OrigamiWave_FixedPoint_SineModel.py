import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit

def generate(angle):
    a = angle * math.pi / 180
    A = math.tan(a)
    # Translation constants and Fixed Point calculation
    DD = A**4 - 4*A**3 + 6*A**2 - 4*A + 5
    XFN = -(-A**4 + 2*A**3 - 4*A**2 + 2*A - 3)
    YFN = -(A**4 - 2*A**3 - 2*A - 1)
    return XFN / DD, YFN / DD

# --- Data Preparation ---
anglesDegree = [5, 8, 10, 12, 15, 20, 22.5, 25, 28, 30, 32, 35, 38, 40]
points = np.array([generate(a) for a in anglesDegree])
X = points[:, 0]
Y = points[:, 1]

# --- Sine Fitting Logic ---
# Function form: y = a * sin(b * x + c) + d
def sine_func(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

# Initial guesses are crucial for sine waves to avoid local minima
# a: amplitude, b: frequency, c: phase, d: offset
initial_guess = [1.0, 2.0, -1.0, 0.5]

# Optimize using curve_fit
popt, pcov = curve_fit(sine_func, X, Y, p0=initial_guess, maxfev=10000)
a_fit, b_fit, c_fit, d_fit = popt

# --- Error Calculation ---
Y_pred = sine_func(X, *popt)
residuals = Y - Y_pred
sse = np.sum(residuals**2)
mse = np.mean(residuals**2)

print(f"Sine Fit: y = {a_fit:.4f} * sin({b_fit:.4f} * x + {c_fit:.4f}) + {d_fit:.4f}")
print(f"Sum of Squared Errors (SSE): {sse:.10f}")
print(f"Mean Squared Error (MSE): {mse:.10f}")

# --- Plotting ---
plt.figure(figsize=(10, 7))

# 1. Plot the actual data points
plt.scatter(X, Y, color='blue', label='Data Points', zorder=5)

# 2. Plot the fitted sine curve
X_line = np.linspace(min(X), max(X), 200)
plt.plot(X_line, sine_func(X_line, *popt), color='red', linewidth=2, label='Sine Fit')

# 3. Add origin point (0,0) for reference
plt.scatter(0, 0, color='green', marker='x', label='Origin (0,0)')

# Formatting the plot
plt.title("Origami Waves: Sine Fit Analysis")
plt.xlabel("XF")
plt.ylabel("YF")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Set axis spines to cross at zero for visibility
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()