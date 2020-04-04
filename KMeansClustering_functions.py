#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random


def openckdfile():
# This function opens and reads the training set.
# This function does not take any arguments.
# Returns three values: glucose, hemoglobin and classification
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
# This function normalizes the training set data.
# Takes three arguments: raw values for glucose and hemoglobin and classification
    glucose_scaled = (glucose - np.amin(glucose))/(np.amax(glucose)-np.amin(glucose))
    hemoglobin_scaled = (hemoglobin - np.amin(hemoglobin))/(np.amax(hemoglobin)-np.amin(hemoglobin))
    return glucose_scaled, hemoglobin_scaled, classification

def select_random_centroid(k):
    centroid_array = np.random.rand(k,2)
    return centroid_array

def calculate_distance_array(k, centroid_array, hemoglobin, glucose):
    distance_array = np.zeros((len(glucose),k))
    for i in range(k):
        distances = np.sqrt((hemoglobin - centroid_array[i,0])**2 + (glucose - centroid_array[i,1])**2)
        distance_array[:,i] = distances
    return distance_array

def nearest_centroid_classification(k, distance_array, hemoglobin, glucose):
    min_indices_array = np.argmin(distance_array, axis=1)
    return min_indices_array

def graphData(k, hemoglobin, glucose, min_indices_array, centroid_array):
    #unscale centroid
    
    plt.figure()
    for i in range(k):
        our_color = np.random.rand(3)
        unscaled_centroid_hemoglobin = (centroid_array[i, 0])*(np.amax(hemoglobin)-np.amin(hemoglobin)) + (np.amin(hemoglobin))
        unscaled_centroid_glucose = (centroid_array[i, 1])*(np.amax(glucose)-np.amin(glucose)) + (np.amin(glucose))
        plt.plot(hemoglobin[min_indices_array==i],glucose[min_indices_array==i], ".", label="Class" + ' ' + str(i), color=our_color)
        plt.plot(unscaled_centroid_hemoglobin, unscaled_centroid_glucose, "x", color=our_color)
    plt.title('Chronic Kidney Disease Training Set')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
        
def update_system(k, centroid_array, min_indices_array, hemoglobin, glucose):
    mean_array = np.zeros((k,2))
    for i in range(k):
        xmean = np.mean(hemoglobin[min_indices_array==i])
        ymean = np.mean(glucose[min_indices_array==i])
        mean_array[i,0] = xmean
        mean_array[i,1] = ymean
        centroid_array = mean_array
    return centroid_array
        
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose, hemoglobin, classification)
centroid_array = select_random_centroid(2)
distance_array = calculate_distance_array(2, centroid_array, hemoglobin_scaled, glucose_scaled)
min_indices_array = nearest_centroid_classification(2, distance_array, hemoglobin_scaled, glucose_scaled)
#mean_array = update_system(2,centroid_array, min_indices_array, hemoglobin_scaled, glucose_scaled)
graphData(2, hemoglobin, glucose, min_indices_array, centroid_array)