**CSE 419 - ARTIFICIAL INTELLIGENCE**

**Assignment #1: Cutting Stock Problem Using Multi-Agent Heuristic Optimization**

**Student Name:** Gökçe Soylu  
**Student ID:** 241805111  
**Date:** April 15, 2025

---

### **1. Introduction**

The Cutting Stock Problem (CSP) is a classic optimization problem encountered in manufacturing and production, where the objective is to cut large rolls of stock material (e.g., wood, paper, metal) into smaller required pieces while minimizing material waste. In this project, we solve the CSP using heuristic optimization methods within a multi-agent architecture.

---

### **2. Problem Definition**

Given a stock roll of fixed length and a list of smaller piece lengths required to fulfill customer orders, the goal is to determine an optimal cutting pattern that minimizes leftover material. For example, from a 100-meter roll, if required pieces are of lengths 10, 15, and 20 meters, the aim is to use as much of the roll as possible while cutting the pieces exactly as needed.

---

### **3. Methodology**

#### 3.1 Multi-Agent System Design
Two different multi-agent strategies were implemented:
- **Collaborative Agent-Based Optimization**: Each agent independently attempts to solve the CSP and shares its best solution. The agents combine their findings to collaboratively refine the final solution.
- **Hyper Meta-Heuristic Approach**: Each agent uses a different heuristic algorithm. The best solution among the agents is selected.

#### 3.2 Heuristic Algorithms Used
- **Simulated Annealing (SA)**: Uses a temperature-based probabilistic acceptance of worse solutions to escape local optima.
- **Hill Climbing (HC)**: Iteratively moves to neighboring solutions that offer better results.
- **Genetic Algorithm (GA)**: Employs selection, crossover, and mutation to evolve a population of solutions.

---

### **4. Implementation Details**

The Python implementation allows users to set:
- Stock roll length
- Required piece lengths (as a list)
- Number of agents
- Selected heuristic algorithms per agent (automated assignment)

Each agent runs its assigned algorithm and reports the resulting cutting pattern and waste.

---

### **5. Experimental Results**

Sample configuration:
- **Stock Length**: 100 meters
- **Piece Lengths**: [10, 15, 20]
- **Agents**: 3 (SA, HC, GA)

| Agent | Algorithm             | Cutting Pattern           | Waste (meters) |
|-------|------------------------|----------------------------|----------------|
| 1     | Simulated Annealing   | [20, 20, 20, 20, 15]       | 5              |
| 2     | Hill Climbing         | [15, 15, 20, 20, 15, 10]   | 5              |
| 3     | Genetic Algorithm     | [20, 20, 20, 15, 15, 10]   | 0              |

---

### **6. Conclusion**

The multi-agent heuristic approach for solving the Cutting Stock Problem has shown promising results. Among the three algorithms tested, the Genetic Algorithm achieved the lowest waste in the sample configuration. This demonstrates the value of using diverse optimization strategies in parallel and selecting the best among them.

Future improvements may include:
- Dynamic agent coordination
- Hybrid strategies
- GUI for broader usability

---

### **References**
[1] https://github.com/nargesbh/Cutting-stock-problem-using-Simulated-Annealing  
[2] https://pypi.org/project/mealpy/