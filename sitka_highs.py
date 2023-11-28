from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime

path = Path("sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract high temperatures.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(current_date)
    high = int(row[4])
    highs.append(high)
print(highs)


# Plot the high temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")
# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
