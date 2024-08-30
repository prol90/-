import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import pandas as pd

# 1. Визуализация с использованием Matplotlib
def plot_with_matplotlib():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.plot(x, y, label='Sine Wave')
    plt.title('Sine Wave using Matplotlib')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.show()

# 2. Визуализация с использованием Seaborn
def plot_with_seaborn():
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [23, 45, 56, 78]
    })

    sns.barplot(x='Category', y='Values', data=data)
    plt.title('Bar Plot using Seaborn')
    plt.show()

# 3. Визуализация с использованием Plotly
def plot_with_plotly():
    data = pd.DataFrame({
        'X': [1, 2, 3, 4, 5],
        'Y': [10, 14, 19, 25, 30]
    })

    fig = px.line(data, x='X', y='Y', title='Line Plot using Plotly')
    fig.show()

# Основная функция, которая вызывает все три визуализации
def main():
    plot_with_matplotlib()
    plot_with_seaborn()
    plot_with_plotly()

if __name__ == "__main__":
    main()
