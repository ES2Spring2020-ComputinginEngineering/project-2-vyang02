#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions

k = 2
glucose, hemoglobin, classification = kmc.openckdfile() #opening file
glucose_scaled, hemoglobin_scaled, classification = kmc.normalizeData(glucose, hemoglobin, classification) #normalized values
centroid_array = kmc.select_random_centroid(k) #STEP 1: SELECT
distance_array = kmc.calculate_distance_array(k, centroid_array, hemoglobin_scaled, glucose_scaled) #STEP 2: ASSIGNMENT
min_indices_array = kmc.nearest_centroid_classification(k, distance_array) #STEP 2: ASSIGNMENT
mean_array = kmc.update_centroid(k,centroid_array, min_indices_array, hemoglobin_scaled, glucose_scaled) #STEP 3: UPDATE
final_centroid = kmc.iterate(100, k, centroid_array, distance_array, hemoglobin_scaled, glucose_scaled, hemoglobin, glucose) #STEP 4: ITERATE