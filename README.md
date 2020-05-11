# EE-551 - Engineering Python

INSTRUCTIONS TO RUN THE PROGRAM

****************************************************************************************************************************************

The UAV’s initial position can be set as follows on x0, y0, and z0. 

The desired position of the UAV’s target can be set as follows by variables xr, yr, zr, zt.

Using this location and its initial position (x0, y0, z0), the quadcopter can calculate a target angle, theta, to use to find the
adjusted x and y values.

****************************************************************************************************************************************

The program can print the target [X, Y, Z, Yaw, Time] in real time as the UAV is conducting it’s flight. The ‘*’ is used to graph the 
position on the plot

print(target) will continuously print the UAV’s position throughout the 94 seconds. 

plt.plot(x, y, '*')	# X-Y Position (m) Viewed From Above

plt.plot(z, '*')	# Z position (m) vs Array Position

plt.plot(yaw, '*')	# Yaw Angle (rad) vs Array Position

plt.show()  # Show the plot

Each plt.plot() can be uncommented to provide the users desired plot
