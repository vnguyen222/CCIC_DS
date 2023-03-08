# Linear Regression Algorithm
# y = mx + b

import numpy as np

def LinearRegression(data, x, y):
    x = data[x].to_numpy()
    y = data[y].to_numpy()

    if np.size(x) != np.size(y):
        raise ValueError("x and y values are not equal")

    # sample size (n)
    sample_size_n = np.size(x)

    # mean of x and y
    mean_x, mean_y = np.mean(x), np.mean(y)

    # sum of squares / deviation about x
    SS_xy = np.sum(y * x) - sample_size_n * mean_y * mean_x
    SS_xx = np.sum(x * x) - sample_size_n * mean_x * mean_x
    
    m = SS_xy / SS_xx
    b = mean_y - m * mean_x

    return (m, b)





# Old Linear Regression Algorithm
'''
from math import sqrt

def sum_of_distances(x, y, df, b, m):
    total_distance = 0
    for index, row in df.iterrows():
        total_distance += abs(((m * df[x]) + b) - (df[y]))
    return total_distance


def MSE(df, b, m):
    sum = 0
    for index, row in df.iterrows():
        predicted = m * row["GPA"] + b
        actual = row["SAT"]
        sum += pow((predicted - actual),2)
    return sum

def RMSE(df, b, m):
    return sqrt(MSE(df, b, m))


def LinearRegression(data, x, y, initial_y_intercept, final_y_intercept, y_increment, initial_slope, final_slope, slope_increment):
    linear_equations = {}    # {b, m} : distance

    y_intercept = initial_y_intercept

    while y_intercept < final_y_intercept:
        slope = initial_slope
        while slope < final_slope:
            # dict_index = "[" + str(y_intercept) + "," + str(slope) + "]"
            # linear_equations[(dict_index)] = sum_of_distances(x, y, data, y_intercept, slope)
            linear_equations[(y_intercept, slope)] = sum_of_distances(x, y, data, y_intercept, slope)

            slope += slope_increment

        y_intercept += y_increment
    
    minimum = min(linear_equations)
'''
