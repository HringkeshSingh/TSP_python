# NN.py
class NearestNeighbor:
    def __init__(self, distances):
        self.distances = distances
        self.num_cities = len(distances)

    def tsp_nearest_neighbor(self):
        path = [0]
        while len(path) < self.num_cities:
            current_city = path[-1]
            next_city = min((city for city in range(self.num_cities) if city not in path),
                            key=lambda city: self.distances[current_city][city])
            path.append(next_city)
        path.append(path[0])  # Return to starting city
        distance = sum(self.distances[path[i]][path[i+1]] for i in range(self.num_cities))
        return path, distance
