# Graph Art

A collection of Python scripts for creating artistic mathematical visualizations using matplotlib. Generate minimalist, high-quality plots of mathematical functions with clean aesthetics.

## What It Does

### Graph.py
Plots explicit mathematical functions with a minimalist aesthetic. Uses a subtle gray grid and line styling to create clean, professional-looking function plots. Simply define any lambda function and visualize it.

**Example:** Plotting a Gaussian function `e^(-x²)`

![Gaussian Function](function_plot.png)

### Heart_Graph.py
Creates artistic plots of implicit functions. Features a heart shape generator using the mathematical equation `(x²+y²-1)³ - x²y³ = 0`, with support for rotation and custom styling.

**Example:** Heart-shaped implicit function plot

![Heart Function](heart_function_plot.png)

### Equation Finder.py
An interactive tool that lets you draw freely on a canvas with your mouse, then automatically fits a cubic polynomial equation to your drawing. After releasing the mouse button, it displays both the drawn curve and the fitted equation.

**Features:**
- Draw freehand curves with your mouse
- Automatic cubic polynomial fitting
- Real-time equation display
- Visual comparison between your drawing and the fitted curve

**Example output:** `y = ax³ + bx² + cx + d` where coefficients are calculated from your drawing
