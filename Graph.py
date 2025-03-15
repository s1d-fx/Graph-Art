import numpy as np
import matplotlib.pyplot as plt

scale = 2.4

def plot_function(f, xlim=(-scale, scale), ylim=(-scale, scale), num_points=1000, save_as=None):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = f(x)
    
    plt.figure(figsize=(7, 7))
    
    # Define color in RGB format
    col = 200
    graph_colour = (col/255, col/255, col/255)
    grid_linewidth = 0.3
    
    # Draw axes 
    plt.axhline(0, color=graph_colour, linewidth=grid_linewidth)
    plt.axvline(0, color=graph_colour, linewidth=grid_linewidth)
    
    # Set grid and limits, ensuring final right and bottom grid lines appear
    plt.xticks(np.arange(xlim[0], xlim[1] + 1, 1), color=graph_colour)  # Keep grid, hide numbers
    plt.yticks(np.arange(ylim[0], ylim[1] + 1, 1), color=graph_colour)  # Keep grid, hide numbers
    plt.grid(True, linestyle='-', linewidth=grid_linewidth, which='both', color=graph_colour)
    plt.minorticks_on()
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    
    # Remove tick marks and plot borders
    plt.gca().tick_params(which='both', size=0, colors=graph_colour)  # Set tick color  # Remove tick marks
    plt.gca().spines['top'].set_color(graph_colour)
    plt.gca().spines['right'].set_color(graph_colour)
    plt.gca().spines['bottom'].set_color(graph_colour)
    plt.gca().spines['left'].set_color(graph_colour)
    
    # Plot the function with the specified light gray color
    plt.plot(x, y, color=graph_colour, linewidth=0.8)
    
    # Save or show the plot
    if save_as:
        plt.savefig(save_as, transparent=True, dpi=300)
        print(f"Graph saved as {save_as}")
    else:
        plt.show()

k = 2

# The Function:
plot_function(lambda x: np.e**(-x**2), save_as="function_plot.png")
# save_as="function_plot.png"
