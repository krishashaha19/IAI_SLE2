# BFS vs DFS – Empirical Performance Analysis

## Course

02AML204 – Introduction to Artificial Intelligence

## Project Type

SLE-2: Profiling Report

---

## 1. Project Overview

This project compares the performance of two uninformed search
algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms are tested on the same small graph so that their
performance can be compared fairly.

The main purpose of this project is to measure actual execution
performance instead of only discussing the algorithms theoretically.

---

## 2. Problem Used

A small graph is used for the experiment.

The starting node is:

A

The goal node is:

G

Graph structure:

A → B, C

B → D, E

C → F, G

The algorithms search for a path from A to G.

---

## 3. Algorithms Used

### Breadth-First Search (BFS)

BFS explores nodes level by level.

It uses a queue to store the nodes that need to be explored.

### Depth-First Search (DFS)

DFS explores one branch as deeply as possible before going to another
branch.

It uses a stack to store the nodes that need to be explored.

---

## 4. Programming Language

Python 3

---

## 5. Tools Used

- Python
- VS Code / Python IDE
- `time` module
- Manual node counter

The `time.perf_counter()` function is used to measure execution time.

---

## 6. Performance Metrics

The following measurements are collected:

1. Run 1 execution time
2. Run 2 execution time
3. Run 3 execution time
4. Average execution time
5. Best execution time
6. Worst execution time
7. Number of nodes expanded

Execution time is measured in milliseconds (ms).

---

## 7. Experimental Method

1. Create the same graph for both algorithms.
2. Start the search from node A.
3. Search for node G.
4. Run BFS three times.
5. Record the execution time of every run.
6. Run DFS three times.
7. Record the execution time of every run.
8. Calculate average, best and worst execution time.
9. Count the nodes expanded by each algorithm.
10. Compare the results.

Both algorithms use the same problem so that the comparison is fair.

---

## 8. Results

The actual results are obtained by running the Python program.

| Metric | BFS | DFS |
|---|---:|---:|
| Average Time (ms) | ______ | ______ |
| Best Time (ms) | ______ | ______ |
| Worst Time (ms) | ______ | ______ |
| Nodes Expanded | ______ | ______ |

The values above should be filled using the actual output obtained
from the program.

---

## 9. Conclusion

The experiment measures the actual performance of BFS and DFS using
execution time and the number of nodes expanded.

The final comparison is based on the measured results obtained from
running both algorithms on the same graph.

The experiment helps in understanding how search algorithms can be
evaluated using practical performance measurements rather than only
theoretical analysis.

---

## 10. AI Contribution

ChatGPT was used as a learning and coding assistance tool.

AI helped with understanding the SLE-2 requirements, preparing the
BFS and DFS implementation, adding profiling calculations, and
organizing the project documentation.

The actual program execution and collection of performance values were
performed by the student.

---

## 11. How to Run

Make sure Python 3 is installed.

Open the project folder in VS Code.

Run:

    python sle2_bfs_dfs.py

The program displays:

- BFS path
- DFS path
- Individual run times
- Average time
- Best time
- Worst time
- Nodes expanded
- Comparison table
- Basic analysis

---

## 12. Files

sle2_bfs_dfs.py
    Python program containing BFS, DFS and profiling code.

README.md
    Project description and instructions.

AI_Contribution_Log.md
    Record of AI assistance and student contribution.

---

## 13. Student Information

Name: Krisha Shaha

PRN: 25UAM070

Division: A

Date: 22/09/2026