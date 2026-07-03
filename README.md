# 8-Puzzle Problem using A* Search and Greedy Best-First Search

This repository contains Python implementations of two informed search algorithms for solving the **8-Puzzle Problem**:

- A* Search Algorithm
- Greedy Best-First Search (GBFS)

This project was completed as part of the CSEAM332 Introduction to AI coursework.

---

## Objective

The objective of this assignment is to:

- Implement the 8-Puzzle problem in Python.
- Solve the puzzle using:
  - A* Search Algorithm
  - Greedy Best-First Search
- Verify that both implementations execute correctly.
- Store the implementations as separate `.py` files.
- Collaborate by sharing the repository.

---

## Files

```
8-puzzle/
│
├── astar.py          # A* Search implementation
├── greedy.py         # Greedy Best-First Search implementation
└── README.md
```

---

## Algorithms Used

### A* Search

A* Search combines the actual path cost (`g(n)`) and the heuristic estimate (`h(n)`) to evaluate each state.

```
f(n) = g(n) + h(n)
```

It guarantees an optimal solution when an admissible heuristic, such as the Manhattan Distance, is used.

---

### Greedy Best-First Search

Greedy Best-First Search expands the node that appears closest to the goal according to the heuristic.

```
f(n) = h(n)
```

Although it is often faster, it does not always produce the shortest solution.

---

## Heuristic

Both implementations use the **Manhattan Distance** heuristic, which computes the sum of the distances of each tile from its goal position.

---

## Requirements

- Python 3.x

No external libraries are required.

---

## Running the Programs

Run the A* Search implementation:

```bash
python astar.py
```

Run the Greedy Best-First Search implementation:

```bash
python greedy.py
```

---

## Expected Output

The programs display the sequence of explored puzzle states and indicate when the goal state has been reached.

---

## Learning Outcomes

- Understanding informed search algorithms
- Implementing heuristic search techniques
- Comparing A* Search and Greedy Best-First Search
- Using Git and GitHub for version control and collaboration

---

## Repository

This repository was created for academic purposes as part of the Artificial Intelligence laboratory coursework.
