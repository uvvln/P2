# Ideales und reales Gas

## Messung des Adiabatenexponent nach der Methode von [Rüchardt](https://de.wikipedia.org/wiki/R%C3%BCchardt-Experiment)

> Diese Methode zur Bestimmung von $\kappa$ ist nach [Eduard Rüchardt](https://de.wikipedia.org/wiki/Eduard_R%C3%BCchardt) benannt. **Sie verbindet die Bestimmung thermodynamischer Größen mit Messprinzipien, die Sie bereits aus der Mechanik kennen.** 

Bei dieser Methode schwingt ein Pfropfen auf einem Luftpolster, das durch den Schwingungsvorgang in **adiabatische Kompression und Expansion** versetzt wird. Nach der Adiabatengleichung (siehe Gleichung **(2) [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Ideales_und_reales_Gas/doc/Hinweise-Thermodynamik.md)**) gilt in diesem Fall: 
$$
\begin{equation*}
p\,V^{\kappa} = const.
\end{equation*}
$$
Für differentielle Druck- und Volumenänderungen ergibt sich daraus:

$$
\begin{equation}
\begin{split}
&\frac{\mathrm{d}p}{\mathrm{d}V} = -const.\,\kappa\,V^{-\kappa-1} \\
&\hphantom{\frac{\mathrm{d}p}{\mathrm{d}V}}= -\kappa\frac{p}{V}; \\
&\\
&\mathrm{d}p = -\kappa\frac{p}{V}\,\mathrm{d}V. \\
\end{split}
\end{equation}
$$
Aus der Multiplikation von Gleichung **(1)** mit dem Rohrinnenquerschnitt $A$ ergibt sich die auf den Pfropfen wirkende Kraft und nach dem zweiten Newtonschen Axiom eine lineare **Schwingungsgleichung für die Bewegung des Pfropfens**:

$$
\begin{equation}
\begin{split}
&\mathrm{d}F = -\kappa\frac{p}{V}A^{2}\,\mathrm{d}x; \\
&\\
&\text{mit}\\
&\\
&\mathrm{d}p = \frac{\mathrm{d}F}{A};\qquad \mathrm{d}V = A\,\mathrm{d}x;\\
&\\
&m\,\ddot{x} = -\kappa\frac{p}{V}A^{2}\,x,
\end{split}
\end{equation}
$$
wobei $m$ der Masse des Pfropfens entspricht. 💡 An dieser Stelle nehmen wir die Näherung vor, dass sich $p$ und $V$ durch die Bewegung des Pfropfens aus seiner Ruhelage nur geringfügig ändern ($p\approx const.,\ V\approx const.$). Aus Gleichung **(2)** lässt sich die Periode 

$$
\begin{equation}
T_{\Omega} = 2\pi\sqrt{\frac{m\,V}{\kappa\,p\,A^{2}}}
\end{equation}
$$
der Schwingung ableiten, woraus sich $\kappa$ bestimmen lässt:

$$
\begin{equation*}
\kappa = \left(\frac{2\pi}{T_{\Omega}}\right)^{2}\frac{m\,V}{p\,A^{2}}.
\end{equation*}
$$
💡 Beachten Sie den Index $T_{\Omega}$ für die Periode der Schwingung, um Verwechslungen mit der Temperatur zur vermeiden.

### Entfernen der Kugel aus der Flasche

⚠️ Wenn Sie für diesen Versuch den **Originalaufbau nach Rüchardt** verwenden heben Sie am Ende des Schwingungsvorgangs die ganze Flasche an und kippen Sie diese vorsichtig um, so dass die Kugel aus der Schwingungsröhre gleitet. Fangen Sie die diese z.B. in einer sauberen Kunststoffschale auf. 

Sollten Sie den rechten Zeitpunkt verpassen, um die Kugel noch aus der Schwingungsröhre zu entfernen, kann es vorkommen, dass diese in die Flasche fällt. In einem solchen Fall müssen Sie die **Schwingungsröhre aus der Flasche entfernen**, um an die Kugel heranzukommen. ⚠️ Dabei müssen Sie besondere Acht haben, damit die Röhre nicht beschädigt wird. 

Gehen Sie dazu wie folgt vor: 

- Ergreifen Sie die Schwingungsröhre an ihrem oberen Ende und lenken Sie sie leicht aus, so dass sie mit der Symmetrieachse der Flasche einen spitzen Winkel bildet. 
- Bewegen Sie das obere Ende der Schwingungsröhre dann einige mal vorsichtig im Kreis, so dass sich der Gummistopfen vom äußeren Rand der Röhre löst. 
- Sie sollten daraufhin die Röhre vorsichtig nach oben aus dem Stopfen herausziehen können.

## Erwartung

Was wir an dieser Stelle von Ihnen erwarten:

- :white_check_mark: Sie können die Methode von Rüchardt zur Bestimmung von $\kappa$ **beschreiben**. 
- :white_check_mark: Sie können Gleichung **(1)** aus der entsprechenden Adiabatengleichung und daraus die **Schwingungsgleichung (2) für die Auslenkung des Pfropfens ableiten**.

## Testfragen

1. Verstärken oder kompensieren sich die Abweichungen von der Annahme $p=const.,\ V=const.$?
2. Welchen Einfluss erwarten Sie auf die Schwingung?

---

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Ideales_und_reales_Gas/README.md)



