import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def plot_energy_loss(ax, label):
    """
    Plot mean relative energy loss after 6mm Hg atmosphere 
    
    Plot as function of the temperature in deg Celsius
    
    """
    ax.set_xlabel(r"$T\,[^{\circ}\mathrm{C}]$")
    ax.set_ylabel(r"$\Delta E/E$")
    ax.set_xlim(0., 225.)
    ax.set_ylim(1e-10,  3*10e-1)
    ax.set_yscale("log")
    ax.grid(axis='both', linewidth=1, linestyle="--", color='lightgray')
    ## Get the data
    df = pd.read_csv("Mittlerer-Energieverlust.csv")
    plot,=ax.plot(df["T"], df["dW/W"], 
        linewidth=2, 
        color="darkmagenta", 
        label="rel. Energieverlust nach 6 mm Hg-Dampf"
        )
    # Add a legend and show plot
    ax.legend(
        handles=[plot], 
        bbox_to_anchor=(0., 0.80, 1., 0.2), 
        loc="lower left", 
        ncol=1
        )
    # Add figure label
    ax.text(205, 5e-10, label, fontsize=12, fontweight="bold")

def plot_interaction_length(ax, label):
    """
    Plot mean interaction length after 6mm Hg atmosphere 
    
    Plot as function of the temperature in deg Celsius
    
    """
    #ax.set_xlabel(r"$T\,[^{\circ}\mathrm{C}]$")
    ax.set_ylabel(r"$\lambda\,[\mathrm{mm}]$")
    ax.set_xlim(0., 225.)
    ax.set_ylim(10e-3,  10e2)
    ax.set_yscale("log")
    ax.grid(axis='both', linewidth=1, linestyle="--", color='lightgray')
    ## Get the data
    df = pd.read_csv("Mittlere-freie-Weglaenge.csv")
    plot,=ax.plot(df["T"], df["lambda"], 
        linewidth=2, 
        color="darkblue", 
        label=r"Mittlere freie Weglänge $\lambda$ in Hg-Dampf"
        )
    # Add a legend and show plot
    ax.legend(
        handles=[plot], 
        bbox_to_anchor=(0., 0.80, 1., 0.2), 
        loc="lower right", 
        ncol=1
        )
    # Add figure label
    ax.text(205, 2e-1, label, fontsize=12, fontweight="bold")

def plot_vapor_pressure(ax, label):
    """
    Plot vapor pressur of Hg 
    
    Plot as function of the temperature in deg Celsius
    
    """
    ## Predefine figure and axes layout
    #ax.set_xlabel(r"$T\,[^{\circ}\mathrm{C}]$")
    ax.set_ylabel(r"$p_{\mathrm{Hg}}\,[\mathrm{mbar}]$")
    ax.set_xlim(0., 225.)
    ax.set_ylim(1e-4,  1e2)
    ax.set_yscale("log")
    ax.grid(axis='both', linewidth=1, linestyle="--", color='lightgray')
    ## Get the data
    df = pd.read_csv("Dampfdruck.csv")
    plot,=ax.plot(df["T"], df["Druck"], 
        linewidth=2, 
        color="darkred", 
        label="Dampfdruck für Hg"
        )
    # Add a legend and show plot
    ax.legend(
        handles=[plot], 
        bbox_to_anchor=(0., 0.83, 1., 0.2), 
        loc="lower left", 
        ncol=1
        )
    # Add figure label
    ax.text(205, 2e-4, label, fontsize=12, fontweight="bold")
    
fig = plt.figure(figsize=(6., 10.))
gs  = fig.add_gridspec(3, hspace=0.05)
axes= gs.subplots(sharex=True)
#fig, axes = plt.subplots(3,1, figsize=(6., 10.), sharex=True)
plot_vapor_pressure(axes[0], "(a)")
plot_interaction_length(axes[1], "(b)")
plot_energy_loss(axes[2], "(c)")
# Hide x labels and tick labels for all but bottom plot.
for ax in axes:
    ax.label_outer()
plt.savefig("Energieverlust.png", bbox_inches="tight")
plt.show()
