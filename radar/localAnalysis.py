import scipy as sp
import scipy.signal as signal
import matplotlib
import matplotlib.dates
import matplotlib.pyplot
import pickle
import numpy as np

with open('sensor_vals.pkl', 'rb') as f:
    saved_data = pickle.load(f)
    f.close()


    
date_nums = saved_data[0]
sensor_values = np.array(saved_data[1])[:,1:]
sensor_med = [np.median(x) for x in sensor_values]
med_med = signal.medfilt(sensor_med, [15])

#fs = 1/300
#bands =   [0, 1*fs/16, 2*fs/8, 3*fs/8] 
#desired = [1, 1,      0,      0]
#weight = [1, 1, 1, 1]

#filter_bs = signal.firls(201, bands, desired, fs=fs)
#filtered_values = signal.lfilter(filter_bs, [1], sensor_med)


fig = matplotlib.pyplot.figure()
fig.suptitle("2 weeks of Radar Data", fontsize=38)
matplotlib.pyplot.plot_date(date_nums, med_med, ls='-', ms=0)
matplotlib.pyplot.xlabel("Time (days)", fontsize=20)
matplotlib.pyplot.ylabel("Distance From Sensor to Target (mm)", fontsize=20)
#matplotlib.pyplot.plot_date(date_nums, sensor_values)
matplotlib.pyplot.show()
