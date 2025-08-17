
# Interactive Data Analysis with Marimo
# Author: 23f2003677@ds.study.iitm.ac.in

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt

# Top-level interactive slider widget
# Cell 1: Interactive slider widget for correlation strength
slider = mo.ui.slider(0, 1, value=0.5, step=0.01, label="Correlation strength")
## The variable 'slider.value' is used in dependent cells below

# Cell 1: Data generation and plot, depends on slider value
# The plot updates interactively when the slider is moved
np.random.seed(42)
x = np.random.normal(size=100)
y = slider.value * x + (1 - slider.value) * np.random.normal(size=100)
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.7)
ax.set_title(f"Correlation: {slider.value:.2f}")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.close(fig)
mo.output(fig)

# Cell 2: Dynamic markdown output based on slider
# This cell displays analysis text that updates with the slider
if slider.value < 0.3:
    msg = "Low correlation between X and Y."
elif slider.value < 0.7:
    msg = "Moderate correlation between X and Y."
else:
    msg = "High correlation between X and Y."
mo.md(f"### Analysis\nCorrelation strength: **{slider.value:.2f}**\n{msg}")

# Comments:
# - The slider widget 'slider' controls the correlation strength interactively.
# - The plot and markdown cells update automatically when the slider is moved.
# - All cells are self-documenting and interactive.
