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


    
date_nums = np.array(saved_data[0])
sensor_values = np.array(saved_data[1])[:,1:]
sensor_med = np.array([np.median(x) for x in sensor_values])

data_start = 2500
interesting = sensor_med[data_start:]
date_nums = date_nums[data_start:] - date_nums[data_start]

med_med = signal.medfilt(interesting, [9])
med_mean = np.mean(med_med)
med_med = (-med_med + med_mean)
cloud = (-sensor_values[data_start:,:] + med_mean)

#fs = 1/300
#bands =   [0, 1*fs/16, 2*fs/8, 3*fs/8] 
#desired = [1, 1,      0,      0]
#weight = [1, 1, 1, 1]

#filter_bs = signal.firls(201, bands, desired, fs=fs)
#filtered_values = signal.lfilter(filter_bs, [1], sensor_med)


fig = matplotlib.pyplot.figure()
fig.suptitle("Radar Data", fontsize=38)
#matplotlib.pyplot.plot_date(date_nums, med_med, ls='-', ms=0)
matplotlib.pyplot.plot(date_nums, cloud,'go', ms=3, ls='', alpha = 0.1)
matplotlib.pyplot.plot(date_nums, med_med, '-b', ls='-', ms=0)
matplotlib.pyplot.xlabel("Time (days)", fontsize=20)
matplotlib.pyplot.ylabel("Change in Water Height (mm)", fontsize=20)
matplotlib.pyplot.minorticks_on()
matplotlib.pyplot.xticks(fontsize=16)
matplotlib.pyplot.yticks(fontsize=16)
matplotlib.pyplot.grid(b=None, which='both', axis='both')
#matplotlib.pyplot.plot_date(date_nums, sensor_values)
matplotlib.pyplot.show()
