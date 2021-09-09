# David Martinez

# A number raised to the third power is a cube. Plot the first
#   five cubic numbers by calculating the values automatically.
#   Use can use either line or scatter points to plot.
#   Hint: 
#     To be plotted: 1, 8, 27, 64, 125

from matplotlib import pyplot as plt

plt.style.use('ggplot')

x = [1, 2, 3, 4, 5]     # base value
y = []                  # empty list for cubed values

for i in x:             # step through x value list to creat y value list
    y.append(i ** 3)    # append each new cubed value

fig, ax = plt.subplots() # create figure and axes

# plot line(x, y, marker, markersize, color)
ax.plot(x, y, color='red')
ax.scatter(x, y, color='green')

# Set title and labels, add legend
ax.set_title("Cube Values", fontsize=16)
ax.set_xlabel('Single Value', fontsize=12)
ax.set_ylabel('Value Cubed', fontsize=12)
ax.set_xticks((x))
ax.set_yticks((y))

plt.show()
