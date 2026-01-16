"""
Error propagation using the Monte Carlo method for determining the uncertainty 
of the heat capacity (Experiment on heat capacity in KIT physics lab course 2)
"""

import numpy as np
import matplotlib.pyplot as plt

def heat_capacity( T, par):
    """
    Function to determine the heat capacitance based on an empirical fit 
    of the temperature curve as a function of time T(t) = a*exp[-t/b0]+c.
    This results in \dot T(T) = a*b*((T-c)/a^(1-1/b))"""
    temp = np.dstack( [T]*len(par) )
    U = par[:,0]
    I = par[:,1]
    a = par[:,2]
    b = par[:,3]
    c = par[:,4]
    b0 = par[:,5]
    c0 = par[:,6]
    Tdott = a * b * ( ( temp - c )/ a )**( 1 - 1/b )
    Tdot0 = -( temp - c0 )/ b0
    return U * I /( m * ( Tdott - Tdot0 ) )

def heat_cap_1D( T, U, I, m, a, b, c, b0, c0 ):
    Tdott = a * b * ( ( T - c )/ a )**( 1 - 1/b )
    Tdot0 = -( T - c0 )/ b0
    return U * I /( m * ( Tdott - Tdot0 ) ) 

"""
Assumption: parameters par are uncorrelated and Gaussian distributed with known 
standard deviation.
Consequence: the standard deviation of any function of the parameters can be 
estimated by "rolling the dice" (i.e., drawing random numbers) for the 
parameters and plugging in the values into the function
"""
U, sigma_U =   9.9, 0.5     # in V
I, sigma_I =  1.91, 0.05    # in A
m, sigma_m = 0.338, 0.0005  # in kg
a, sigma_a =  2.0969, 0.031
b, sigma_b =  0.5858, 0.0016
c, sigma_c = 12.8987, 0.3952
a0, sigma_a0 =  -208.0134,  0.2874
b0, sigma_b0 = 19456.7078, 62.9674
c0, sigma_c0 =   295.8593,  0.1504

par   = np.array( [U, I, a, b, c, b0, c0 ] )
sigma = np.array( [ sigma_U, sigma_I, sigma_a, sigma_b, sigma_c, sigma_b0, sigma_c0 ] )

# -----------------------------------------------------------------------------
# Draw random numbers
#
# Step 1: Initiate random generator
rng = np.random.default_rng( 42 )

# Step 2: Draw 10000 random numbers for the parameters
ntoys = 10000
rnd_par = rng.normal( par, sigma, size=(ntoys,len(par)) )

# Step 3: Plug the random numbers into the function
npoints = 10000
T0 = 273.15 
T = np.linspace( 80, 300, npoints )
rnd_heat_cap = heat_capacity( T, rnd_par )
# Step 4: The function returns an array of randomized function values, the 
#         standard deviation is a measure of the uncertainty 
mean      = np.mean( rnd_heat_cap, axis=2 )
quantiles = np.quantile( rnd_heat_cap, [0.1585,0.5,0.8415], axis=2 )
std       = np.std( rnd_heat_cap, axis=2, ddof=1 )

# Step 5: Plot function values as curve and area around central 68.3% interval 
#         as band
fig,ax = plt.subplots()
ax.plot( T, heat_cap_1D( T,U,I,m,a,b,c,b0,c0 ) )
ax.fill_between( T, quantiles[0][0], quantiles[2][0], alpha=0.2 )
ax.set_xlabel(r'Temperatur ($\mathrm{K}$)') 
ax.set_ylabel(r'Spezifische Wärmekapazität ($\mathrm{J/kg\ K}$)')

idx = np.searchsorted( T, T0 )
print( T[idx], heat_cap_1D( T[idx],U,I,m,a,b,c,b0,c0), quantiles[1][0][idx], quantiles[0][0][idx]-quantiles[1][0][idx], quantiles[2][0][idx]-quantiles[1][0][idx] )
plt.show()
