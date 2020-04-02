# Name: Vicky Yang
# Project 2, Step 2 & 3


import numpy as np
import matplotlib.pyplot as plt


# FUNCTIONS
def openckdfile():
# This function opens and reads the training set and normalizes 
# the value of the data.
# This function does not take any arguments.
# Returns three values: normalized glucose and hemoglobin values and 
# classification.
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
#   Normalizing Data
    glucose_scaled = (glucose - 70)/(490-70)
    hemoglobin_scaled = (hemoglobin - 3.1)/(17.8-3.1)
    return glucose_scaled, hemoglobin_scaled, classification

def graphData(glucose, hemoglobin, classification):
# This function graphs the Chronic Kidney Disease training set with glucose on
# the y-axis and the hemoglobin on the x-axis.
# Takes three arguments: normalized glucose values, normalized hemoglobin values
# and classification
# No return value
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.title('Chronic Kidney Disease Training Set')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

def createTestCase():
# This function creates test case by generating two random numbers between 0
# and 1 with one for glucose and the other for hemoglobin.
# There are no arguments.
# The return values are the test case (new_hemoglobin and new_glucose)
    new_glucose = np.random.rand()
    new_hemoglobin = np.random.rand()
    return new_hemoglobin, new_glucose

def calculateDistanceArray(new_glucose, new_hemoglobin, glucose, hemoglobin):
# This function calculates the distance between the test case and all the other
# points in the training set and forms a distance array.
# Takes four arguments: new_glucose and new_hemoglobin (the test case), normalized
# values for glucose and hemoglobin from the training set
# Returns the distance array
    distances = np.sqrt((hemoglobin - new_hemoglobin)**2 + (glucose - new_glucose)**2)
    return distances

def nearestNeighborClassifier(new_glucose, new_hemoglobin, glucose, hemoglobin, classification):
# This function calls the calculateDistanceArray function and finds the index of
# the minimum distance in the array (implementing nearest neighbor classifer). 
# The class of the nearest point is then found.
# Takes five arguments: new_glucose adn new_hemoglobin (the test case), normalized
# values for glucose and hemoglobin from training set, and the classifications
# Returns the classification of the nearest point to test case (0 or 1)
    distances = calculateDistanceArray(new_glucose, new_hemoglobin, glucose_scaled, hemoglobin_scaled)
    min_index = np.argmin(distances)
    nearest_class = classification[min_index]
    return nearest_class #returns logical 0 or 1

def graphTestCase(new_glucose, new_hemoglobin, glucose, hemoglobin, classificiation):
# This function graphs the Chronic Kidney Disease training set along with the 
# test case.
# Takes five arguments: normalized glucose values, normalized hemoglobin values,
# classification, the test case (new_hemoglobin and new_glucose)
# No return value
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot(new_hemoglobin, new_glucose,'g.', markersize=10)
    plt.title('Chronic Kidney Disease Nearest Neighbor Classifer')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

def kNearestNeighborClassifier(k, new_glucose, new_hemoglobin, glucose, hemoglobin, classificiation):
# This function implements the k-nearest neighbor classifer by calling on the 
# calculateDistanceArray function and sorting the indices of that array. k indices
# are used to classify the test case.
# Takes sic arguments: k (number of points to classify with), test case (new_glucose
# and new_hemoglobin), normalized values of glucose and hemoglobin, and classifcation
# Returns the classification of the test case
    distances = calculateDistanceArray(new_glucose, new_hemoglobin, glucose_scaled, hemoglobin_scaled)
    sorted_indices = np.argsort(distances)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    ckd = 0
    not_ckd = 0
    for i in k_classifications:
        if i == 1:
            ckd = ckd + 1
        elif i == 0:
            not_ckd = not_ckd + 1
    if ckd > not_ckd:
        return 'CKD'
    else: 
        return 'not CKD'

# MAIN SCRIPT

glucose_scaled, hemoglobin_scaled, classification = openckdfile()
new_hemoglobin, new_glucose = createTestCase()
graphData(glucose_scaled, hemoglobin_scaled, classification)
graphTestCase(new_glucose, new_hemoglobin, glucose_scaled, hemoglobin_scaled, classification)
k_classification = kNearestNeighborClassifier(3, new_glucose, new_hemoglobin, glucose_scaled, hemoglobin_scaled, classification)
