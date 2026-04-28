# Photoeffekt

## Experimentelle Aufbauten

### Hg-Dampflampe

Für den Versuch wird die Photozelle mit dem Licht einer Hochdruck-Quecksilberdampflampe bestrahlt. 💡 [Hg](https://de.wikipedia.org/wiki/Quecksilberdampflampe) besitzt u.a. die folgenden für diesen Versuch relevanten diskreten Emissionslinien 

- $\lambda=365.01\ \mathrm{nm}$ (UV);
- $\lambda=404.66\ \mathrm{nm}$ (violett);
- $\lambda=407.78\ \mathrm{nm}$ (violett);
- $\lambda=435.83\ \mathrm{nm}$ (blau);
- $\lambda=491.60\ \mathrm{nm}$ (cyan);
- $\lambda=546.07\ \mathrm{nm}$ (grün);
- $\lambda=576.96\ \mathrm{nm}$ (orange);
- $\lambda=579.07\ \mathrm{nm}$ (orange).

In der Überlagerung ergibt sich eine **grünliche Farbe**. Einzelne Wellenlängen können mit Hilfe von sechs [Fabry-Pero](https://de.wikipedia.org/wiki/Fabry-P%C3%A9rot-Interferometer)-Farbfiltern weiter ausgewählt werden, die für die folgenden Wellenlängen durchlässig sind:

- $\lambda^{(1)}_{\mathrm{CWL}}=360\ \mathrm{nm}$;
- $\lambda^{(2)}_{\mathrm{CWL}}=400\ \mathrm{nm}$;
- $\lambda^{(3)}_{\mathrm{CWL}}=440\ \mathrm{nm}$;
- $\lambda^{(4)}_{\mathrm{CWL}}=490\ \mathrm{nm}$;
- $\lambda^{(5)}_{\mathrm{CWL}}=540\ \mathrm{nm}$;
- $\lambda^{(6)}_{\mathrm{CWL}}=590\ \mathrm{nm}$.

💡 Die Abkürzung CWL steht dabei für *central wavelength*; es ist die Wellenlänge in der Mitte des Filterbandpasses. Laut Hersteller haben die Filter eine **[Halbwertsbreite](https://de.wikipedia.org/wiki/Halbwertsbreite) von $\pm10\ \mathrm{nm}$**, aus der Sie die Standardabweichung des eingestrahlten Lichts bestimmen können. 💡 Beachten Sie dabei die Umrechnung zwischen Halbwertsbreite und Standardabweichung unter Annahme einer Normalverteilung. 

### Spannungsmessung mit dem Messverstärker

Da die Photozelle nur sehr geringe Spannungen erzeugt würde sie bei direkter Messung mit einem einfachen Multimeter direkt über den Innenwiderstand des Messgeräts entladen werden. Ein gutes Handmultimeter besitzt zur Spannugnsmessung einen Innenwiderstand von $R_{i}\approx\mathcal{O}(1{-}10\ \mathrm{G\Omega})$. 

Die Messung als Spannungsmessung kann auf zweierlei Weise erfolgen: 

- Als sich aufbauende Spannung an einem Kondensator mit der bekannten Kapazität $C$. 
- Als abfallende Spannung an einem bekannten Widerstand $R$. 

🔔 Die Messanordnung hierzu sollte einen **maximal hohen Innenwiderstand $R_{i}$** aufweisen. Dies erreicht man z.B. durch Verwendung eines Operationsverstärkers (OPV) als Impedanzwandler (Spannungsfolger), wie in **Abbildung 1** gezeigt: 

---

<img src="../figures/Spannungsfolger.png" width="600" style="zoom:100%;"/>

(**Abbildung 1:** Schaltbild eines Impedanzwandlers, wie er zur Auslese des Versuchs **Photoeffekt** verwendet wird)

---

🔔 Ein Impedanzwandler übersetzt $U_{e}$ ohne weitere Verstärkung (d.h. mit dem Verstärkungsfaktor $v_{U}=1$) in $U_{a}=U_{e}$. Der Versuch [**Signalverarbeitung**](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Signalverarbeitung/README.md) gibt Ihnen die Möglichkeit sich mit dieses Bauelement besser kennenzulernen. 

Am Ausgang des Impedanzwandlers wird das Signal mit Hilfe eines Analog-Digital-Wandlers ([ADS1115](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/doc/SOLDERED_ADS1115_DATASHEET.pdf)) digitalisiert und zur weiteren Verarbeitung an einen [Raspberry Pi 400](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/doc/raspberry-pi-400-product-brief.pdf) (oder höher) weitergeleitet. 

> Mit Hilfe des Impedanzwandlers kann $U_{a}$ weiterverarbeitet werden, ohne die am Eingang anliegende Spannung $U_{e}$ zu beeinflussen. Auf diese Weise wird die Photozelle effektiv von der weiteren Auslesekette zur Signalverarbeitung entkoppelt, so dass der Einfluss der Messung auf die Photozelle so gering wie möglich bleibt. 

Der Schaltkreis von der Aufnahme des Signals als $U_{e}$ bis zum 40-poligen Breitbandkabel zur Weiterleitung des digitalisierten Signals an den Raspberry Pi ist in **Abbildung 2** gezeigt: 

---

<img src="../figures/Ausleseplatine.png" width="600" style="zoom:100%;"/>

(**Abbildung 2**: Platine zur Auslese der Photozelle. Abbildung (a) zeigt die Platine noch in rohem Zustand, nach Abschluss der Entwicklungen. Abbildung (b) zeigt die Platine im finalen Gehäuse. Die Anschlüsse sind einzeln identifizierbar)

---

#### Bestimmung des Innenwiderstands $R_{i}$ der Messanordnung

Das Ersatzschaltbild für eine klassische Bestimmung des Innenwiderstands $R_{i}$ eines Spannungsmessgeräts ist in **Abbildung 3** gezeigt:

---

<img src="../figures/Innenwiderstand.png" width="600" style="zoom:100%;"/>

**Abbildung 3**: (Ersatzschaltbild für eine klassische Bestimmung des Innenwiderstands $R_{i}$ eines Spannungsmessgeräts)

---

🔔 Das Messgerät ist durch den gestrichelten Kasten dargestellt. Es hat den Ausgabewert $U_{a}$, den Eingabewert $U_{e}$ (jeweils relativ zu GND) und den Innenwiderstand $R_{i}$. Zum Messgerät ist mit $R_{V}$ ein bekannter Referenzwiderstand $R_{V}$ in Serie geschaltet. In der Messanordnung gehen wir zudem von einer bekannten idealen Spannungsquelle für die Spannung $U_{0}$ aus. Nach den [Kirchhoffschen Regeln](https://de.wikipedia.org/wiki/Kirchhoffsche_Regeln) gilt:
$$
\begin{equation*}
\begin{split}
&U_{e}=R_{i}\,I;\qquad U_{0}=(R_{V}+R_{i})\,I;\\
&\\
&U_{a} = U_{e} = U_{0}\,\frac{R_{i}}{R_{V}+R_{i}}\approx U_{0}\left(1-\frac{R_{V}}{R_{i}}\right); \\
%&\\
%&R_{i} = \frac{U_{e}}{U_{0}+U_{e}}\,R_{V}.\\
\end{split}
\end{equation*}
$$
🔔 Das Problem bei der Messung von $R_{i}$ für die Messanordnung, wie wir sie für diesen Versuch verwenden, besteht darin, dass der Wert von $R_{i}$ im Bereich mehrerer(!) $100\ \mathrm{G\Omega}$ und damit deutlich höher liegt als jeder im Handel erhältliche Referenzwiderstand $R_{V}$. 

Zum Vergleich: 

- Der Innenwiderstand des menschlichen Körpers wird mit ${\approx}70\ \mathrm{k\Omega}$ [[1](https://de.wikipedia.org/wiki/K%C3%B6rperwiderstand)] (von Fingerspitze zu Fingerspitze) angegeben.
- Die höchsten im Handel erhältlichen Widerstände haben einen Nennwert von $10\ \mathrm{G\Omega}$. 

Selbst unter Verwendung eines im Handel erhältlichen Widerstands von $R_{V}=10\ \mathrm{G\Omega}$ läge der Spannungsabfall an $U_{a}$ durch Serienschaltung von $R_{V}$ mit dem Messgerät, für das $R_{i}$ zu bestimmen ist im %-Bereich. 

💡Der Effekt, aus dem $R_{i}$ zu bestimmen wäre, wäre also tendenziell eher klein und daher sehr unpräzise. 

**Wir schlagen vor, den Kondensator mit der Kapazität $C=(4.7\pm0.05)\ \mathrm{nF}$ über die Messanordnung kurz zu schließen.** Dadurch kommt es zur Entladung 
$$
\begin{equation}
U_{a}(t, C, R_{i}) = U_{0}\,e^{-\frac{1}{C\,R_{i}}t},
\tag{1}
\end{equation}
$$
die Sie über die Messanordnung bestimmen können. Aus dem Verlauf der Entladekurve lässt sich $R_{i}$ bei Kenntnis von $C$ bestimmen.

---

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Photoeffekt/README.md)
