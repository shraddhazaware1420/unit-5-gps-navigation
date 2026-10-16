"""
Name: Zaware Shraddha Sandip
Roll No.: 67 | Division: B | Batch: C
Unit V Case Study: GPS Navigation Using a Weighted Graph
Algorithm: Dijkstra's Shortest Path
"""

import heapq


# Each road connects two locations; its value is the distance in kilometres.
CITY_MAP = {
    "College": {"Library": 4, "Hospital": 7},
    "Library": {"College": 4, "Market": 3, "Park": 6},
    "Hospital": {"College": 7, "Market": 2},
    "Market": {"Library": 3, "Hospital": 2, "Park": 4, "Station": 5},
    "Park": {"Library": 6, "Market": 4, "Station": 2},
    "Station": {"Market": 5, "Park": 2},
}


def shortest_route(graph, start, destination):
    """Return the shortest distance and route using Dijkstra's algorithm."""
    distances = {location: float("inf") for location in graph}
    previous = {location: None for location in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)

        if current_distance > distances[current]:
            continue

        if current == destination:
            break

        for neighbour, road_distance in graph[current].items():
            new_distance = current_distance + road_distance

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = current
                heapq.heappush(priority_queue, (new_distance, neighbour))

    if distances[destination] == float("inf"):
        return None, []

    route = []
    current = destination
    while current is not None:
        route.append(current)
        current = previous[current]

    route.reverse()
    return distances[destination], route


def main():
    locations = list(CITY_MAP)

    while True:
        print("\n=== City GPS Navigation ===")
        print("Locations:", ", ".join(locations))
        print("1. Find shortest route")
        print("2. Display road connections")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            start = input("Starting location: ").strip().title()
            destination = input("Destination: ").strip().title()

            if start not in CITY_MAP or destination not in CITY_MAP:
                print("Please enter locations from the list.")
                continue

            if start == destination:
                print(f"You are already at {start}. Distance: 0 km.")
                continue

            distance, route = shortest_route(CITY_MAP, start, destination)

            if route:
                print("Shortest route:", " -> ".join(route))
                print(f"Total distance: {distance} km")
            else:
                print("No route is available.")
        elif choice == "2":
            print("\nRoad connections:")
            for location, roads in CITY_MAP.items():
                connections = ", ".join(
                    f"{neighbour} ({distance} km)"
                    for neighbour, distance in roads.items()
                )
                print(f"{location}: {connections}")
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Choose 0, 1, or 2.")


if __name__ == "__main__":
    main()
    