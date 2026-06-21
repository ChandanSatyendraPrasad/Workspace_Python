from statistics import mode

data = [10, 30, 20, 40, 50]
mean = sum(data) / len(data)
print("Mean: ", mean)

sorted_data = sorted(data)
print("Sorted Data :\n",sorted_data)
median = sorted_data[len(data) // 2] if len(data) % 2 != 0 else (
    (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2
)
print("Median: ", median)

print("Mode: ", mode(data))

variance = sum((x - mean) ** 2 for x in data) / len(data)
print("Variance: ", variance)
std_dev = variance ** 0.5
print("Standard Deviation:", std_dev)