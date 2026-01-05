import numpy as np
import matplotlib.pyplot as plt
import math

def generate(angle):
    a = angle * math.pi / 180
    scale = 1 - math.tan(a)
    
    # Translation constants
    A = math.tan(a)
    XX = (A + 2*A**2 - A**3) / (1 + A**2)
    YY = (-A + 2*A**2 + A**3) / (1 + A**2)
    
    # Calculate Fixed Points (XF, YF)
    DD = A**4 - 4*A**3 + 6*A**2 - 4*A + 5
    XFN = -(-A**4 + 2*A**3 - 4*A**2 + 2*A - 3)
    YFN = -(A**4 - 2*A**3 - 2*A - 1)
    
    XF = XFN / DD
    YF = YFN / DD
    return XF, YF

# --- Data Preparation ---
anglesDegree = [5, 8, 10, 12, 15, 20, 22.5, 25, 28, 30, 32, 35, 38, 40]
# anglesDegree = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22.5, 25, 27.5, 30, 31, 32.5,33.5, 35, 36, 37.5, 38.5, 40, 42, 44]
points = []

for angle in anglesDegree:
    xf, yf = generate(angle)
    points.append((xf, yf))

points_array = np.array(points)
X = points_array[:, 0]
Y = points_array[:, 1]

# --- Polynomial Fitting ---
degree = 4
coeffs = np.polyfit(X, Y, degree)
poly = np.poly1d(coeffs)

# --- Error Calculation (Square of the Errors) ---
# Y_pred are the values on the red line
Y_pred = poly(X)
# residuals are the differences (errors)
residuals = Y - Y_pred
# SSE is the sum of the squares of these errors
sse = np.sum(residuals**2)
mse = np.mean(residuals**2)

print(f"Polynomial Degree: {degree}")
print(f"Sum of Squared Errors (SSE): {sse:.10f}")
print(f"Mean Squared Error (MSE): {mse:.10f}")

# --- Plotting ---
plt.figure(figsize=(10, 7))

# 1. Plot the actual data points
plt.scatter(X, Y, color='blue', label='Data Points', zorder=5)

# 2. Plot the fitted polynomial line
# We create a smooth range of X values for a cleaner curve
X_line = np.linspace(min(X), max(X), 200)
plt.plot(X_line, poly(X_line), color='red', linewidth=2, label=f'Fit (Polynomial Degree {degree})')

# 3. Add origin point (0,0) for reference
plt.scatter(0, 0, color='green', marker='x', label='Origin (0,0)')

# Formatting the plot
plt.title("Origami Waves: Polynomial Fit Analysis")
plt.xlabel("XF")
plt.ylabel("YF")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Adjusting axes to show (0,0) clearly
plt.xlim(0, max(X) * 1.1)
plt.ylim(min(Y) - 0.1, max(Y) * 1.1)

# Set axis spines to cross at zero
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()