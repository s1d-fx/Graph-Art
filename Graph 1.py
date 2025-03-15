import numpy as np
import matplotlib.pyplot as plt

scale = 5

def plot_function(f, xlim=(-scale, scale), ylim=(-scale, scale), num_points=1000, save_as=None):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = f(x)
    
    plt.figure(figsize=(8, 8))
    
    # Define color in RGB format
    graph_colour = (225/255, 225/255, 225/255)
    grid_linewidth = 0.5
    
    # Draw axes 
    plt.axhline(0, color=graph_colour, linewidth=grid_linewidth)
    plt.axvline(0, color=graph_colour, linewidth=grid_linewidth)
    
    # Set grid and limits, ensuring final right and bottom grid lines appear
    plt.xticks(np.arange(xlim[0], xlim[1] + 1, 1), [])  # Keep grid, hide numbers
    plt.yticks(np.arange(ylim[0], ylim[1] + 1, 1), [])  # Keep grid, hide numbers
    plt.grid(True, linestyle='-', linewidth=grid_linewidth, which='both', color=graph_colour)
    plt.xlim(xlim[0] - 0.5, xlim[1] + 0.5)
    plt.ylim(ylim[0] - 0.5, ylim[1] + 0.5)
    
    # Remove minor ticks and plot borders
    plt.gca().tick_params(which='both', size=0)  # Remove tick marks
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    
    # Plot the function with the specified light gray color
    plt.plot(x, y, color=graph_colour, linewidth=0.8)
    
    # Save or show the plot
    if save_as:
        plt.savefig(save_as, transparent=True, dpi=300)
        print(f"Graph saved as {save_as}")
    else:
        plt.show()


# The Function:
# plot_function(np.cos) # Plot
plot_function(np.cos, save_as="function_plot.png") # Save as png
