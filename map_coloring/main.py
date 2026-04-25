regions = input("Enter regions (comma separated): ").split(',')
colors = ['Red', 'Green', 'Blue']

neighbors = {}
for r in regions:
    neighbors[r] = input(f"Enter neighbors of {r} (comma separated): ").split(',')

def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment

    unassigned = [r for r in regions if r not in assignment][0]

    for color in colors:
        print(f"Trying {unassigned} → {color}")
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            result = backtrack(assignment)
            if result:
                return result
            print(f"Backtracking on {unassigned}")
            del assignment[unassigned]

    return None

solution = backtrack({})

print("\nFinal Solution:")
for region, color in solution.items():
    print(f"{region} is colored {color}")
