# Messwerte:
#
# Messplatz
M        = (151, 152, 153)
# Umfang mit Maßband (in cm)
U        = ( 70,  68,  68)
# Hoehe mit Maßband in cm
h        = ( 30,  30,  30)
# Dicke der Glaswand mit Laserentfernungsmesser (in cm)
DeltaR   = (0.4, 0.6, 0.6)
# Krümmungsradius am Deckel mit Maßband (in cm)
r        = ( 10,  12,  12)

from numpy import pi

# Innerer Radius der Glocke (in cm)
def R(i): return U[i]/2/pi-DeltaR[i]
# Unkorrigiertes Volumen der Glockes als Zylinder (in cm**3) 
def V(i): return pi*R(i)**2*h[i]
# Korrigiertes Volumen der Glocke als abgerundeter Zylinder (in Liter)
for i in [0, 1, 2]:
    Vol = (V(i)-(1-pi/4)*r[i]**2)/1000.
    print(M[i], Vol)

# Uncertainties: 
# dU = +/-5   mm   --> +/- 0.15 l
# dh = +/-1   mm   --> +/- 0.20 l 
# dR = +/-2.5 mm   --> +/- 0.07 l
# dr = +/-2.5 mm   --> negligible
# Sums to +/- 0.26 l
