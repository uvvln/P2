import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from scipy.interpolate import make_interp_spline

def plot_FranckHertz(ax):
    """
    Plot the qualitative course of a Franck Hertz curve     
    """
    ax.set_xlabel(r"$U_{B}\,[\mathrm{V}]$")
    ax.set_ylabel(r"$I_{A}\,[\mathrm{nA}]$")
    ax.set_xlim(0., 18.)
    ax.set_ylim(0., 18.)
    ax.grid(axis='both', linewidth=1, linestyle="--", color='lightgray')
    ## Get the data
    df = pd.read_csv("Franck-Hertz-Kurve.csv")
    X_Y_Spline = make_interp_spline(df["UB"], df["IA"]) 
    # Returns evenly spaced numbers
    # over a specified interval.
    X_ = np.linspace(df["UB"].min(), df["UB"].max(), 250)
    Y_ = X_Y_Spline(X_)
    
    plot,=ax.plot(X_, Y_, 
        linewidth=2, 
        color="black", 
        label="Auffängerstrom ($I_{A}$)"
        )
    # Add a legend and show plot
    ax.legend(
        handles=[plot], 
        bbox_to_anchor=(0., 0.90, 1., 0.2), 
        loc="lower left", 
        ncol=1
        )
    
fig, ax = plt.subplots(figsize=(6., 6.))
plot_FranckHertz(ax)
plt.savefig("FranckHertzKurve.png", bbox_inches="tight")
plt.show()
