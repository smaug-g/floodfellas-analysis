import matplotlib
import matplotlib.dates
import matplotlib.pyplot
import pickle
import numpy as np

with open('sensor_vals.pkl', 'rb') as f:
    saved_data = pickle.load(f)
    f.close()

with open('temp_vals.pkl', 'rb') as f:
    saved_temps = pickle.load(f)
    f.close()

    
date_nums = saved_data[0]
sensor_values = np.array(saved_data[1])
temp_values = np.array(saved_temps[1])

matplotlib.pyplot.plot_date(date_nums, sensor_values)
matplotlib.pyplot.plot_date(date_nums, temp_values)
matplotlib.pyplot.show()
