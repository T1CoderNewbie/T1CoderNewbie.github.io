import itertools

# Define distances between cities (in kilometers)
distances = {
    ('Ho Chi Minh', 'Da Nang'): 964,
    ('Ho Chi Minh', 'Dalat'): 308,
    ('Ho Chi Minh', 'Nha Trang'): 435,
    ('Ho Chi Minh', 'Hai Phong'): 1640,
    ('Ho Chi Minh', 'Hanoi'): 1710,
    ('Da Nang', 'Dalat'): 659,
    ('Da Nang', 'Nha Trang'): 530,
    ('Da Nang', 'Hai Phong'): 883,
    ('Da Nang', 'Hanoi'): 764,
    ('Dalat', 'Nha Trang'): 135,
    ('Dalat', 'Hai Phong'): 1702,
    ('Dalat', 'Hanoi'): 1542,
    ('Nha Trang', 'Hai Phong'): 1465,
    ('Nha Trang', 'Hanoi'): 1290,
    ('Hai Phong', 'Hanoi'): 120,
    ('Hai Phong', 'Ho Chi Minh'): 1640
}

# Function to get the distance between two cities
def get_distance(city1, city2):
    if (city1, city2) in distances:
        return distances[(city1, city2)]
    elif (city2, city1) in distances:
        return distances[(city2, city1)]
    else:
        return float('inf')  # Return infinity if no path exists

# List of cities to visit (excluding start/end city for permutations)
cities = ['Da Nang', 'Dalat', 'Nha Trang', 'Hai Phong', 'Ho Chi Minh']
start_city = 'Hanoi'

# Generate all possible routes starting and ending at the start city
all_routes = itertools.permutations(cities)

# Initialize variables to store the shortest route and its distance
shortest_route = None
shortest_distance = float('inf')
backup_route = None
backup_distance = float('inf')

# Calculate the distance for each route
for route in all_routes:
    total_distance = 0
    current_route = [start_city] + list(route) + [start_city]  # Add start and end city
    for i in range(len(current_route) - 1):
        total_distance += get_distance(current_route[i], current_route[i + 1])
    # Update shortest route if the current one is shorter
    if total_distance < shortest_distance:
        backup_route = shortest_route
        backup_distance = shortest_distance
        shortest_distance = total_distance
        shortest_route = current_route

# Display the results
print("Shortest route:", " -> ".join(shortest_route))
print("Total distance:", shortest_distance, "km")

if backup_route:
    print("Backup route:", " -> ".join(backup_route))
    print("Backup distance:", backup_distance, "km")

# A basic algorithm to solve the truck traveling route problem
def truck_traveling_route_problem():
    print("\nTruck Traveling Route Problem Solution:")
    visited = set()
    current_city = start_city
    total_distance = 0
    route = [current_city]

    while len(visited) < len(cities) + 1:  # Include start city as visited
        visited.add(current_city)
        nearest_city = None
        nearest_distance = float('inf')

        for city in cities + [start_city]:
            if city != current_city and city not in visited:
                distance = get_distance(current_city, city)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_city = city

        if nearest_city:
            route.append(nearest_city)
            total_distance += nearest_distance
            current_city = nearest_city
        else:
            break

    # Return to start city
    route.append(start_city)
    total_distance += get_distance(current_city, start_city)

    print("Truck route:", " -> ".join(route))
    print("Total distance:", total_distance, "km")

truck_traveling_route_problem()
