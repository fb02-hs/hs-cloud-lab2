import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Read data from CSV file
with open('history.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)  # skip header row
    dates = []
    rates = []
    for row in reader:
        dates.append(datetime.strptime(row[0], '%d.%m.%Y'))  # convert date string to datetime object
        rates.append(float(row[1]))

# Build plot
fig, ax = plt.subplots(figsize=(14, 8))
fig.set_dpi(500)
ax.plot(dates, rates)
ax.set_xlabel('Date')
ax.set_ylabel('Rate')
ax.set_title('History: UAH per USD')
ax.xaxis.set_major_locator(mdates.MonthLocator())   # set major ticks every month
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) # format month and year
ax.tick_params(axis='x', rotation=45, labelsize=10)   # rotate x-axis labels by 45 degrees
plt.subplots_adjust(left=0.05, right=0.99, bottom=0.15, top=0.95)  # set the left padding to 10% and right padding to 90%
# Save plot to file
plt.savefig('exchange_rate.png')
