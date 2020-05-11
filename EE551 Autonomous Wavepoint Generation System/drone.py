# pi is math.pi
# round is int(round(Value))
# need numpy to do matrices easier
# need matplotlib to make plots

# Need this for atan2
import math  # for most math functions
import numpy  # for arctan2 and matrices
import matplotlib.pyplot as plt  # for plotting
import time  # needed to count the time


# Drone Flight Path
# starting position
x0 = 1
y0 = 1
z0 = 0
# desired position and target
xr = 6
yr = 5
zr = 1  # to prevent skating
zt = 5  # top of object


# Heading
yaw0 = numpy.arctan2((yr-y0), (xr-x0))

# Radius of Target
R = 1

theta = numpy.arctan2((y0-yr), (x0-xr))

# Solving for adjusted x and y values
xAdj = xr + R*math.cos(theta)
yAdj = yr + R*math.sin(theta)

# from here i will be attempting to find the distances for the code
# first lets find define then D1 is there Dc is the since loop D2 is back
# L is the total distance of the travel

# Towards Target
D1 = math.sqrt((xAdj - x0)**2 + (yAdj - y0)**2 + (zr - z0)**2)

# Circular Path
Dc = 2*math.pi*R

# Back From Target
D2 = math.sqrt((xAdj - x0)**2 + (yAdj - y0)**2+(zr - z0)**2)

N = 2  # N is the number of rotations around the object

# Total Length
L = D1 + D2 + N*Dc

# now lets define the max speed, v, and the points per distance we want.
v = 0.25  # m/s
ppm = 20  # points/meter

# total points
Points = ppm*L  # points

# total time for the flight
totaltime = L/v  # seconds
# time to get to each point
timebtw = totaltime/Points

# Resolution
# to rise
t0 = 1
# To target
t1 = int(round(ppm*D1, 0))
# time to circle
t2 = int(round(ppm*Dc*N, 0))
# Return time
t3 = int(round(ppm*D2, 0))


# Circle calculation
omega = 2*math.pi/(t2/N)

# zeros matrix of 5 columns and t1+t2+t3 rows
waypoints = numpy.zeros((t1+t2+t3, 5))
# The new fifth column will be the time

# for loop only has a few small changes
# indexing starts at 0 not 1
for ii in range(0, t1+t2+t3):
    # To the target
    if ii < t1:
        waypoints[ii, 0] = (xAdj-x0)/t1*ii+x0
        waypoints[ii, 1] = (yAdj-y0)/t1*ii+y0
        waypoints[ii, 2] = zr
        waypoints[ii, 3] = yaw0
    # Around the target
    elif (t1 <= ii) and (ii < t1+t2):
        waypoints[ii, 0] = xr + R*math.cos(theta + omega*(ii-t1))
        waypoints[ii, 1] = yr + R*math.sin(theta + omega*(ii-t1))
        waypoints[ii, 2] = (zt-zr)/(t2)*(ii-t1)+zr
        waypoints[ii, 3] = (N*2*math.pi)/t2*(ii-t1)+yaw0
        # waypoints[ii,3] = waypoints[ii-1,3] + omega * timebtw
    # Coming Back
    else:
        waypoints[ii, 0] = (x0-xAdj)/(t3)*(ii-t1-t2)+xAdj
        waypoints[ii, 1] = (y0-yAdj)/(t3)*(ii-t1-t2)+yAdj
        waypoints[ii, 2] = (zr-zt)/(t3)*(ii-t1-t2)+zt
        waypoints[ii, 3] = yaw0 + N*2*math.pi
    waypoints[ii, 4] = timebtw*ii
ii+1


# Initialize the time and elapsed time
Start_Time = time.time()
Elapsed_Time = time.time() - Start_Time


def find_nearest(array, values):
    values = numpy.atleast_1d(values)
    indices = numpy.abs(numpy.subtract.outer(array, values)).argmin(0)
    out = array[indices]
    return out if len(out) > 1 else out[0]


# Finding the time, then going to the right line in the matrix
while Elapsed_Time < totaltime:
    Elapsed_Time = time.time() - Start_Time
    target_time = find_nearest(waypoints[:, 4], Elapsed_Time)
    position = int(round(target_time/timebtw, 0))
    target = waypoints[position, :]
    Elapsed_Time = Elapsed_Time = time.time() - Start_Time
    # DO NOT UNCOMMENT THE PRINT OR IT PRINT SEVERAL THOUSAND LINES
    # IF YOU WANT PROOF THAT THIS WORKS THEN CHANGE TOTALTIME
    # IN THE WHILE STATEMENT TO '3' THEN TEST
    print(target)


x = waypoints[:, 0]  # x values
y = waypoints[:, 1]  # y values
z = waypoints[:, 2]  # z values
yaw = waypoints[:, 3]  # yaw values

plt.plot(x, y, '*')  # X-Y Position (m) Viewed From Above
# plt.plot(z, '*')  # Z position (m) vs Array Position
# plt.plot(yaw, '*')  # Yaw Angle (rad) vs Array Position

plt.show()  # show the plot
