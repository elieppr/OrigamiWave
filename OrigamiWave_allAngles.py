import numpy as np
import matplotlib.pyplot as plt
import math

plt.figure()
def generate(angle, color):
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
    XX = A*(1+B)/(1+A*B)
    YY = (A-B+A*B+A*A*B)/(1+A*B)
    move = np.array([XX,YY])

    # Graph parameters
    n_points = 100  # Number of points/iterations to plot

    # Initial points
    pointsx = [1]
    pointsy = [0]

    # Initial point to show the annotation
    X0 = 0
    Y0 = 0

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

                # Plot point
                plt.scatter(pprime[0], pprime[1], c=color, s=10)  # Plot point
                # Plot line connecting consecutive points
                plt.plot([p[0], pprime[0]], [p[1], pprime[1]], 'k-', linewidth=1.2, color = color)
                plt.axis('equal')
                p = pprime
    # Add annotation
    plt.text(X0 + 0.02, Y0, f"angle: {angle:.1f}")

# angles in degrees
anglesDegree = [5, 10, 15, 20, 22.5, 30, 35, 40]

# colors for each angle
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
    (0.1, 0, 0.9),
    (0.1, 0, 0.9),
    (0.0, 0, 1.0)
]

# draw the waves for each angle
for angle in anglesDegree:
    # convert to angle from degrees to radians
    generate(angle, colors[anglesDegree.index(angle)])

# Set axis limits
plt.xlim([0, 1.2])
plt.ylim([0, 1])

# Configure axes
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Add grid and title
plt.grid(True)
#plt.title("Phase Portrait with Adjusted Arrow Scaling")
plt.title("Origami Waves With Different Folding Angles")
plt.xlabel("X-axis", loc='right')
plt.ylabel("Y-axis", loc='top')
plt.show()
