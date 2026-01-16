#!/usr/bin/python3
"""
...
"""
import matplotlib.pyplot as plt
import numpy as np

# Creating a list of points in x from -10 to 10 to display the functions of 
# choice

kappa = np.linspace(-4, 2, 60)
d = np.linspace(0.1, 1, 20)

# Define the functions of choice
def grobVakuum(d=0.1, l=5, kappa=0.6):
    return 135*d**3/l*kappa 
def feinVakuum(d=0.1, l=5, kappa=0.6):
    return grobVakuum(d, l, kappa)+hochVakuum(d, l, kappa)*(1+192*kappa)/(1+237*kappa)
def hochVakuum(d=0.1, l=5, kappa=0.6):
    return 12.1*d**3/l
def interp(d=0.1, l=5, kappa=0.6):
    return 12.1*d**3/l*(1+203*kappa+2780*kappa**2)/(1+237*kappa)

plt.plot(d, grobVakuum(d, kappa=1), 
    color="steelblue", 
    linestyle="solid",
    linewidth=2., 
    label="Hagen-Poiseuille (Grobvakuum)"
    )
plt.plot(d, interp(d, kappa=1), 
    color="indigo", 
    linestyle="dashed",
    linewidth=2., 
    label=r"Interpolation ($d\bar{p}=1.0\ \mathrm{mbar\ cm}$)"
    )
plt.plot(d, feinVakuum(d, kappa=0.5), 
    color="green",
    linestyle="solid",#(0, (5,2,1,2)), 
    linewidth=2., 
    label="Knudsen (Feinvakuum)"
    )
plt.plot(d, interp(d, kappa=0.5), 
    color="darkgreen", 
    linestyle="dashed",
    linewidth=2., 
    label=r"Interpolation ($d\bar{p}=0.5\ \mathrm{mbar\ cm}$)"
    )
plt.plot(d, hochVakuum(d), 
    color="red",
    linestyle="solid",#(0, (5,2,1,2)), 
    linewidth=2., 
    label="Hochvakuum"
    )
plt.plot(d, interp(d, kappa=0.01), 
    color="mediumvioletred", 
    linestyle="dashed",
    linewidth=2., 
    label=r"Interpolation ($d\bar{p}=10^{-2}\ \mathrm{mbar\ cm}$)"
    )


# Customize the figure
#plt.title("Display different functions")
plt.xlabel(r"$d (\mathrm{cm})$")
plt.ylabel(r"$L (\mathrm{l/s})$")
plt.legend()
# Save to pdf
plt.savefig("Knudsen.pdf")    
# Show the plot with a rendering machine
plt.show()

