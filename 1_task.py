steps = list(map(int, input("Enter the number of steps taken each day (separated by spaces): ").split()))

highest_steps = max(steps)
lowest_steps = min(steps)

average_steps = sum(steps) / len(steps)

steps.sort(reverse=True)

print(f"Highest steps: {highest_steps}")
print(f"Lowest steps: {lowest_steps}")
print(f"Average daily steps: {average_steps:.2f}")
print(f"Sorted steps in descending order: {steps}")
