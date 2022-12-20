import numpy as np  
import math  
from timeit import Timer

# Calculate the distance between two points  
def CalculateDistanceBetweenTwoPoints(p1, p2):  
    distance = math.sqrt((p1[0] + p2[0]) ** 2 + (p1[1] + p2[1]) ** 2)
    #print("Distance of {p1} and {p2}: \n".format(p1 = p1,p2 = p2) + str(distance))

    return distance  
      
# Find the closest pairs between two points  
def FindClosestPairs(P, m):  
    closestPairs = {}
    
    # Variables for testing
    test_i_loop = 0
    test_j_loop = 0
    
    for i in range(len(P)):  
        minDistance = float("inf") # assign max float number for comparison 
        test_i_loop += 1
        for j in range(0,len(P)):
            test_j_loop += 1
            # don't calculate distance of self
            if(i != j):
                dist = CalculateDistanceBetweenTwoPoints(P[i], P[j])
                
                # if minDistance is greater than distance, assign the distance to minDistance
                if(minDistance > dist):  
                    minDistance = dist
                    
                    # Use minPair variable to store the minimum distance pairs
                    minPair = []  
                    minPair.append((P[i], P[j]))  
              
        # Append the minimum distance to closest pairs dictionary 
        closestPairs[minDistance] = minPair  
      
    # Sort the pairs in closestPairs using TimSort  
    closestPairs = dict(sorted(closestPairs.items()))  
    print("\nSorted Closest Pairs are: \n" + str(closestPairs))
    
    resultDistance = []
    resultPairs = []
    
    # Variable for testing
    test_k_loop = 0
    for k in range(0,m):
        test_k_loop += 1
        resultDistance.append(list(closestPairs.keys())[k])  
        resultPairs.append(list(closestPairs.values())[k])  
    
    # Print testing variable result
    print("\nTesting variables\n")
    print("\n i loop count: " + str(test_i_loop))
    print("\n j loop count: " + str(test_j_loop))
    print("\n k loop count: " + str(test_k_loop))
        
    return resultDistance, resultPairs
   
# Execute the Find Closest Pairs from Main function
def main():
     # Input size of points  
    n = 4000

    # Set of points in 2D plane - Use numpy to randomly generate [x,y] points  
    P = np.random.rand(n, 2)  
    print("\nPoints Are: \n" + str(P))  

    # Number of closest pairs to find in a list of vector points.  
    m = 8
    
    # Handle exceptions
    # if m is larger than n, throw an error
    if m > n:
        raise Exception("Error: m can't be greater than the input size n")
        
    closeDistance,closePairs = FindClosestPairs(P, m)
    print("\nClosest Distance Are: \n" +  str(closeDistance))  
    print("\nClosest Pairs Are: \n" + str(closePairs))
    

    print("\nExecution Time is \n")

# Use timer to track the executime time
if __name__=='__main__':
    t = Timer("main()", "from __main__ import main")
    print(t.timeit(1))