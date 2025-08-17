# Interactive Data Analysis with Marimo
# Author: 23f2003677@ds.study.iitm.ac.in

import marimo
import numpy as np
import matplotlib.pyplot as plt

mo = marimo.App()

# Cell 1: Slider widget for variable selection
@mo.cell
def slider_cell():
    # Select correlation strength
    corr = mo.slider(label="Correlation strength", min=0, max=1, step=0.01, value=0.5)
    return corr

# Cell 2: Data generation and plot, depends on slider value
@mo.cell
def plot_cell(corr):
    # Generate synthetic data with variable correlation
    np.random.seed(42)
    x = np.random.normal(size=100)
    y = corr * x + (1 - corr) * np.random.normal(size=100)
    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.7)
    ax.set_title(f"Correlation: {corr:.2f}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.close(fig)
    return mo.output(fig)

# Cell 3: Dynamic markdown output based on slider
@mo.cell
def markdown_cell(corr):
    # Document the relationship interactively
    if corr < 0.3:
        msg = "Low correlation between X and Y."
    elif corr < 0.7:
        msg = "Moderate correlation between X and Y."
    else:
        msg = "High correlation between X and Y."
    return mo.md(f"### Analysis\nCorrelation strength: **{corr:.2f}**\n{msg}")

# Comments:
# - The slider in Cell 1 controls the correlation strength.
# - Cell 2 generates and plots data based on the slider value.
# - Cell 3 provides dynamic markdown analysis based on the slider state.
# - All cells are self-documenting and interactive.

if __name__ == "__main__":
    mo.run()
