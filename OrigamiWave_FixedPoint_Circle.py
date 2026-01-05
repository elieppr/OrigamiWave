import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

plt.figure()
def generate(angle, color, color2):
    a = angle * math.pi / 180

    # scale
    scale = 1-math.tan(a)

    # rotation matrix
    aa = math.cos(2*a)
    ab = -math.sin(2*a)
    ba = math.sin(2*a)
    bb = math.cos(2*a)
    tt = math.tan(a)
    R_a = np.array([[math.cos(2*a), -math.sin(2*a)], [math.sin(2*a), math.cos(2*a)]])

    # Translation
    A=math.tan(a)
    B=math.tan(2*a)

    XX = (A+2*A*A-A*A*A)/(1+A*A)
    YY = (-A+2*A*A+A*A*A)/(1+A*A)
    move = np.array([XX,YY])

    yN = (A*A+4*A+1)/(2*(1-A*A))
    xPy=4*A*A/(1+A*A)
    n_points = 100  # Number of points/iterations to plot

    # Initial points
    pointsx = [1]
    pointsy = [0]

    # Initial point to show the annotation
    X0 = 0
    Y0 = 0

    DD = A*A*A*A - 4*A*A*A + 6*A*A - 4*A + 5
    
    XFN = -(-A*A*A*A+2*A*A*A-4*A*A+2*A-3)
    
    YFN = -(A*A*A*A-2*A*A*A-2*A-1)

    XF = XFN/DD*1.0
    YF = YFN/DD*1.0

    XYF = XF + YF
    XYF2 = 4*(1+A*A)/((1-A)*(1-A)*(1-A)*(1-A)+4)
    print(f"XF: {XF} YF: {YF}")

    # Plot point - CHANGED c=color2 to c=color
    plt.scatter(XF, YF, c=color, s=10)

    # Plot points
    for x in range(len(pointsx)):

        for y in range(len(pointsy)):

            p = np.array([pointsx[x], pointsy[y]])

            for i in range(n_points):
                pprime = scale * R_a @ p + move  # Transformed point
                # set the another point to show the annotation
                if(X0==0 and Y0==0):
                    X0 = pprime[0]
                    Y0 = pprime[1]

                p = pprime
    # Add annotation
    plt.text(X0 + 0.02, Y0, f"angle: {angle:.1f}")

    return XF, YF

# angles in degrees
anglesDegree = [5, 10, 15, 20, 22.5, 30, 35, 40]

# This is the color list that will now be used for the data points
colors = [
    (1.0, 0, 0.0),
    (0.9, 0, 0.1),
    (0.8, 0, 0.2),
    (0.7, 0, 0.3),
    (0.6, 0, 0.4),
    (0.5, 0, 0.5),
    (0.4, 0, 0.6),
    (0.3, 0, 0.7),
    (0.2, 0, 0.8),
    (0.1, 0, 0.9),
    (0.0, 0, 1.0)
]

colors2 = [
    (1.0, 1, 0.0),
    (0.95, 1, 0.1),
    (0.9, 1, 0.1),
    (0.85, 1, 0.2),
    (0.8, 1, 0.1),
    (0.75, 1, 0.3),
    (0.7, 1, 0.1),
    (0.65, 1, 0.4),
    (0.6, 1, 0.1),
    (0.55, 1, 0.5),
    (0.5, 1, 0.1),
    (0.45, 1, 0.6),
    (0.4, 1, 0.1),
    (0.35, 1, 0.7),
    (0.3, 1, 0.1),
    (0.25, 1, 0.8),
    (0.2, 1, 0.1),
    (0.15, 1, 0.9),
    (0.1, 1, 0.1),
    (0.0, 1, 1.0)
]

points = []

# draw the waves for each angle
for angle in anglesDegree:
    # convert to angle from degrees to radians
    XF, YF = generate(angle, colors[anglesDegree.index(angle)], colors2[anglesDegree.index(angle)])  
    # Save the points in an array
    points.append((XF, YF))

# Convert the list to a numpy array if needed
points_array = np.array(points)


X = points_array[:, 0]  # All XF values (first column)
Y = points_array[:, 1]  # All YF values (second column)

# --- PLOT THE CIRCLE ---
# Equation: (x-2)^2 + y^2 = 2, so center is (2,0) and radius is sqrt(2)
center_h = 2.0
center_k = 0.0
radius = math.sqrt(2)

# Generate points for the circle using parametric equations
theta = np.linspace(0, 2 * np.pi, 200) # 200 points for a smooth circle
circle_x = center_h + radius * np.cos(theta)
circle_y = center_k + radius * np.sin(theta)

# Plot the circle
plt.plot(circle_x, circle_y, 'g--', label='Circle $(x-2)^2 + y^2 = 2$') # Green dashed line
# --- END OF NEW CODE ---


# --- MODIFIED PLOT SETTINGS ---
plt.title("Fixed Points of Different Folding Angles Forms a Circle")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.axis('equal')  # Ensures the circle is not distorted

# Adjust limits to make sure all plots are visible
plt.xlim(-0.5, 3.5)
plt.ylim(-1.5, 1.5)
# --- END OF MODIFIED SETTINGS ---


plt.show()