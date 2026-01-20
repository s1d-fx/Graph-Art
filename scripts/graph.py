import numpy as np
import matplotlib.pyplot as plt

len_x = 5
len_y = 3

def plot_function(f, xlim=(-len_x, len_x), ylim=(-2, len_y), num_points=1000, save_as=None):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = f(x)
    
    plt.figure(figsize=(10, 5))
    
    # Define color in RGB format
    grid = 130
    line = 50
    grid_col = (grid/255, grid/255, grid/255)
    line_col = (line/255, line/255, line/255)
    grid_linewidth = 0.3
    
    # Draw axes 
    plt.axhline(0, color=grid_col, linewidth=grid_linewidth)
    plt.axvline(0, color=grid_col, linewidth=grid_linewidth)
    
    # Set grid and limits, ensuring final right and bottom grid lines appear
    plt.xticks(np.arange(xlim[0], xlim[1] + 1, 1), color=grid_col)  # Keep grid, hide numbers
    plt.yticks(np.arange(ylim[0], ylim[1] + 1, 1), color=grid_col)  # Keep grid, hide numbers
    plt.grid(True, linestyle='-', linewidth=grid_linewidth, which='both', color=grid_col)
    plt.minorticks_on()
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    
    # Remove tick marks and plot borders
    plt.gca().tick_params(which='both', size=0, colors=grid_col)  # Set tick color  # Remove tick marks
    plt.gca().spines['top'].set_color(grid_col)
    plt.gca().spines['right'].set_color(grid_col)
    plt.gca().spines['bottom'].set_color(grid_col)
    plt.gca().spines['left'].set_color(grid_col)
    
    # Plot the function with the specified light gray color
    plt.plot(x, y, color=line_col, linewidth=0.8)
    
    # Save or show the plot
    if save_as:
        plt.savefig(save_as, transparent=True, dpi=300)
        print(f"Graph saved as {save_as}")
    else:
        plt.show()

# The Function:
plot_function(lambda x: np.e**(-x**2))
# save_as="function_plot.png"
