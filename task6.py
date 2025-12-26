items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    item_list = []
    for name, data in items.items():
        ratio = data["calories"] / data["cost"]
        item_list.append((name, data["cost"], data["calories"], ratio))
    
    item_list.sort(key=lambda x: x[3], reverse=True)
    
    total_calories = 0
    total_cost = 0
    chosen_items = []

    for name, cost, calories, ratio in item_list:
        if total_cost + cost <= budget:
            chosen_items.append(name)
            total_cost += cost
            total_calories += calories
            
    return chosen_items, total_calories, total_cost

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    costs = [items[name]["cost"] for name in item_names]
    calories = [items[name]["calories"] for name in item_names]
    n = len(item_names)

    # dp[w] will store the maximum calories for budget w
    # We use a table to also reconstruct which items were picked.
    # K[i][w] = max calories using first i items with budget w
    K = [[0 for w in range(budget + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i-1] <= w:
                K[i][w] = max(calories[i-1] + K[i-1][w-costs[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # Reconstruct the solution (find which items were included)
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if K[i][w] != K[i-1][w]:
            chosen_items.append(item_names[i-1])
            w -= costs[i-1]
    
    total_calories = K[n][budget]
    # Total cost can be calculated by budget - remaining w, or summing items
    total_cost = sum(items[item]["cost"] for item in chosen_items)
            
    return chosen_items, total_calories, total_cost

if __name__ == "__main__":
    budget_limit = 100
    
    print(f"Budget: {budget_limit}")
    
    greedy_items, greedy_cal, greedy_cost = greedy_algorithm(items, budget_limit)
    print(f"Greedy Algorithm: {greedy_items}, Calories: {greedy_cal}, Cost: {greedy_cost}")

    dp_items, dp_cal, dp_cost = dynamic_programming(items, budget_limit)
    print(f"Dynamic Programming: {dp_items}, Calories: {dp_cal}, Cost: {dp_cost}")
