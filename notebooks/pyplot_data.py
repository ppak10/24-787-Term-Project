import matplotlib.pyplot as plt
import numpy as np

def plot_observed_vs_predicted(
    labels,
    prediction,
    color=(0, 0, 0, 0.5),
    title="Observed vs. Predicted Critical Temperature"
):
    """
    Plots the observed critical temperature vs. the predicted critical
    temperature.
    """

    # Plot observed temperatures vs predicted temperatures with scatter plot.
    plt.scatter(labels, prediction, color=color)
    plt.title(title)
    plt.xlabel("Observed Critical Temperature (K)")
    plt.ylabel("Predicted Critical Temperature (K)")

    # Plot linear trendline
    z = np.polyfit(labels.ravel(), prediction, 1)
    p = np.poly1d(z)
    plt.plot(labels, p(labels))
    plt.show()
