#!/usr/bin/env python3


# Define the E48 row as a list of standard resistor values
E48 = [1.00, 1.05, 1.10, 1.15, 1.21, 1.27, 1.33, 1.40, 1.47, 1.54, 1.62, 1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74, 2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87, 5.11, 5.36, 5.62, 5.90, 6.19, 6.49, 6.81, 7.15, 7.50, 7.87, 8.25, 8.66, 9.09, 9.53]
Resistors = sorted([round(E48[i] * 10**j * 1000) for i in range(len(E48)) for j in range(3)])  # E48 resistors in Ohm, from 1 kOhm to 953 kOhm


#############################
# Exercise 1, A: Attenuator #
#############################

print("Exercise 1, A")

# Define the amplitude of the input signal:
U_in = 9  # in Volts
# Define the desired amplitude of the output signal:
U_out = 1.5  # in Volts

# TODO: Simulate the circuit, because I don't know where I messed up that calculation!!!
# Calculate the required attenuation factor.
U_2 = U_out
U_1 = U_in - U_2
R_factor = U_1 / U_2  # as explained in the preparation material
print("Looking for attenuation factor:", R_factor)

# find two resistors where the ratio R1 / R2 is as close as possible to R_factor
best_R1 = Resistors[0]
best_R2 = Resistors[0]

for r1 in Resistors:
    for r2 in Resistors:
        if abs((r1 / r2) - R_factor) < abs((best_R1 / best_R2) - R_factor):
            best_R1 = r1
            best_R2 = r2

print(f"Best resistor values for the attenuator: R1 = {best_R1} Ohm, R2 = {best_R2} Ohm")
print(f"Achieved attenuation factor: {best_R1 / best_R2}")


########################################
# Exercise 1, B: Capacitive Attenuator #
########################################

print("\nExercise 1, B")


# Since there is no real list of available capacitors,
# And we also want to include the trimmer, which allows for some variation,
# I just looked the values up. There is no better way to do this.
#
# There is not even a single reason to use python for this exercise ...

C_1 = 470  # pf
C_2 = 82  # pF
# C_2 is arrached in parallell to an scilloscope with an input capacitance of about 15 pF.
C2_eff = 97  # pF
# When we multiply with the ratio, we get: C_1 = 485 pF
# So we choose the 680 pF Capacitor with the 6 - 30 pF Trimmer in parallel to adjust for the correct value.
print(f"Chosen capacitor values for the capacitive attenuator: C1 = {C_1} pF, C2 = {C_2} pF (with scope input capacitance considered: C2 = {C2_eff} pF)")


##################################
# Exercise 1, C: Offset Addition #
##################################

print("\nExercise 1, C")

# Calculate the offset voltage, based on the formula provided in the preparation material.
U_offset = 1.5  # Volt
U_generate = U_offset * (1 + (best_R2 / best_R1))
print(f"To achieve an offset of {U_offset} V, the generated voltage must be: {U_generate} V")

# Find the best resistor values to generate this voltage from a N V supply.
N = 12  # Volt

best_R3 = Resistors[0]
best_R4 = Resistors[0]

for r3 in Resistors:
    for r4 in Resistors:
        U_out_generated = N * (r4 / (r3 + r4))
        U_out_best = N * (best_R4 / (best_R3 + best_R4))
        if abs(U_out_generated - U_generate) < abs(U_out_best - U_generate):
            best_R3 = r3
            best_R4 = r4

print(f"Best resistor values for the offset generator: R3 = {best_R3} Ohm, R4 = {best_R4} Ohm")
U_out_final = N * (best_R4 / (best_R3 + best_R4))
print(f"Achieved generated voltage: {U_out_final} V")


###############################################
# Exercise 2, A and 3, B: inverting Amplifier #
###############################################

print("\nExercise 2, A and 3, B")

# Find two resistors with the Ratio R_1 / R_2 = 2
# One of them can be one of the four previously discovered resistors
# To reduce the number of resistors that need to be bought for the lab

"""
desired_ratio = 2
R_ex3 = Resistors[0]
R_other = best_R1

for r in Resistors:
    for other in [best_R1, best_R2, best_R3, best_R4]:
        if abs((r / other) - desired_ratio) < abs((R_ex3 / R_other) - desired_ratio):
            R_ex3 = r
            R_other = other

print(f"Best resistor values for the inverting amplifier: R_ex3 = {R_ex3} Ohm, R_other = {R_other} Ohm, achieved ratio: {R_ex3 / R_other}")
"""
# It turns out, that the result of this calculation is:
#   - R_ex3 = 22.6kΩ
#   - R_other = 11.5kΩ
# But: For the next exercise we need a 1.15kΩ resistor, and we already have the 2.26kΩ
# resistor, which have the same ratio. Therefore: Use them instead (*10e-1)
print("Best resistor values for the inverting amplifier: R_1 = 2260 Ohm, R_2 = 1150 Ohm, achieved ratio: {R_ex3 / R_other}")


####################################
# Exercise 2, C: Gain Verification #
####################################

# result from last exercise:
R_1 = 2260  # Ohm
N = 1  # V
N_max = 9  # V (before the saturation starts)

# find 5 equi-distantial gain values between N and N_max (endpoints not included)
print("\nExercise 2, C")
gain_values = [2, 3.5, 5, 7.5, 9]
print("Gain values to be tested:", gain_values)

# calculate the value for resistor R_2 for each gain value, using the formula: Gain = 1 + (R_1 / R_2)
resistors = [R_1 / (gain - 1) for gain in gain_values]
print("Resistor values for the gain verification:", resistors)
print(f"The potentiometer should have a range from {min(resistors)} Ohm to {max(resistors)} Ohm")


####################################
# Exercise 3, C: summing Amplifier #
####################################

print("\nExercise 3, C")

# The input signal with an amplitude of + - 9V should be reduced
# to 0V ... 3V
# We can achieve this by using the inverting amplifier from Ex 3, B
# And add an offset of 1,5V with the summing amplifier.

# Define the amplitude of the input signal:
U_in = 9  # in Volts
# Define the desired amplitude of the output signal:
U_out = 1.5  # in Volts

# Calculate the required attenuation factor.
# U_1 = U_out - U_2
# U_2 = U_out
R_factor = U_in / U_out  # = U_1 / U_2 as explained in the preparation material
print("Looking for attenuation factor:", R_factor)

# find two resistors where the ratio R1 / R2 is as close as possible to R_factor
best_R1 = Resistors[0]
best_R2 = Resistors[0]

for r1 in Resistors:
    for r2 in Resistors:
        if abs((r1 / r2) - R_factor) < abs((best_R1 / best_R2) - R_factor):
            best_R1 = r1
            best_R2 = r2

print(f"Best resistor values for the attenuator: R1 = {best_R1} Ohm, R2 = {best_R2} Ohm")
print(f"Achieved attenuation factor: {best_R1 / best_R2}")

# Calculate the right resistor for the offset
N = 12  # V

# Use the formula: U_offset = N * (R_2 / R_add)
R_add = best_R2 * (N / U_out)

# find the best resistor in the E48 series that is closest to R_add
best_R_add = Resistors[0]
for r in Resistors:
    if abs(r - R_add) < abs(best_R_add - R_add):
        best_R_add = r

print(f"Best resistor value for the offset: R_add = {best_R_add} Ohm, achieved voltage: {N * (best_R2 / best_R_add)} V")

