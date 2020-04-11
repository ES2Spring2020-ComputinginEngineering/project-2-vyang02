#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt


def openckdfile():
# This function opens and reads the training set.
# This function does not take any arguments.
# Returns three values: glucose, hemoglobin and classification
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
# This function normalizes the training set data.
# Takes three arguments: raw values for glucose and hemoglobin and classification
# Returns three values: the normalized values for glucose and hemoglobin along
# with the classification
    glucose_scaled = (glucose - np.amin(glucose))/(np.amax(glucose)-np.amin(glucose))
    hemoglobin_scaled = (hemoglobin - np.amin(hemoglobin))/(np.amax(hemoglobin)-np.amin(hemoglobin))
    return glucose_scaled, hemoglobin_scaled, classification

#STEP 1: SELECT
def select_random_centroid(k):
# This function generates k number of centroids for a set of data.
# Takes the one argument k (number of centroids)
# Returns k x k array with the centroid points
    centroid_array = np.random.rand(k,2)
    return centroid_array

# STEP 2: ASSIGNMENT
def calculate_distance_array(k, centroid_array, hemoglobin, glucose):
# The function calculates the distance between all the points and the centroid points.
# Takes four arguments: k(number of centroids), centroid array, normalized values
# for hemoglobin and glucose
# Returns the calculated distance_array
    distance_array = np.zeros((len(glucose),k))
    for i in range(k):
        distances = np.sqrt((hemoglobin - centroid_array[i,0])**2 + (glucose - centroid_array[i,1])**2)
        distance_array[:,i] = distances
    return distance_array

def nearest_centroid_classification(k, distance_array):
# The function takes the distance array and sorts the array by its indices.
# Takes four arguments: number of centroids and the distance array
# Returns an array of indices of the minimum distance
    min_indices_array = np.argmin(distance_array, axis=1)
    return min_indices_array

def graphData(k, hemoglobin, glucose, min_indices_array, centroid_array):
# The function graphs the assignment of data with their centroids (unnormalized
# the centroids)
# Takes five arguments: number of centroids, raw values for hemoglobin and glucose,
# min_indices_array, and the centroid_array
# No return values
    plt.figure()
    for i in range(k):
        our_color = np.random.rand(3)
        unscaled_centroid_hemoglobin = (centroid_array[i, 0])*(np.amax(hemoglobin)-np.amin(hemoglobin)) + (np.amin(hemoglobin))
        unscaled_centroid_glucose = (centroid_array[i, 1])*(np.amax(glucose)-np.amin(glucose)) + (np.amin(glucose))
        plt.plot(hemoglobin[min_indices_array==i],glucose[min_indices_array==i], ".", label="Class" + ' ' + str(i), color=our_color)
        plt.plot(unscaled_centroid_hemoglobin, unscaled_centroid_glucose, "x", markersize = 10, color=our_color)
    plt.title('Chronic Kidney Disease Training Set')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
# STEP 3: UPDATE   
def update_centroid(k, centroid_array, min_indices_array, hemoglobin, glucose):
# The function takes the mean of the assigned points to each centroid and
# makes the means the updated centroid point.
# Takes five arguments: number of centroids, centroid_array, min_indices_array,
# and the normalized hemoglobin and glucose values
# returns the updated centroid_array
    mean_array = np.zeros((k,2))
    for i in range(k):
        xmean = np.mean(hemoglobin[min_indices_array==i])
        ymean = np.mean(glucose[min_indices_array==i])
        mean_array[i,0] = xmean
        mean_array[i,1] = ymean
        centroid_array = mean_array
    return centroid_array

# STEP 4: ITERATE
def iterate(iterations, k, centroid_array, distance_array, hemoglobin_scaled, glucose_scaled, hemoglobin, glucose):
# The function iterates the updating of the centroids by using the updated centroid
# values to update the distance array which updates the min_indices_array and 
# cycles through.
# Takes eight arguments: number of iterations, k, centroid array, distance array,
# and the scaled and raw values for glucose and hemoglobin
# Returns the updated centroid value
    for i in range(iterations):
        distance_array = calculate_distance_array(k, centroid_array, hemoglobin_scaled, glucose_scaled)
        min_indices_array = nearest_centroid_classification(k, distance_array)
        centroid_array = update_centroid(k, centroid_array, min_indices_array, hemoglobin_scaled, glucose_scaled)
    graphData(k, hemoglobin, glucose, min_indices_array, centroid_array)
    return centroid_array