import numpy as np

# BCM Task
# Read in dataset(s), implement K-Means Clustering to compute the best K for dataset,
#     and output Results.txt file with the dataset's name and estimated K for each dataset
# Input: [datasetName].txt
# Output: Results.txt

# Loading in dataset into a numpy table
# Input: Filename(if file in same folder as script) or File Location
# Returns numpy table
def loadDataSet(filename):
    with open(filename) as f:
        ncols = len(f.readline().split(' '))
    dataSet = np.loadtxt(filename, delimiter=' ')
    return dataSet

        
# Initializing K-means algorithms and performing comparisons for best K using the Silhouette method of comparing dissimilarities
# K will be grown using optimal initial centroids based on the converged values of (K-1) centroids until Silhouette values drop drastically (Chose 10% from the current max)
# Input: Numpy dataset with rows as samples and columns as features
def init_KMeans(dataset):
    if len(dataset.shape) > 1:
        # Initializing K comparisons by running K-means for k=1
        initCentroid = dataset[0]
        k = 1
        _, current_Centroid, assignments = general_KMeans(dataset, k, initCentroid, True)
        prev_Error = 0
        
        # Calculating distance table to be used for Silhouette Analysis later
        distance = calc_Distance(dataset)
        
        # Calculating Silhouette for K=1
        current_Silhouette = calc_Silhouette(assignments, distance)
        max_Silouette = current_Silhouette
        best_k = k
        
        # Grow the K clusters until Silhouette Value drops below 90% of the current MAX
        while (current_Silhouette == max_Silouette or current_Silhouette >= (0.90 * max_Silouette)) and k < dataset.shape[0]:   
            k += 1
            
            # Determining optimal initial centroids for current K
            initCentroid = opt_Initial_Clusters(dataset, k, current_Centroid)
            
            # Running K-Means with optimal centers at current K to obtain error, or Total Squared Distance
            _, _, assignments = general_KMeans(dataset, k, initCentroid, True)
            
            # Calculating new Silhouette Value
            current_Silhouette = calc_Silhouette(assignments, distance)
            if current_Silhouette > max_Silouette:
                max_Silouette = current_Silhouette
                best_k = k
            current_Centroid = initCentroid        
    else:   # If there is only 1 row in dataset
        best_k = 1
    
    return best_k
    
        
# Calculating distance table
# Input: Dataset
# Output: Distance table between each point
def calc_Distance(dataset):
    distance = np.zeros([dataset.shape[0], dataset.shape[0]])
    for row in range(dataset.shape[0]):
        for col in range(dataset.shape[0]):
            if row != col and distance[row, col] == 0:
                distance[row, col] = np.sqrt(np.sum((dataset[row] - dataset[col])**2))
                distance[col, row] = distance[row, col]  # Mirror to save time
    return distance
    
# General K-means algorithm
# Input: Numpy dataset, cluster amount, Numpy centroid values with row as centroid and columns as features, Boolean silhouette
# Return: [Error as represented by the Squared Distance Total, Centroid Centers]
#         If Silhouette is True, returns assignment table for silhouette Analysis
def general_KMeans(dataset, k, centroids, silhouette):    
    # Initializing assignment matrices and centers
    assignment_m = np.full(dataset.shape[0], -1)    # Cluster assignments for each point at iteration m
    assignment_Centers = np.zeros([dataset.shape[0], dataset.shape[1]])     # Store Centroid values for each dataset row
    updatedCenters = np.copy(centroids)
    distance = np.zeros(k)
    totalSquaredDist = 0    # Used to calculate error of clusters
    change = True
    
    # K-Means iteration until convergence
    while change:
        change = False
        totalSquaredDist = 0 # Resetting error
        counter = np.zeros(k)
        temp = np.zeros(updatedCenters.shape)
        
        # Iterating through dataset rows for centroid assignment
        for row in range(assignment_m.shape[0]):
            # Calculating distance of sample row (Squared Euclidean Distance)
            # For each cluster, calculating (C_jl - X_il)^2, where i is the current dataset row, 
            #     j is current cluster row, and l is the column
            distMatrixSquared = (updatedCenters - dataset[row])**2      
            
            # Assigning centers
            if len(distMatrixSquared.shape) == 2:   # Multiple clusters calculated
                distance = np.sum(distMatrixSquared, 1)     # Array of sums for each row
                assignment = np.where(distance == min(distance))[0]     # Row assigned to centroid labeled by index
                totalSquaredDist += min(distance)   # Summing total squared distance for error calculations
            else:   # There's only one cluster
                assignment = np.array([0]) 
                totalSquaredDist += np.sum(distMatrixSquared)   # Summing error for k=1
                
            # Detecting change to determine convergence
            if assignment[0] != assignment_m[row]:
                assignment_m[row] = assignment[0]
                change = True   
            assignment_Centers[row] = updatedCenters[assignment[0]]    
            
            # Summing to update centers by adding to a temp 
            if len(temp.shape) == 2:
                temp[assignment[0]] = temp[assignment[0]] + dataset[row]
            else:
                temp = temp + dataset[row]
            counter[assignment[0]] += 1     # Counting population of centroid
            
        # Updating centers by averaging (temp sum / counter)
        for centerIndex in range(k):
            if counter[centerIndex] != 0:
                if len(updatedCenters.shape) == 2:
                    updatedCenters[centerIndex] = temp[centerIndex] / counter[centerIndex]
                else:
                    updatedCenters = temp / counter[centerIndex]
    
    if silhouette:
        return totalSquaredDist, updatedCenters, assignment_m
    else:
        return totalSquaredDist, updatedCenters

# Optimizing Initial Centroid by using converged values of (K-1) centroids + allowing each row to act as the last centroid
# Input: Dataset, k, (K-1) centroids
# Return: The converged values with the least Total Squared Distance as error will be returned
def opt_Initial_Clusters(dataset, k, prev_Centroids):
    if k == 2:
        prev_Centroids = np.array([prev_Centroids])
    min_Error = 10000000000000000000.0
    current_Error = 0
    
    # Iterating through each row in dataset
    for row in range(len(dataset)):
        centers = np.append(prev_Centroids, [dataset[row]], axis=0)     # Current initial centroids with dataset[row]
        current_Error, temp_Centers = general_KMeans(dataset, k, centers, False)   # Run K-Means
        
        # Comparing Error to current minimum Error to update new centers
        if min_Error > current_Error:
            min_Error = current_Error
            final_Centers = temp_Centers
            
    return final_Centers
        
# Calculating Silhouette Value to determine dissimilarities between clusters using s(i) = (b(i) - a(i))/max{a(i), b(i)}
#     where a(i) is the average distance between point i and all other points in the same cluster, and 
#     b(i) is the minimum value between clusters of the average distance between point i and all points in a different cluster
# Input: point assignments, distance table
# Return: Means Silhouette Value
def calc_Silhouette(assignments, distance):
    # Initializing tables
    a_i = np.zeros(distance.shape[0])
    b_i = np.zeros(distance.shape[0])
    s_i = np.zeros(distance.shape[0])
    
    for row in range(distance.shape[0]):
        counter_a = 0       # Counter for Same cluster
        counter_b = np.zeros(np.max(assignments) + 1)       # Counter for cluster at index j, uses maximum value in assignments which is k-1 due to index value
        temp_b = np.zeros(np.max(assignments) + 1)
        for col in range(distance.shape[0]):
            if row != col:
                if assignments[row] == assignments[col]:    # Same cluster -> a(i) calculations
                    a_i[row] += distance[row, col]          # Summing distance of points in same cluster as [row]
                    counter_a += 1
                else:   # Different cluster
                    temp_b[assignments[col]] +=  distance[row, col]     # Summing distance for [col]'s cluster
                    counter_b[assignments[col]] += 1
        
        # Averaging a and b
        if counter_a != 0:
            a_i[row] = a_i[row] / counter_a
        for b in range(len(counter_b)):
            if counter_b[b] != 0:
                temp_b[b] = temp_b[b] / counter_b[b]
        if np.sum(temp_b) != 0:
            b_i[row] = np.min(temp_b[np.nonzero(temp_b)])       # Assigning min cluster b value to b_i
        
        s_i[row] = (b_i[row] - a_i[row]) / np.max([a_i[row], b_i[row]])
    
    # Averaging s(i) values
    return np.mean(s_i)
                

# Running K-means package script
# Input: List of filenames or locations, Filename or location of output text file
# Prints results to a text file delimited by tab by line:
#     "...\[Filename]\tk=[k]"
def run_KMeans(filenames, output):
    if isinstance(filenames, list):
        try:
            outputFile = open(output, 'w')
            for file in filenames:
                try:
                    print("Finding best k for", file)
                    # Input dataset file
                    dataset = loadDataSet(file)
                    
                    # Running K-means on dataset
                    best_k = init_KMeans(dataset)
                    
                    # Writing results to file
                    outputFile.write(file + "\tk=" + str(best_k) + "\n")
                except Exception as e:
                    print("Error has occured while opening or reading dataset for", file)   
            outputFile.close()
        except:
            print("Error in opening output file")
    else:
        print("Error: First argument requires a list.")
        
