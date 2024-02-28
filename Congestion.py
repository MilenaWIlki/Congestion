def calculate_traffic_congestion_probability(num_cars, road_capacity):
    return min(num_cars / road_capacity, 1)

# Example usage:
num_cars = 50
road_capacity = 60
congestion_probability = calculate_traffic_congestion_probability(num_cars, road_capacity)
print("Probability of traffic congestion:", congestion_probability)
