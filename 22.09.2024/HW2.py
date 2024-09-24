import statistics
# START
heights: list[float] = []
height_more2: list[float] = []
above_average: list[float] = []

while True:
    height: float = float(input("What is the players height?: "))
    if height == -999:
        break
    if height < 1.60:
        continue
    if height > 2.0:
        height_more2.append(height)
    heights.append(height)

mean_heights = statistics.mean(heights)

print(f"There were {len(heights)} heights entered.")
print(f"The shortest height entered was {min(heights)}.")
print(f"The tallest height entered was {max(heights)}.")
print(f"The mean of all the heights was {mean_heights}")
print(f"There were {len(height_more2)} players that are taller than 2.0")

for height in heights:
    if height > mean_heights:
        above_average.append(height)
print(f"There were {len(above_average)} players that their height was above average.")

# STOP
