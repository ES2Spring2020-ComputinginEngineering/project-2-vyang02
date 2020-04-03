Name: Vicky Yang
ES2: Project 2 (Biomedical Data Analysis)

FILES
1. NearestNeighborClassification.py
2. KMeansClustering_functions.py
3. KMeansClustering_driver.py
4. ckd.csv

File 1: Algorithms and their functions

(1) Nearest Neighbor Classification

openckdfile() function
  This function opens and reads the training set.
  This function does not take any arguments.
  Returns three values: glucose, hemoglobin and classification
normalizeData(glucose, hemoglobin, classification)
  This function normalizes the training set data.
  Takes three arguments: raw values for glucose and hemoglobin and classification
graphData(glucose, hemoglobin, classification)
  This function graphs the Chronic Kidney Disease training set with glucose on the y-axis and the hemoglobin on the x-axis.
  Takes three arguments: normalized glucose values, normalized hemoglobin values and classification
  No return value
createTestCase()
  This function creates test case by generating two random numbers between 0 and 1 with one for glucose and the other for hemoglobin.
  There are no arguments.
  The return values are the test case (new_hemoglobin and new_glucose)
calculateDistanceArray(new_glucose, new_hemoglobin, glucose, hemoglobin)
  This function calculates the distance between the test case and all the other points in the training set and forms a distance array.
  Takes four arguments: new_glucose and new_hemoglobin (the test case), normalized values for glucose and hemoglobin from the 
  training set
  Returns the distance array
nearestNeighborClassifier(new_glucose, new_hemoglobin, glucose, hemoglobin, classification)
  This function calls the calculateDistanceArray function and finds the index of the minimum distance in the array (implementing nearest 
  neighbor classifer) to find the class of the nearest point.
  Takes five arguments: new_glucose and new_hemoglobin (the test case), normalized values for glucose and hemoglobin from training set, 
  and the classifications
  Returns the classification of the nearest point to test case (0 or 1)
graphTestCase(new_glucose, new_hemoglobin, glucose, hemoglobin, classificiation)
  This function graphs the training set along with the test case.
  Takes five arguments: normalized glucose values, normalized hemoglobin values, classification, the test case (new_hemoglobin and 
  new_glucose)
  No return value
  
(2) K-Nearest Classification

kNearestNeighborClassifier(k, new_glucose, new_hemoglobin, glucose, hemoglobin, classificiation)
  This function implements the k-nearest neighbor classifer by calling on the calculateDistanceArray function and sorting the indices of 
  that array. k indices are used to classify the test case.
  Takes six arguments: k (number of points to classify with), test case (new_glucose and new_hemoglobin), normalized values of glucose  
  and hemoglobin, and classifcation
  Returns the classification of the test case
  
(3) K-Means Clustering

File 2: Functions for File 3

File 3: Using the data from File 4 on Chronic Kidney Disease to implement K-Means Clustering Algorithm

File 4: The training set for the biomedical data analysis on Chronic Kidney Disease.

**This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).
