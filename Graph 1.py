import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def plot_function(f, xlim=(-10, 10), ylim=(-10, 10), num_points=1000, save_as=None):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = f(x)
    
    plt.figure(figsize=(7, 7))
    
    # Draw axes
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    
    # Set grid and limits
    plt.xticks(np.arange(xlim[0], xlim[1]))
    plt.yticks(np.arange(ylim[0], ylim[1]))
    plt.grid(True, linestyle='-', linewidth=0.5, which='both')
    # plt.minorticks_on()
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    # Plot the function
    plt.plot(x, y, label=f.__name__ if hasattr(f, '__name__') else 'Function')
    
    # Labels
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Function Plot on a Coordinate Plane")
    plt.legend()
    
    # Save or show the plot
    if save_as:
        plt.savefig(save_as, transparent=True, dpi=300)
        print(f"Graph saved as {save_as}")
    else:
        plt.show()

# The funtion
plot_function(lambda x: x**3)  # Save as PNG with a transparent background
# save_as="function_plot.png"































