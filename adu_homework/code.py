import random
import numpy as np
from typing import List, Tuple

# -------------------- Problem Setup --------------------
def generate_random_solution(stock_length: int, piece_lengths: List[int]) -> List[int]:
    solution = []
    remaining = stock_length
    while True:
        options = [p for p in piece_lengths if p <= remaining]
        if not options:
            break
        choice = random.choice(options)
        solution.append(choice)
        remaining -= choice
    return solution

def calculate_waste(stock_length: int, solution: List[int]) -> int:
    return stock_length - sum(solution)

# -------------------- Simulated Annealing --------------------
def simulated_annealing(stock_length, piece_lengths, max_iter=1000, temp=100, cooling_rate=0.95):
    current = generate_random_solution(stock_length, piece_lengths)
    best = current
    for i in range(max_iter):
        candidate = generate_random_solution(stock_length, piece_lengths)
        delta = calculate_waste(stock_length, current) - calculate_waste(stock_length, candidate)
        if delta > 0 or random.random() < np.exp(delta / temp):
            current = candidate
        if calculate_waste(stock_length, current) < calculate_waste(stock_length, best):
            best = current
        temp *= cooling_rate
    return best

# -------------------- Hill Climbing --------------------
def hill_climbing(stock_length, piece_lengths, max_iter=1000):
    current = generate_random_solution(stock_length, piece_lengths)
    best = current
    for _ in range(max_iter):
        neighbor = generate_random_solution(stock_length, piece_lengths)
        if calculate_waste(stock_length, neighbor) < calculate_waste(stock_length, best):
            best = neighbor
    return best

# -------------------- Genetic Algorithm --------------------
def crossover(parent1, parent2):
    cut = random.randint(1, min(len(parent1), len(parent2)) - 1)
    child = parent1[:cut] + parent2[cut:]
    return child

def mutate(solution, piece_lengths, stock_length):
    if solution:
        idx = random.randint(0, len(solution) - 1)
        solution[idx] = random.choice(piece_lengths)
    return solution

def genetic_algorithm(stock_length, piece_lengths, population_size=10, generations=50):
    population = [generate_random_solution(stock_length, piece_lengths) for _ in range(population_size)]
    for _ in range(generations):
        population.sort(key=lambda x: calculate_waste(stock_length, x))
        new_population = population[:2]  # Keep best two
        while len(new_population) < population_size:
            parents = random.sample(population[:5], 2)
            child = crossover(parents[0], parents[1])
            child = mutate(child, piece_lengths, stock_length)
            new_population.append(child)
        population = new_population
    return min(population, key=lambda x: calculate_waste(stock_length, x))

# -------------------- Multi-Agent Execution --------------------
def run_agents(stock_length: int, piece_lengths: List[int], agent_count: int):
    results = []
    heuristics = [simulated_annealing, hill_climbing, genetic_algorithm]
    for i in range(agent_count):
        algo = heuristics[i % len(heuristics)]
        solution = algo(stock_length, piece_lengths)
        results.append((algo.__name__, solution, calculate_waste(stock_length, solution)))
    return results

# -------------------- Main --------------------
if __name__ == "__main__":
    stock_length = int(input("Enter stock roll length: "))
    piece_lengths = list(map(int, input("Enter required piece lengths (comma-separated): ").split(',')))
    agent_count = int(input("Enter number of agents: "))

    results = run_agents(stock_length, piece_lengths, agent_count)

    for algo, solution, waste in results:
        print(f"\nAgent using {algo} found solution: {solution} with waste: {waste}")
