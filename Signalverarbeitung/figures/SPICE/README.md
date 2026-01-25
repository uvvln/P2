# Simulations

This directory contains some SPICE simulations to generate the pictures for the documentation.

## Prerequisites

Install the Program `Ngspice`

## How to use?

0. Create the directory `~/tmp`, otherwise the plots cannot be saved
1. Open a terminal
2. Type `ngspice <filename>.cir` to run a simulation file.
3. A window which plots the relevant results should appear
4. In this window, use the "save as SVG" option to save the plot as an SVG file.
5. Quit ngspice by typing `exit` into the prompt.
6. Edit this SVG file to replace the dark background with a white one and adjust the colors if needed. You have no influence on the color of the plots from ngspice, so you have to change them manually.

**Whenever you think abut changing small detail of the plots (e.g. the names of the plotted signals in the plot legend) consider doing this with inkscape first!**

## Use imagemagick to invert the color:
```bash
magick input.svg -channel RGB -negate output.png
```
This might work sometimes

## Notes

- When editing the file in VIM, use ":set syntax=spice" at the beginning for better syntax highlighting.
