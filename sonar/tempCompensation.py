import pickle
from scipy import signal
import matplotlib
import matplotlib.dates
import matplotlib.pyplot
from datetime import datetime
import math
import numpy as np

# read in pickle files
with open("sensor_vals.pkl", "rb") as f:
    saved_data = pickle.load(f)
    f.close()

with open("temp_vals.pkl", "rb") as f:
    saved_temp = pickle.load(f)
    f.close()

date_nums = saved_data[0]
sensor_values = np.array(saved_data[1])
temp_values = np.array(saved_temp[1])
temp_values = signal.medfilt(temp_values, [21])

sensor_med = [np.median(x) for x in sensor_values]
med_med = signal.medfilt(sensor_med, [21])

num_points = len(saved_data[0])
print("Number of data points: " + str(num_points))

# Get current time and print
current_time = datetime.now()
current_date_num = matplotlib.dates.date2num(current_time)
print("Current time: " + str(current_time) +
      "\nEpoch time: " + str(current_date_num))

# Print timestamp of first data point
date_str = matplotlib.dates.num2date(date_nums[0])
date_num = matplotlib.dates.date2num(date_str)
print("Time of first data point: " + str(date_str) + ", " + str(date_num))

# Print timestamp of most recent data point
date_str = matplotlib.dates.num2date(date_nums[-1])
date_num = matplotlib.dates.date2num(date_str)
print("Time of most recent data point: " +
      str(date_str) + ", " + str(date_num))

# Calibrate distance measurement based on temperature reading
calib_dist = []
for x in range(num_points):
	# formula based on speed of sound with temperature
	calib_dist.append(round((331.3*math.sqrt(1+(temp_values[x]/273.15)))*(med_med[x])/343.21))

fig = matplotlib.pyplot.figure()
fig.suptitle("Sonar Distance from Sensor to Target", fontsize=38)
matplotlib.pyplot.plot_date(date_nums, med_med, ls='-', ms=0)
#matplotlib.pyplot.plot_date(date_nums, temp_values)
matplotlib.pyplot.xlabel("Time (days)", fontsize=20)
matplotlib.pyplot.ylabel("Distance (mm)", fontsize=20)
#matplotlib.pyplot.plot_date(date_nums, calib_dist, ls='-', ms=0)
matplotlib.pyplot.show()

