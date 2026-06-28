# Lecture 25: Plotting

## 1. Introduction to Plotting & Matplotlib

- **Purpose:** Visualizing data helps expose trends, identify anomalies, and pose analytical questions that are difficult to see in raw numerical data. It serves as a prime example of leveraging an existing professional library rather than writing operations from scratch.


- **Matplotlib:** Python's standard graphing library can be easily integrated using the syntax: `import matplotlib.pyplot as plt`.

## 2. Core Plotting Principles & Commands

- **Basic Line Plots:** Created using `plt.plot(x_values, y_values)` where arguments must be sequences or lists of the same length. Points are plotted sequentially and connected by lines.


- **Order Matters:** If data points are provided in an arbitrary or unordered sequence, standard line plots will look chaotic because they stringently connect points consecutively based on list indexing.


- **Scatter Plots:** To avoid messy connection lines on unordered data, `plt.scatter(x_values, y_values)` can be used to isolate individual data points.


- **Formatting Customization:** Matplotlib allows developers to explicitly control markers (e.g., `o`, `^`, `*`), line styles (e.g., solid `-`, dashed `--`), colors (e.g., `b`, `g`, `r`), and line widths. Labels and grids can be handled using `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, and `plt.grid()`.

## 3. Handling Scale Differences

- **The Scale Problem:** When plotting functions with drastically different orders of growth (e.g., linear vs. exponential) on a single plot, lower-order graphs become squished and entirely unreadable.

- **Solutions:**
    1. **Multiple Windows:** `plt.figure('name')` can be used to split datasets into entirely distinct frames or windows.
    2. **Logarithmic Scaling:** Changing axes to a log scale allows linear visual growth to represent exponential increases, making wide-ranging historical data trends visible.
    3. **Subplots:** Plotting multiple graphs side-by-side or stacked inside uniform layouts.


## 4. Real-World Case Studies Included

The lecture exercises these tools across three extensive data visualizations:

- **US Population Growth:** Demonstrates how changing to a log scale uncovers distinct exponential growth patterns and showcases the distinct historical impacts of major events like the American Civil War and WWII.

- **Benford's Law (Country Populations):** Investigates the strict logarithmic distribution frequencies of the first digit in complex empirical datasets.

- **US Cities Temperature Analysis:** Tracks 55 years of daily weather across 21 cities. This section highlights the necessity of **fixing identical Y-axis ranges** (`ylim`) to properly compare structural variations (e.g., contrasting the flat stability of San Diego weather against the volatile seasonal ranges of Boston).