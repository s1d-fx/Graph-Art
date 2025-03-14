import numpy as np
import matplotlib.pyplot as plt

def plot_function(f, xlim=(-8, 8), ylim=(-8, 8), num_points=1000, save_as=None):
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
    plt.xticks(np.arange(xlim[0], xlim[1] + 1, 1), [])  # Keep grid but hide numbers
    plt.yticks(np.arange(ylim[0], ylim[1] + 1, 1), [])  # Keep grid but hide numbers
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
    
    # Add function label
    function_label = f"y = {f.__name__}(x)" if hasattr(f, '__name__') else "y = f(x)"
    plt.text(0.5 * (xlim[0] + xlim[1]), 0.8 * ylim[1], function_label, color=graph_colour, fontsize=12, ha='center')
    
    # Save or show the plot
    if save_as:
        plt.savefig(save_as, transparent=True, dpi=300)
        print(f"Graph saved as {save_as}")
    else:
        plt.show()


# The Function:
plot_function(np.cos)  # Save as PNG with a transparent background
# save_as="function_plot.png"
