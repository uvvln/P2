# Polarisation und Doppelbrechung

## Tensor der dielektrischen Moduln und Doppelbrechung

> In einem dielektrischen Medium gilt für die Beziehung zwischen elektrischer Feldstärke $\vec{E}$ und dielektrischer Verschiebung $\vec{D}$ die Beziehung: 
> $$
> \begin{equation*}
> \begin{split}
> &\vec{D} = \epsilon_{0}\boldsymbol{\epsilon}\vec{E} \\
> &\\
> &\boldsymbol{\epsilon} = \left(\epsilon_{ij}\right).
> \end{split}
> \end{equation*}
> $$

💡 Für isotrope Medien, für die keine Raumrichtung ausgezeichnet ist wird die dielektrische Konstante $\boldsymbol{\epsilon}$ ([Permittivität](https://de.wikipedia.org/wiki/Permittivit%C3%A4t)) oft wie ein Skalar behandelt. Im Allgemeinen handelt es sich aber um einen **symmetrischen Tensor zweiter Stufe**. Das gleiche gilt für den Tensor $\boldsymbol{\eta}$ der dielektrischen Moduln
$$
\begin{equation*}
\begin{split}
&\vec{E} = \frac{1}{\epsilon_{0}}\boldsymbol{\eta}\vec{D} \\
&\\
&\boldsymbol{\eta} = \left(\eta_{ij}\right).
\end{split}
\end{equation*}
$$
💡 Symmetrische Tensoren zweiter Stufe kennen Sie bereits z.B. den Trägheitstensor aus dem P1-Versuch [Kreisel](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Kreisel). 

🔔 Jeder symmetrische Tensor zweiter Stufe lässt sich durch [Hauptachsentransformation](https://de.wikipedia.org/wiki/Hauptachsentransformation) in Diagonalenform bringen 
$$
\begin{equation}
\boldsymbol{\eta} = 
\left(
\begin{array}{ccc}
\eta_{11} & 0 & 0 \\
0 & \eta_{22} & 0 \\
0 & 0 & \eta_{33} \\
\end{array}
\right),
\end{equation}
$$
aus deren Eigenwerten $\eta_{ii}$ sich die **Hauptbrechungsindizes** 
$$
\begin{equation*}
\begin{split}
&n_{\alpha} = \frac{1}{\sqrt{\eta_{11}}}; \qquad n_{\beta} = \frac{1}{\sqrt{\eta_{22}}}; \qquad n_{\gamma} = \frac{1}{\sqrt{\eta_{33}}} \\
\end{split}
\end{equation*}
$$
bestimmen lassen, die man konventionell ihrer Größe nach aufsteigend definiert. Für die weitere Diskussion führen wir zudem die Hauptachsenvektoren $\hat{\alpha},\ \hat{\beta},\ \hat{\gamma}$ ein. In seinem Hauptachsensystem lässt sich $\boldsymbol{\eta}$ als [Indexellipsoid](https://de.wikipedia.org/wiki/Indexellipsoid) mit den [Halbmessern](https://de.wikipedia.org/wiki/Radius) $n_{i}$ seiner [Hauptachsen](https://de.wikipedia.org/wiki/Halbachsen_der_Ellipse) darstellen. 

Die exakte Form von $\boldsymbol{\eta}$ ist durch die mikrokopische Struktur des Mediums vorgeben:

- Für **isotrope Medien**, die keine Raumrichtung auszeichnen, liegen alle $n_{i}$ entartet vor. Dies ist bei Gasen oder Flüssigkeiten, aber auch z.B. bei [kubischen Kristallen](https://de.wikipedia.org/wiki/Kubisches_Kristallsystem) der Fall. 
- In einem **dielektrisch anisotropen Medium** liegen die $n_{i}$ nicht entartet vor, d.h. **die Ausbreitungsgeschwindigkeit eines Lichtstrahls in einem solchen Medium hängt von dessen Polarisationsrichtung ab**. 💡 Da der Brechungsindex nicht einen einzigen Wert annimmt spricht man bei Kristallen von [Doppelbrechung](https://de.wikipedia.org/wiki/Doppelbrechung). Der Umstand, dass Doppelbrechung von der kristallinen Struktur des Mediums abhängt erhöht die Komplexität der Beschreibung dieses Phänomens signifikant:
  - Bei optisch einachsigen (uniaxialen) Kristallen ([wirtelige Kristallsysteme](https://de.wikipedia.org/wiki/Wirteliges_Kristallsystem)) liegen zwei der $n_{i}$ entartet vor. 
  - Bei optisch zweiachsigen (biaxialen) Kristallen ([orthorhombische](https://de.wikipedia.org/wiki/Orthorhombisches_Kristallsystem), [monokline](https://de.wikipedia.org/wiki/Monoklines_Kristallsystem) und [trikline](https://de.wikipedia.org/wiki/Triklines_Kristallsystem) Kristallsysteme) unterscheiden sich alle $n_{i}$. 


🔔 Tatsächlich sind die meisten Kristalle anisotrop und daher doppelbrechend.

### Uniaxiale Kristalle und optische Achse

Für uniaxial doppelbrechende Kristalle liegen zwei $n_{i}$ entartet vor, es gilt also entweder $n_{\alpha}=n_{\beta}=n$ oder $n_{\beta}=n_{\gamma}=n$. 🔔 In diesem Fall gibt es eine ausgezeichnete Richtung im Kristall, entlang derer die Geschwindigkeit eines Lichtstrahls und damit $n$ **nicht von der Polarisation des Strahls abhängen**. Diese Richtung bezeichnet man als [optische Achse](https://de.wikipedia.org/wiki/Optische_Achse_(Optik)). Sie fällt mit der Hauptachse des Indexellipsoids zusammen, die zum Brechungsindex gehört, der nicht entartet vorliegt, also entweder $n_{\gamma}$ oder $n_{\alpha}$. Entlang der optischen Achse verhält sich der Kristall isotrop. Verläuft ein Lichtstrahl nicht entlang der optischen Achse, **bilden sich zwei Strahlen aus**, die sich mit unterschiedlicher Geschwindigkeit durch den Kristall bewegen:

- Den Strahl, dessen Polarisation senkrecht zur optischen Achse verläuft, bezeichnet man als **ordentlichen Strahl**; den zugehörigen Brechungsindex bezeichnet man als $n_{\mathrm{o}}$ ("o" für "ordinair"). Dieser Strahl folgt dem [Snelliusschen Brechungsgesetz](https://de.wikipedia.org/wiki/Snelliussches_Brechungsgesetz), d.h. er wird bei senkrechtem Einfall auf das Medium nicht gebrochen. Die Elementarwellen des ordentlichen Strahls bilden Kugelwellen.  
- Den Strahl, dessen Polarisation parallel zur optische Achse liegt, bezeichnet man als **außerordentlichen Strahl**; den zugehörigen Brechungsindex bezeichnet man als $n_{\mathrm{e}}$ ("e" für "extraordinair"). Dieser Strahl folgt nicht dem Snelliusschen Brechungsgesetz, d.h. er wird selbst bei senkrechtem Einfall(!) auf das Medium gebrochen. Die Elementarwellen des außerordentlichen Strahls bilden Rotationsellipsoide. 

Die Differenz $n_{\mathrm{e}}-n_{\mathrm{o}}$ bezeichnet man als **optische Orientierung**. Uniaxiale Kristalle mit $`n_{\mathrm{o}}(=n_{\gamma})>n_{\mathrm{e}}(=n)`$ bezeichnet man als optisch negativ. 🔔 Hier bewegt sich der ordentliche Strahl langsamer durch das Medium, als der außerordentliche Strahl. Uniaxiale Kristalle mit $`n_{\mathrm{o}}(=n)<n_{\mathrm{e}}(=n_{\gamma})`$ bezeichnet man als optisch positiv. 

Eine Skizze des (a) ordentlichen und (b) außerordentlichen Strahls ist in **Abbildung 1** gezeigt:

---

<img src="../figures/DoppelbrechungUniaxial.png" width="1000" style="zoom:100%;" />

**Abbildung 1**: (Skizze des (b) ordentlichen und (b) außerordentlichen Strahls beim Durchgang durch einen uniaxial doppelbrechenden Kristall. Rechts oben im Bild ist die Konstruktion des gebrochenen Strahls skizziert)

---

Beispiele für uniaxial doppelbrechende Kristalle sind [Kalkspat](https://de.wikipedia.org/wiki/Calcit) (optisch negativ) oder Eis (optisch positiv). 

### Biaxiale Kristalle

In biaxialen Kristallen gibt es **zwei optische Achsen**. Sie liegen in der Ebene, die durch $\hat{\alpha}$ und $\hat{\gamma}$ aufgespannt wird. Die Winkel der sich kreuzenden optischen Achsen werden jeweils durch $\hat{\alpha}$ und $\hat{\gamma}$ halbiert. Dies lässt sich wie folgt verstehen: 

💡 Im biaxialen Kristall liegt ein Indexellipsoid mit drei Hauptachsen unterschiedlicher Längen $n_{\alpha},\ n_{\beta},\ n_{\gamma}$ vor. Dreht man das Ellipsoid um $\hat{\beta}$ nimmt der Halbmesser $n_{\gamma}^{\prime}$ (entlang $\hat{\gamma}$) der sich ergebenden [Schnittellipse](https://de.wikipedia.org/wiki/Ellipsoid#Bestimmung_einer_Schnittellipse) alle Werte zwischen $n_{\gamma}$ und $n_{\alpha}$ an. Da es sich dabei um eine stetige Transformation handelt gibt es also auch einem Winkel $\omega_{n_{\gamma}\to n_{\beta}}$, unter dem $n_{\gamma}^{\prime}$ den Wert $n_{\beta}$ annimmt. Damit ist die erste optische Achse gefunden. Das gleiche Argument gilt für den Winkel $\omega_{n_{\alpha}\to n_{\beta}}$ für den der Halbmesser $n_{\alpha}^{\prime}$ (entlang $\hat{\alpha}$) der Schnittellipse den Wert $n_{\beta}$ annimmt. Bei gleicher Drehrichtung, wie zuvor nimmt $n_{\alpha}^{\prime}$ alle Werte zwischen $n_{\alpha}$ und $n_{\gamma}$ an. Damit ist die zweite optische Achse gefunden. 

Da der Wert von $n_{\beta}$ zwischen den Werten von $n_{\alpha}$ und $n_{\gamma}$ liegt und die Wertebereiche von $n_{\gamma}^{\prime}$ und $n_{\alpha}^{\prime}$ jeweils stetig variieren muss es genau zwei optische Achsen geben, die auf diese Weise eindeutig bestimmt sind. Sie können nicht übereinanderliegen, weil nach Voraussetzung $n_{\alpha}\neq n_{\beta}\neq n_{\gamma}$.  

💡 Verläuft ein Lichtstrahl entlang einer der beiden optischen Achsen würde man aus der Diskussion uniaxialer Kristalle zunächst erwarten, dass es nicht zur Doppelbrechung kommt. Tatsächlich ist dies bei biaxialen Kristallen **doch der Fall**. Dabei entsteht für die Polarisationskomponente parallel zu $\hat{\beta}$ ein ordentlicher Strahl. Für alle anderen Polarisationskomponenten entsteht ein außerordentlicher Strahl, der für jede Polarisationskomponente eine andere Ausbreitungsrichtung, aber den gleichen Brechungsindex besitzt. Daher sind alle Polarisationsrichtungen gleichberechtigt und es findet keine diskrete Aufspaltung in zwei Strahlen statt. 💡 Stattdessen kommt es zur [konischen Brechung](https://de.wikipedia.org/wiki/Indexellipsoid#Innere_konische_Refraktion) des außerordentlichen Strahls. Der Grund hierfür liegt darin, dass der biaxiale Kristall entlang der optischen Achsen nicht, wie der uniaxiale Kristall isotrop ist. Für alle anderen Einstrahlrichtungen treten zwei außerdorendliche Strahlen auf. 

**Glimmer ist ein biaxialer Kristall.**

## Erwartung

Was wir an dieser Stelle von Ihnen erwarten:

- :white_check_mark: Sie kennen die Definition des **Tensors der dielektrischen Moduln**. 

- :white_check_mark: Sie verstehen den Zusammenhang zwischen dem Tensor der dielektrischen Moduln und der **optischen Achse eines uniaxial doppelbrechenden Kristalls**. 
- :white_check_mark: Sie wissen, was eine **ordentliche und eine außerordentliche Achse** bei einem uniaxial doppelbrechenden Kristall ist.

## Testfragen

1. Wie viele optische Achsen hat ein uniaxial doppelbrechender Kristall?
1. Wie viele optische Achsen hat ein biaxial doppelbrechender Kristall?
1. In welchen Eigenschaften unterscheidet sich ein biaxial von einem uniaxial doppelbrechenden Kristall?
1. Wie müssen Sie das im Praktikum verwendete $\lambda/4$-Plättchen (aus Glimmer) ausrichten, damit es die Eigenschaften hat, die Sie von ihm erwarten. Was passiert, wenn Sie von dieser Ausrichtung abweichen?

---

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Polarisation/README.md)
