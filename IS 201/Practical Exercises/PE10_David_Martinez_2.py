# David Martinez

# Plot first 10 square number sequence in a graph by calculating
#   the values automatically. Use scatter points to plot.
# Hint:
#   To be plotted: 1, 4, 9, 16, 25, 36, 49, 64, 81, and 100

from matplotlib import pyplot as plt

plt.style.use('ggplot')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     # base value
y = []                  # empty list for squared values

for i in x:             # step through x value list to creat y value list
    y.append(i ** 2)    # append each new squared value

fig, ax = plt.subplots() # create figure and axes

# plot scatter shot
ax.scatter(x, y, color='green')

# Set title and labels, add legend
ax.set_title("Squared Values", fontsize=16)
ax.set_xlabel('Single Value', fontsize=12)
ax.set_ylabel('Value Squared', fontsize=12)
ax.set_xticks((x))
ax.set_yticks((y))

plt.show()
