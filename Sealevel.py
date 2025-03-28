import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

#Tehty DaBi-kurssia varten

def draw_plot():
    # Read data from file
    sea_lvl_data = pd.read_csv('epa-sea-level.csv')
    x = sea_lvl_data['Year']
    y = sea_lvl_data['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x,y)

    # Create first line of best fit
    f_value = linregress(x,y)
    slope = f_value.slope
    intercept = f_value.intercept
    extend = np.arange(min(x), 2051)
    plt.plot(extend, intercept + slope * extend, 'r', label='Sea Level Years 1880 - 2050')

    # Create second line of best fit
    new_sea_lvl_data = sea_lvl_data[sea_lvl_data['Year'] >= 2000]
    x_recent = new_sea_lvl_data['Year']
    y_recent = new_sea_lvl_data['CSIRO Adjusted Sea Level']
    s_value = linregress(x_recent,y_recent)
    slope_2 = s_value.slope
    intercept_2 = s_value.intercept
    extend_2 = np.arange(2000, 2051)
    plt.plot(extend_2, intercept_2 + slope_2 * extend_2, 'g', label='Sea Level Years 2000 - 2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
plt.show()