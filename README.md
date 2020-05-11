# EE-551 - Engineering Python
# Engineering Python

The program can print the target [X, Y, Z, Yaw, Time] in real time as the UAV is conducting it’s flight. The ‘*’ is used to graph the position on the plot

print(target) will continuously print the UAV’s position throughout the 94 seconds. 

plt.plot(x, y, '*')	# X-Y Position (m) Viewed From Above

plt.plot(z, '*')	# Z position (m) vs Array Position

plt.plot(yaw, '*')	# Yaw Angle (rad) vs Array Position

plt.show()  # Show the plot

Each plt.plot() can be uncommented to provide the users desired plot
