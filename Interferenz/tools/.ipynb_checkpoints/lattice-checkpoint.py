#!/usr/bin/python3
"""
Diffraction and interference at single, double slit and lattice

Usage:

python3 sinc.py
"""
import matplotlib.pyplot as plt
import numpy as np

def lattice(x, b=150., l=200., g=200., N=2):
    """
    x: alpha (rad)
    b: slit width (nm)
    l: wavelength (nm)
    g: lattice constant (nm)
    N: number of illuminated slits
    """
    arg = np.pi/l*x
    ## Spaltfunktion
    fS  = (np.sin(b*arg)/(b*arg))**2
    ## Gitterinterferenzfunktion
    fG  = 1/N/N*(np.sin(N*g*arg)/np.sin(g*arg))**2
    return fS*fG

# Creating a list of points in x from -10 to 10 to display the functions of 
# choice
def plot(b=250., l=200, g=200, N=2):
    x = np.linspace(-10.2, 10.2, 2000)
    plt.plot(x, lattice(x=x, b=b, g=g, N=N),
        color="black", 
        linestyle="solid",
        linewidth=1.5, 
        label=r"Intensität am Gitter"
        )
    plt.plot(x, lattice(x=x, b=b, l=l, g=1., N=1),
        color="black", 
        linestyle="dashed",
        linewidth=1., 
        label=r"Beugung am Spalt"
        )
    # Customize the figure
    plt.xlabel(r'Position (cm)') 
    plt.ylabel(r'Intensität') 
    plt.legend(bbox_to_anchor=(0., 1., 1., 0.1), loc="lower left", ncol=2, mode="expand")
    # Save to pdf
    plt.savefig("lattice.png")    
    # Show the plot with a rendering machine
    #plt.show()
plot(b=1., l=200., g=120., N=5)

