# AI Problem Solving Assignment

## Repository Name

AI_ProblemSolving_RA2411026050059

---

## Team Members

* K.Saketh
* P.Parthivendra

---

## Objective

The objective of this assignment is to apply Artificial Intelligence problem-solving techniques using practical implementation. This project demonstrates how AI algorithms can be used to solve real-world logical problems using Constraint Satisfaction Problem (CSP) approaches.

---

## Problems Implemented

### 1. Map Coloring Problem (CSP)

#### Description

The map coloring problem involves assigning colors to different regions such that no two adjacent regions share the same color. This is a classic problem in AI used to demonstrate constraint satisfaction.

#### Features

* Accepts user input for regions and neighbors
* Dynamically builds the constraint graph
* Ensures no adjacent regions have the same color
* Displays step-by-step solving process
* Uses limited colors (Red, Green, Blue)

#### Algorithm Used

* Backtracking Search
* Constraint Satisfaction Problem (CSP)

#### How It Works

1. User inputs regions and adjacency
2. System assigns colors one by one
3. Checks constraints at each step
4. If conflict occurs → backtracking is applied
5. Final valid solution is displayed

---

### 2. Crypt Arithmetic Puzzle Solver (CSP)

#### Description

Crypt arithmetic puzzles assign digits to letters such that a mathematical equation is satisfied. Example:
SEND + MORE = MONEY

#### Features

* Accepts any valid puzzle input
* Ensures each letter has a unique digit
* Prevents leading zeros
* Displays valid solution mapping
* Shows computed arithmetic result

#### Algorithm Used

* Constraint Satisfaction Problem (CSP)
* Permutation-based search

#### How It Works

1. User inputs puzzle
2. Extracts unique letters
3. Generates permutations of digits
4. Applies constraints (no leading zero, unique mapping)
5. Checks equation validity
6. Displays correct solution

---

## AI Concepts Demonstrated

* Constraint Satisfaction Problem (CSP)
* Backtracking Algorithm
* State Space Search
* Constraint Propagation
* Search Space Optimization

---

## Comparison / Analysis

| Feature      | Map Coloring   | Crypt Arithmetic  |
| ------------ | -------------- | ----------------- |
| Approach     | Backtracking   | Permutation + CSP |
| Complexity   | Low–Moderate   | High              |
| Speed        | Faster         | Slower            |
| Search Space | Smaller        | Larger            |
| Use Case     | Graph problems | Logical puzzles   |

### Conclusion

* Map Coloring is efficient due to smaller search space
* Crypt Arithmetic is computationally heavier but demonstrates deeper constraint reasoning

---

## Why This is Artificial Intelligence

This project demonstrates AI principles by simulating intelligent decision-making:

* The system explores multiple possible states
* Applies constraints to eliminate invalid solutions
* Uses backtracking when a path fails
* Finds optimal valid solutions without brute-force guessing

This mimics how intelligent agents solve complex problems.

---

## How to Run the Project

### Requirements

* Python 3.x installed

### Steps

```bash
cd map_coloring
python main.py

cd ../cryptarithmetic
python main.py
```

---

## Sample Output

### Map Coloring

A → Red
B → Green
C → Blue
D → Red

### Crypt Arithmetic

9567 + 1085 = 10652

---

## Project Structure

```
AI_ProblemSolving/
│
├── map_coloring/
│   └── main.py
│
├── cryptarithmetic/
│   └── main.py
│
└── README.md
```

---

## Key Highlights

* Interactive input-based system
* Demonstrates core AI algorithms
* Clean and modular implementation
* Suitable for understanding CSP concepts
* Easily extendable to more complex problems

---

## Future Enhancements

* Add graphical user interface (GUI)
* Improve optimization techniques
* Add more CSP problems
* Visualize search process using graphs

---

## Conclusion

This project successfully demonstrates how Artificial Intelligence techniques such as CSP and backtracking can be used to solve logical and combinatorial problems efficiently. It provides a strong foundation for understanding problem-solving in AI.

---
