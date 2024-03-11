#distance.py
import random

def generate_distance_matrix(num_cities):
    if num_cities < 2:
        raise ValueError("Number of cities must be at least 2")
    # Generate a num_cities x num_cities matrix with random distances
    distance_matrix = [[random.randint(0, 100) if i != j else 0 for j in range(num_cities)] for i in range(num_cities)]

    for row in distance_matrix:
        print(row)

    return distance_matrix