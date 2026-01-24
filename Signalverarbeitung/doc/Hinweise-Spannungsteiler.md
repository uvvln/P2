# Hinweise für den Versuch **Signalverarbeitung**

## Spannungsteiler

Ein Spannungsteiler, wie in **Abbildung 1 (a)** zu sehen, ist eine einfache Schaltung, die aus zwei Widerständen in Reihe aufgebaut ist und nach dem Ohmschen Gesetz eine Spannung in zwei Teilspannungen aufteilt. Ein elektrischer Widerstand $R$ ist definiert als das Verhältnis von Spannung $U$ zu Strom $I$:
$$
\begin{equation*}
R = \frac{U}{I}.
\end{equation*}
$$
In einer Reihenschaltung von zwei Widerständen $R_{1}$ und $R_{2}$ fließt durch beide Widerstände der gleiche Strom $I$. Die Gesamtspannung $U$ teilt sich in die Teilspannungen $U_{1}$ und $U_{2}$ auf, die jeweils über den Widerständen $R_{1}$ und $R_{2}$ abfallen. Aus der Energieerhaltung folgt, dass die Gesamtspannung die Summe der abfallenden Teilspannungen ist $U_{0} = U_{1} + U_{2}$ und aus der Ladungserhaltung folgt, dass der Strom durch beide Widerstände gleich sein muss:
$$
\begin{equation*}
I = \frac{U_{0}}{R_{1}+R_{2}}.
\end{equation*}
$$
Dabei wurde verwendet, dass der Gesamtwiderstand zweier in Reihe geschalteter Widerstände die Summe der Einzelwiderstände ist: $R=R_{1}+R_{2}$.
Nach dem Ohmschen Gesetz gilt für die Teilspannungen:
$$
\begin{equation*}
U_{2} = R_{2}\,I = R_{2}\,\frac{U_{0}}{R_{1}+R_{2}}.
\end{equation*}
$$
Analog lässt sich auch die Spannung $U_{1}$ berechnen. Aus der Gleichung lässt sich auch ein Zusammenhang erkennen, der für das Verständnis der Schaltungen in diesem Versuch hilfreich ist: Am größeren Widerstand fällt auch die größere Spannung ab.

Der Spannungsteiler kann verwendet werden, um am Abgriff zwischen den beiden Widerständen eine bestimmte Spannung $U_{2}$ zu erzeugen, die kleiner ist als die Eingangsspannung $U_{0}$. In **Abbildung 1 (b)** ist beispielhaft ein Spannungsteiler dargestellt, der am unteren Ende mit der Masse verbunden ist. Die Widerstände wurden so gewählt, dass eine Eingangsspannung von $\pm12 \mathrm{V}$ auf eine Ausgangsspannung von $\pm 3 \mathrm{V}$ reduziert wird. Der Spannungsteiler funktioniert in diesem Fall unabhängig davon, ob die Eingangsspannung positiv oder negativ ist.

---

<img src="../figures/resistive_voltage_divider.png" width="800" style="zoom:100%;"/>

**Abbildung 1**: ((a) Schaltung eines Spannungsteilers mit den an den Widerständen abfallenden Spannungen. (b) Ein Spannungsteiler, um eine gezielte Ausgangsspannung zu erzeugen.)

---

Ein Spannungsteiler ist eine sehr einfache Methode um Spannungen zu reduzieren aber es gibt zwei wichtige Nachteile, die den Einsatzbereich des Spannungsteilers einschränken. Erstens ist der Spannungsteiler keine gute Stromquelle. Wenn wir die Ausgangsspannung verwenden wollen, um ein anderes Bauteil zu versorgen, dann fließt durch dieses Bauteil ein Strom. Das angeschlossene Bauteil lässt sich als ein weiterer Widerstand $R_{L}$, für gewöhnlich "Lastwiderstand" genannt, am Ausgang des Spannungsteilers modellieren (siehe **Abbildung 2**). Der Widerstand $R_{L}$ ändert den Gesamtwiderstand des unteren Zweigs des Spannungsteilers von $R_{2}$ auf den Parallelschaltungswiderstand $R_{p}$:
$$
\begin{equation*}
R_{p} = R_2 \parallel R_L = \frac{R_{2} R_{L}}{R_{2} + R_{L}} \lt R_2.
\end{equation*}
$$
Der Parallelwiderstand ist dabei immer kleiner als der kleinste der beiden Widerstände $R_{2}$ und $R_{L}$. Dieser führt dazu, dass die Ausgangsspannung $U_{2}$ kleiner wird als erwartet, da der Gesamtwiderstand des unteren Zweigs des Spannungsteilers kleiner wird. Je kleiner der Lastwiderstand $R_{L}$ ist, desto stärker ändert sich die Ausgangsspannung. Nur wenn der Lastwiderstand sehr groß im Vergleich zu $R_{2}$ ist ($R_{L} \gg R_{2}$), ändert sich die Ausgangsspannung nur wenig. Dieses Problem werden Sie im Verlauf des Praktikumsversuches durch einen Impedanzwandler umgehen.

---

<img src="../figures/resistive_voltage_divider_load.png" width="300" style="zoom:100%;"/>

**Abbildung 2**: (Ein belasteter Spannungsteiler mit einem Lastwiderstand $R_{L}$ am Ausgang)

---

Ein weiteres Problem wird nicht erst sichtbar, wenn wir ein Oszilloskop an den Ausgang des Spannungsteilers anschließen. Der Eingang eines Oszilloskops hat für gewöhnlich einen sehr hohen Eingangswiderstand (typischerweise $1 \mathrm{M}\Omega$ oder höher) und eine sehr niedrige Eingangskapazität (typischerweise $\mathrm{15 pF}$). In **Abbildung 3** ist ein Spannungsteiler dargestellt (Mit den Widerständen $R_{1} = R_{2} = \mathrm{1 \Omega}) dessen Ausgang an den Eingangswiderstand und die Eingangskapazität des Oszilloskops angeschlossen sind. Obwohl die Kapazität klein ist, kann sie dennoch einen Tiefpassfilter bilden, der die Messung verfälscht. Bei rechteckigen Signalen kann diese deutliche Verzerrung des Signals gut beobachtet werden, wie eine Simulation der Schaltung aus **Abbildung 3** in **Abbildung 4** zeigt.

---

<img src="../figures/resistive_voltage_divider_oscilloscope.png" width="500" style="zoom:100%;"/>

**Abbildung 3**: (Ein Spannungsteiler mit dem Eingangswiderstand und der Eingangsimpedanz eines Oszilloskops am Ausgang)

---

<img src="../figures/simulation_resistive_voltage_divider_oscilloscope.png" width="500" style="zoom:100%;"/>

**Abbildung 4**: (Simulation der in **Abbildung 3** dargestellten Schaltung. **v(source)** ist ein Rechteck-förmiges Eingangssignal, welches durch den Spannungsteiler zu **v(out)** reduziert wird. Das Ausgangssignal ist durch die Kapazität des Oszilloskops sichtbar verzerrt.)

---

Zur Lösung des Problems schauen wir uns im nächsten Abschnitt einen anderen Spannungsteiler an, der nicht aus Widerständen aufgebaut ist.

## Kapazitiver Spannungsteiler

**TODO: Continue**

#  Essentials

Was Sie ab jetzt wissen sollten:

- Sie sollten den Spannungsteiler erklären und die Formel zur Berechnung der Ausgangsspannung kennen.

## Testfragen  TODO

1. Wo liegt das Problem bei der Messung von $X_{a}$ des OPV? Warum haben Sie dieses Problem bei der Messung von $X_{e}$ nicht?
2. Ihr Signal besteht aus einer geringen Aufladung eines Kondensators. Was passiert, wenn Sie versuchen diese Aufladung als Spannungsantieg mit einem Spannungsmessgerät mit moderatem Innenwiderstand zu messen?
3. Wie würden Sie das Signal durch einen OPV vom Spannungsmessgerät entkoppeln? 

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Operationsverstaerker)

