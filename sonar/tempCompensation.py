import pickle
import matplotlib
import matplotlib.dates
import matplotlib.pyplot
from datetime import datetime
import math
import numpy

# read in pickle files
sensor_values = pickle.load( open( "sensor_vals.pkl", "rb" ) )
temp_values = pickle.load( open( "temp_vals.pkl", "rb" ) )

num_points = len(sensor_values[0])
print("Number of data points: " + str(num_points))

# Get current time and print
current_time = datetime.now()
current_date_num = matplotlib.dates.date2num(current_time)
print("Current time: " + str(current_time) + "\nEpoch time: " + str(current_date_num))

# Print timestamp of first data point
date_str = matplotlib.dates.num2date(sensor_values[0][0])
date_num = matplotlib.dates.date2num(date_str)
print("Time of first data point: " + str(date_str) + ", " + str(date_num))

# Print timestamp of most recent data point
date_str = matplotlib.dates.num2date(sensor_values[0][num_points-1])
date_num = matplotlib.dates.date2num(date_str)
print("Time of most recent data point: " + str(date_str) + ", " + str(date_num))

# Calibrate distance measurement based on temperature reading
calib_dist = []
for x in range(num_points):
	# formula based on speed of sound with temperature
	calib_dist.append(round((331.3*math.sqrt(1+(temp_values[1][x]/273.15)))*(numpy.median(sensor_values[1][x])/343.21)))

matplotlib.pyplot.plot_date(sensor_values[0], sensor_values[1])
matplotlib.pyplot.plot_date(temp_values[0], temp_values[1])
matplotlib.pyplot.plot_date(temp_values[0], calib_dist)
matplotlib.pyplot.show()