# SEM_4_MPR_TSP
# TSP Solver

## Description
The Traveling Salesman Problem (TSP) Solver is a Python application designed to find the optimal solution for the Traveling Salesman Problem using two different algorithms: Branch and Bound, and Nearest Neighbor. The TSP involves finding the shortest possible route that visits each city exactly once and returns to the original city.

## Features
- **Branch and Bound Algorithm:** Utilizes the Branch and Bound algorithm to find the optimal solution for the TSP by exhaustively searching through all possible paths and pruning branches that cannot lead to an optimal solution.
- **Nearest Neighbor Algorithm:** Implements the Nearest Neighbor algorithm to find a suboptimal solution for the TSP by iteratively selecting the nearest unvisited city from the current city.
- **Graphical User Interface (GUI):** Provides a simple GUI interface using Tkinter for users to select the desired algorithm and visualize the optimal solution using Turtle graphics.

## Files
- **GUI.py:** Contains the Tkinter-based GUI for the TSP Solver application, allowing users to choose between the Branch and Bound or Nearest Neighbor algorithms and visualize the optimal solution.
- **BnB.py:** Implements the Branch and Bound algorithm for solving the TSP, utilizing techniques such as bounding and backtracking to find the optimal solution.
- **NN.py:** Implements the Nearest Neighbor algorithm for solving the TSP, which iteratively selects the nearest unvisited city from the current city to construct a suboptimal solution.

## Usage
1. Run the `GUI.py` file to launch the TSP Solver application.
2. Select the desired algorithm (Branch and Bound or Nearest Neighbor) by clicking the corresponding radio button.
3. Click the "Solve TSP" button to initiate the solving process.
4. The application will display the optimal solution graphically using Turtle graphics, including the optimal path and the total distance traveled.

## Requirements
- Python 3.x
- Tkinter
- Turtle

## Installation
1. Clone the repository from GitHub using the following command:
```bash
git clone https://github.com/MeetRaut/SEM_4_MPR_TSP.git
```
## Authors
- [Amit Shinde](https://github.com/Amit-Shinde4)
- [Hringkesh Singh](https://github.com/HringkeshSingh)
- [Meet Raut](https://github.com/MeetRaut)
- [Shrirang Zend](https://github.com/Shrirang-Zend)
