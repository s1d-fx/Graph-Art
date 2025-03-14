import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def plot_function(f, xlim=(-6, 6), ylim=(-6, 6), num_points=1000, save_as=None):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = f(x)
    
    plt.figure(figsize=(7, 7))
    
    # Define color in RGB format
    light_gray = (225/255, 225/255, 225/255)
    grid_linewidth = 0.5
    
    # Draw axes with the same color and thickness as grid lines
    plt.axhline(0, color=light_gray, linewidth=grid_linewidth)
    plt.axvline(0, color=light_gray, linewidth=grid_linewidth)
    
    # Set grid and limits
    plt.xticks(np.arange(xlim[0], xlim[1] + 1, 1))
    plt.yticks(np.arange(ylim[0], ylim[1] + 1, 1))
    plt.grid(True, linestyle='-', linewidth=grid_linewidth, which='both', color=light_gray)
    # plt.minorticks_on()
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    # Plot the function with the specified light gray color
    plt.plot(x, y, color=light_gray, linewidth=0.8, label=f.__name__ if hasattr(f, '__name__') else 'Function')
    
    # Labels
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Graph")
    plt.legend()
    
    # Save or show the plot
    if save_as:
        plt.savefig(save_as, transparent=True, dpi=300)
        print(f"Graph saved as {save_as}")
    else:
        plt.show()

# The funtion
plot_function(lambda x: x**5, save_as="function_plot.png")  # Save as PNG with a transparent background
# save_as="function_plot.png"































