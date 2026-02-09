# Hinweise für den Versuch **Signalverarbeitung**

## Hinweise Komplexere Schaltungen

## Clamping-Dioden

Ein Operationsverstärker kann das Eingangssignal verstärken, aber er kann nicht verhindern, dass die Ausgangsspannung einen bestimmten Wert überschreitet. Wenn die Ausgangsspannung einen bestimmten Wert nicht überschreiten darf, können Dioden als **Clamping-Dioden** eingesetzt werden. Sie werden so geschaltet, dass sie bei Überschreiten der gewünschten Spannung leitend werden und die Spannung nicht über dieses Niveau hinausgehen lassen. Die Dioden werden in der Regel in Sperrrichtung geschaltet, um sicherzustellen, dass sie nur bei Überschreiten der gewünschten Spannung leitend werden.

**Abbildung 1** zeigt eine Schaltung, bei der das Ausgangssignal auf $\pm{}5 \mathrm{V}$ begrenzt wird. Eine Simulation dieser Schaltung ist in **Abbildung 2** zu sehen. Damit der Strom durch die Dioden nicht zu groß wird, muss er durch einen Widerstand begrenzt werden.

---

<img src="../figures/clamping_diodes.png" width="600" style="zoom:100%;"/>

**Abbildung 1**: (Ein nicht-invertierender Verstärker mit clamping-Dioden, um die Ausgangsspannung zu begrenzen. Die Dioden sind in Sperrrichtung geschaltet, um sicherzustellen, dass sie nur bei Überschreiten der gewünschten Spannung leitend werden. Der $1 \mathrm{k\Omega}$ Widerstand begrenzt den Strom durch die Dioden.)

---

<img src="../figures/clamping_diodes_simulation.png" width="600" style="zoom:100%;"/>

**Abbildung 2**: (Simulation der Schaltung in **Abbildung 1**. Das verstärkte Ausgangssignal des OPV ist rot dargestellt und hat eine Amplitude von $\pm{}9 \mathrm{V}$. Das von den Dioden beschränkte Ausgangssignal in Grün wird nach Überschreiten der Durchbruchspannung der Dioden abgeschnitten.)

---

Die Simulation in **Abbildung 2** zeigt, dass die Dioden das Niveau nicht exakt im Rahmen von $\pm{}5 \mathrm{V}$ halten. Dies liegt daran, dass die Dioden einen Potentialunterschied von ca. $0,7 \mathrm{V}$ benötigen um leitfähig zu werden. Daher wird die Ausgangsspannung auf etwa $\pm{}5,7 \mathrm{V}$ begrenzt.

Clamping-Dioden können verwendet werden, wenn das durch zu hohe Ausgangsspannungen andere elektrische Bauteile beschädigt werden können, wie z.B. andere Operationsverstärker, Mikrocontroller oder Sensoren.

🔔**In diesem Dokument haben wir die Polarisation der Dioden, die Sie für den Aufbau der Schaltungen verwenden, bewusst nicht erklärt.** 🔔 Führen Sie einen Dioden-Test an einer Diode durch, um die Polarität zu bestimmen, bevor Sie sie in Ihre Schaltung einbauen.

## Summierverstärker

Die Schaltung des Summierverstärkers ist in **Abbildung 3** dargestellt.

---

<img src="../figures/summing_amplifier.png" width="600" style="zoom:100%;"/>

**Abbildung 3**: (Schaltung eines Summierverstärkers)

---

Zur Erklärung der Schaltung wird erst einmal nur die Spannungsquelle $V_1$ betrachtet. Es handelt sich um einen invertierenden Verstärker, bei dem die Ausgangsspannug des OPV so dimmensioniert wird, dass der eingehende Strom von $V_1$ durch den Widerstand $R_1$ vollständig durch den Widerstand $R_f$ fließt. Es gilt also:
$$
\begin{equation}
\frac{V_1}{R_1} = - \frac{V_{out}}{R_f} \Rightarrow V_{out} = - V_1 \cdot \frac{R_f}{R_1}
\end{equation}
$$

Wird nun zusätzlich die Spannungsquelle $V_2$ betrachtet, so fließt auch durch den Widerstand $R_2$ ein Strom. Am nicht-invertierenden Eingang summieren sich diese Ströme. Durch den Widerstand $R_f$ fließt der gesamte Strom, der von den Spannungsquellen $V_1$ und $V_2$ durch die Widerstände $R_1$ und $R_2$ geliefert wird. Es gilt also:
$$
\begin{equation}
\frac{V_1}{R_1} + \frac{V_2}{R_2} = - \frac{V_{out}}{R_f} \Rightarrow V_{out} = - \left( V_1 \cdot \frac{R_f}{R_1} + V_2 \cdot \frac{R_f}{R_2} \right)
\end{equation}
$$
Die Ausgangsspannung setzt sich somit aus der Summe der einzelnen Eingangsspannungen mit ihren jeweiligen Verstärkungsfaktoren zusammen.

Um einen Summierverstärker zu realisieren, der eine Eingangsspannung von $\pm9 \mathrm{V}$ in den Bereich von $-3 \mathrm{V} \to 0 \mathrm{V}$ umwandelt, verwenden Sie die folgenden Werte für die Widerstände:
- $R_1 = 6,81 \mathrm{k\Omega}$
- $R_2 = 9,09 \mathrm{k\Omega}$
- $R_f = 1,15 \mathrm{k\Omega}$

## Essentials

Was Sie ab jetzt wissen sollten:

- Clamping-Dioden können verwendet werden, um die Ausgangsspannung eines OPVs zu begrenzt.
- Mit dem Summierverstärker können mehrere Eingangssignale mit unterschiedlichen Verstärkungsfaktoren summiert werden.

## Testfragen

1. Wie bestimmen Sie die Polarität der Dioden?
2. Wie wirkt sich die virtuelle Masse auf den Summierverstärker aus?

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Operationsverstaerker)

