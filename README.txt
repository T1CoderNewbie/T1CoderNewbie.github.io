This Python script solves the following problems:

Shortest Route Problem: Uses a brute-force approach to find the shortest possible route that starts and ends in Ho Chi Minh City while visiting a set of specified cities exactly once.

Truck Traveling Route Problem: Implements a greedy algorithm to calculate a route by visiting the nearest unvisited city until all cities are visited, then returning to the starting city.

Features

Calculates the shortest route using all permutations of the given cities.

Provides a basic greedy solution for the truck traveling route problem.

Outputs the route and total distance for both problems.

Requirements

To run this script, ensure you have the following:

Python 3.x installed.

The pandas and tabulate libraries installed (though not required for the current script, you can install them for potential extensions).

How to Run

Download the Script
Download the shortest_route.py file to your computer.

Install Python
If Python is not installed, download and install it from python.org.

Run the Script

Open a terminal (Command Prompt, PowerShell, or a terminal emulator).

Navigate to the folder where the script is saved. For example:

cd path/to/your/folder

Run the script using the following command:

python shortest_route.py

Output

When the script runs successfully, it will display:

Shortest Route Solution:

The optimal route that minimizes total distance.

The total distance traveled.

Truck Traveling Route Solution:

A greedy solution that visits the nearest city at each step.

The corresponding total distance.

Example Output

Shortest route: Ho Chi Minh -> Dalat -> Nha Trang -> Da Nang -> Hai Phong -> Ho Chi Minh
Total distance: XXXX km

Truck Traveling Route Problem Solution:
Truck route: Ho Chi Minh -> Dalat -> Nha Trang -> Da Nang -> Hai Phong -> Ho Chi Minh
Total distance: YYYY km

Notes

The brute-force approach guarantees the shortest route but may become computationally expensive for a large number of cities.

The greedy algorithm provides a faster, approximate solution for practical use cases.
