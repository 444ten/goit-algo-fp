import random

def simulate_dice_throws(num_simulations):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sum_counts[total] += 1

    probabilities = {k: v / num_simulations for k, v in sum_counts.items()}
    return probabilities

def main():
    num_simulations = 1_000_000
    monte_carlo_probs = simulate_dice_throws(num_simulations)

    analytical_probs = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

    print(f"{'Sum':<5} | {'Monte Carlo':<12} | {'Analytical':<12} | {'Difference':<10}")
    print("-" * 45)
    
    for s in range(2, 13):
        mc_p = monte_carlo_probs[s]
        an_p = analytical_probs[s]
        diff = abs(mc_p - an_p)
        print(f"{s:<5} | {mc_p:<12.4f} | {an_p:<12.4f} | {diff:<10.4f}")

if __name__ == "__main__":
    main()
