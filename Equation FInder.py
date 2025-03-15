import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

# Lists to store drawn points
points = []

def on_move(event):
    if event.xdata is not None and event.ydata is not None:
        points.append((event.xdata, event.ydata))
        plt.plot(event.xdata, event.ydata, 'ro', markersize=2)  # Mark drawn points
        plt.draw()

def on_release(event):
    if len(points) >= 4:  # Fit polynomial once enough points are available
        x_vals, y_vals = zip(*points)
        coeffs = poly.Polynomial.fit(x_vals, y_vals, deg=3).convert().coef  # Cubic fit
        coeffs = [c * 10 for c in coeffs]  # Scale coefficients to make them larger
        x_line = np.linspace(min(x_vals), max(x_vals), 100)
        y_line = coeffs[0] + coeffs[1] * x_line + coeffs[2] * x_line**2 + coeffs[3] * x_line**3
        
        plt.clf()  # Clear old points
        plt.axhline(0, color='black', linewidth=1)  # Add x-axis
        plt.axvline(0, color='black', linewidth=1)  # Add y-axis
        plt.plot(x_vals, y_vals, 'ro', markersize=2)  # Replot drawn points
        plt.plot(x_line, y_line, 'b-', label=f'y = {coeffs[3]:.2f}x³ + {coeffs[2]:.2f}x² + {coeffs[1]:.2f}x + {coeffs[0]:.2f}')
        plt.legend()
        plt.draw()
        
        print(f'Equation of the curve: y = {coeffs[3]:.2f}x³ + {coeffs[2]:.2f}x² + {coeffs[1]:.2f}x + {coeffs[0]:.2f}')

# Set up plot
fig, ax = plt.subplots(figsize=(10, 8))  # Increase figure size
ax.set_xlim(-20, 20)  # Expand x-axis range
ax.set_ylim(-20, 20)  # Expand y-axis range
ax.axhline(0, color='black', linewidth=1)  # Add x-axis
ax.axvline(0, color='black', linewidth=1)  # Add y-axis
ax.set_title("Draw freely to generate a cubic equation")
fig.canvas.mpl_connect('motion_notify_event', on_move)
fig.canvas.mpl_connect('button_release_event', on_release)
plt.show()
