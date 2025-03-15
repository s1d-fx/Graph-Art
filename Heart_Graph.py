import numpy as np
import matplotlib.pyplot as plt

scale = 5

def plot_implicit_function(xlim=(-scale, scale), ylim=(-scale, scale), resolution=500, save_as=None):

    # Create a grid of (x, y) values.
    x = np.linspace(xlim[0], xlim[1], resolution)
    y = np.linspace(ylim[0], ylim[1], resolution)
    X, Y = np.meshgrid(x, y)
    
    # Evaluate the implicit function: (x²+y²-1)³ - x²y³ = 0
    Z = (X**2 + Y**2 - 1)**3 - (X**2) * (Y**3)
    
    plt.figure(figsize=(8, 8))
    
    # Define color in RGB format
    col = 200
    light_gray = (col/255, col/255, col/255)
    grid_linewidth = 0.3
    
    # Draw the axes
    plt.axhline(0, color=light_gray, linewidth=grid_linewidth)
    plt.axvline(0, color=light_gray, linewidth=grid_linewidth)
    
    # Set grid and limits
    plt.xticks(np.arange(xlim[0], xlim[1] + 1, 1), [])  # Keep grid, hide numbers
    plt.yticks(np.arange(ylim[0], ylim[1] + 1, 1), [])  # Keep grid, hide numbers
    plt.grid(True, linestyle='-', linewidth=grid_linewidth, which='both', color=light_gray)
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    
    # Remove minor ticks and plot borders
    plt.gca().tick_params(which='both', size=0)  # Remove tick marks
    plt.gca().spines['top'].set_color(light_gray)
    plt.gca().spines['right'].set_color(light_gray)
    plt.gca().spines['bottom'].set_color(light_gray)
    plt.gca().spines['left'].set_color(light_gray)
    
    # Plot the implicit function by drawing the contour where Z == 0.
    plt.contour(X, Y, Z, levels=[0], colors=[light_gray], linewidths=0.8)
    
    # Save or display the plot.
    if save_as:
        plt.savefig(save_as, transparent=True, dpi=300)
        print(f"Graph saved as {save_as}")
    else:
        plt.show()

plot_implicit_function(save_as="heart_function_plot")
