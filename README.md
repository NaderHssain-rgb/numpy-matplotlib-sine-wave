# NumPy + Matplotlib Sine Wave 📈

Beginner Python practice project demonstrating how to create and customize a **Sine Wave** using **NumPy** and **Matplotlib**.

## 📌 Project Overview

This project demonstrates how NumPy can be used to generate mathematical data and how Matplotlib can be used to visualize that data.

The project creates a Sine Wave and customizes its appearance using different Matplotlib options.

The project covers:

* Importing NumPy
* Importing Matplotlib
* Creating evenly spaced values with `np.linspace()`
* Calculating sine values with `np.sin()`
* Creating a Line Chart
* Customizing line style
* Customizing line color
* Changing line width
* Adding a chart title
* Adding X-axis and Y-axis labels
* Adding a grid
* Controlling grid transparency with `alpha`
* Setting X-axis limits
* Setting Y-axis limits

## 🛠️ Technologies Used

* Python
* NumPy
* Matplotlib

## 📂 Project Structure

```text
numpy-matplotlib-sine-wave/
│
├── numpy_matplotlib_sine_wave.py
├── sine_wave.png
├── requirements.txt
└── README.md
```

## 🖼️ Visual Preview

The program generates a customized Sine Wave using NumPy and Matplotlib.

![Sine Wave Preview](sine_wave.png)

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/numpy-matplotlib-sine-wave.git
```

Move into the project directory:

```bash
cd numpy-matplotlib-sine-wave
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 📋 Requirements

```text
numpy
matplotlib
```

## ▶️ How to Run

Run the Python file:

```bash
python numpy_matplotlib_sine_wave.py
```

The program will generate and display a customized Sine Wave.

## 📐 Creating the Data

The X values are created using NumPy:

```python
x = np.linspace(0, 10, 50)
```

This creates 50 evenly spaced values between 0 and 10.

The Y values are calculated using:

```python
y = np.sin(x)
```

This calculates the sine of each value in `x`.

## 📈 Creating the Sine Wave

The Sine Wave is created using Matplotlib:

```python
plt.plot(
    x,
    y,
    linestyle="-.",
    color="green",
    linewidth=5
)
```

### Line Style

```python
linestyle="-."
```

Creates a dash-dot line.

### Line Color

```python
color="green"
```

Sets the line color to green.

### Line Width

```python
linewidth=5
```

Controls the thickness of the line.

## 🏷️ Chart Title and Labels

The chart title is added using:

```python
plt.title("Sine Wave")
```

The X-axis is labeled using:

```python
plt.xlabel("X")
```

The Y-axis is labeled using:

```python
plt.ylabel("Sin(X)")
```

## 🔲 Grid

A grid is added to make the chart easier to read:

```python
plt.grid(
    True,
    color="red",
    linestyle="--",
    alpha=0.5
)
```

### `alpha`

The `alpha` parameter controls transparency.

```text
0 → fully transparent
1 → fully visible
```

In this project:

```python
alpha=0.5
```

creates a semi-transparent grid.

## 📏 Axis Limits

The visible X-axis range is controlled with:

```python
plt.xlim(2, 8)
```

The visible Y-axis range is controlled with:

```python
plt.ylim(-0.5, 1)
```

These functions control which part of the graph is visible.

## 🔑 Important Functions

| Function             | Purpose                       |
| -------------------- | ----------------------------- |
| `np.linspace()`      | Creates evenly spaced values  |
| `np.sin()`           | Calculates sine values        |
| `plt.figure()`       | Creates/configures the figure |
| `plt.plot()`         | Creates a Line Chart          |
| `plt.title()`        | Adds a chart title            |
| `plt.xlabel()`       | Labels the X-axis             |
| `plt.ylabel()`       | Labels the Y-axis             |
| `plt.grid()`         | Adds a grid                   |
| `plt.xlim()`         | Sets X-axis limits            |
| `plt.ylim()`         | Sets Y-axis limits            |
| `plt.tight_layout()` | Improves the layout           |
| `plt.show()`         | Displays the chart            |

## 🎯 Learning Goals

After completing this project, you should understand:

* How NumPy generates numerical data
* How `np.linspace()` works
* How `np.sin()` creates sine values
* How to visualize mathematical functions
* How to create Line Charts with Matplotlib
* How to customize line styles
* How to customize line width and color
* How to add and customize grids
* How to control chart limits

## 🚀 Future Improvements

Possible improvements:

* Create Cosine Wave
* Compare Sine and Cosine Waves
* Add markers to the data points
* Experiment with different line styles
* Change the number of points
* Create multiple mathematical functions
* Save the generated chart as an image
* Add more Matplotlib customization

## 👨‍💻 Author

Nader

## 📄 License

This project is created for learning and practice purposes.
