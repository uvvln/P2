# Polarisation und Doppelbrechung

## Polarisation

### Lineare, elliptische und zirkulare Polarisation

> Elektromagnetsiche (em) Wellen sind **transversale Wellen**. Ihre Polarisation wird i.a. durch die Ausrichtung des elektrischen Feldstärkevektors $\vec{E}$ definiert. 

Zur besseren Übersicht stellen wir für die weitere Diskussion o.B.d.A. die Welle durch ihre zeitliche Entwicklung in $\vec{E}(t)$ mit der festen Kreisfrequenz $\omega$ und der festen Wellenzahl $\vec{k}$ dar. Wir betrachten die Welle außerdem an einem festen Ort in der Ebene senkrecht zu $\vec{k}$. Für **linear polarisierte Wellen** variiert $\vec{E}(t)$ entlang einer Achse mit zeitlich unveränderlicher Orientierung in dieser Ebene: 
$$
\begin{equation*}
\vec{E}(t) = \vec{E}\,e^{\pm i\omega\,t}.
\end{equation*}
$$
💡 Jede linear polarisierte Welle mit der Amplitude $\vec{E}$ lässt sich in zwei senkrecht zueinander stehende, linear polarisierte Teilwellen mit den Amplituden $`\vec{E}_{1}\perp\vec{E}_{2}`$, wie in **Abbildung 1** dargestellt, zerlegen: 

---

<img src="../figures/PolarisationSkizze.png" width="750" style="zoom:100%;" />

**Abbildung 1**: (Bild (a) zeigt die Aufspaltung des Vektors $\vec{E}$ in zwei senkrecht zueinander stehende Komponenten $`\vec{E}_{1}\perp \vec{E}_{2}`$. Bild (b) zeigt den Fall der elliptischen Polarisation, wobei zwischen den ebenen Teilwellen zu $`\vec{E}_{1}`$ und $`\vec{E}_{2}`$ eine Phasendifferenz von $\Delta\phi=\pi/2$ besteht

---

💡 Je nachdem welche weiteren Randbedingungen für die Beträge $`|\vec{E}_{1}|`$ und $`|\vec{E}_{2}|`$ und die Phasenbeziehung $\Delta\phi\in[0,\pi)$ zwischen den Wellen $`\vec{E}_{1}(t)`$ und $`\vec{E}_{2}(t)`$ bestehen weist $\vec{E}(t)$ eine unterschiedliche Polarisation auf: 

- Für $\Delta\phi=0$ liegt die bereits diskutierte **lineare Polarisation** vor. 

- Für $\Delta\phi=\pi/2$ und $`|\vec{E}_{1}|=|\vec{E}_{2}|`$ beschreibt die Spitze von $\vec{E}(t)$ einen Kreis in der Ebene senkrecht zu $\vec{k}$; man bezeichnet diese Art der Polarisation als **zirkulare Polarisation**.

- Für $\Delta\phi=\pi/2$ und $`|\vec{E}_{1}|\neq|\vec{E}_{2}|`$ beschreibt die Spitze von $\vec{E}(t)$ eine Ellipse senkrecht zur Ausbreitungsrichtung; man bezeichnet diese Art der Polarisation als **elliptische Polarisation**. 💡 Dieser Zustand ist äquivalent zu der Randbedingung $`|\vec{E}_{1}^{\prime}|=|\vec{E}_{2}^{\prime}|`$ und

  ```math
  \begin{equation*}
  \Delta\phi^{\prime} = \arctan\left(\frac{|\vec{E}_{1}^{\prime}|}{|\vec{E}_{2}^{\prime}|}\right).
  \end{equation*}
  ```

### Erzeugung von elliptisch polarisiertem Licht mit Hilfe einer Verzögerungsplatte

> Eine [Verzögerungsplatte](https://de.wikipedia.org/wiki/Verz%C3%B6gerungsplatte) (VP) ist ein optisches Bauelement bestehend aus einem doppelbrechenden Kristall in dem sich i.a. zwei senkrecht zueinander, linear polarisierte Strahlen S und L mit unterschliedlichen Geschwindigkeiten $c_{i}=c/n_{i}, \ i=\mathrm{S,\ L}$ ausbreiten, wobei $c$ der Lichtgeschwindigkeit im Vakuum entspricht. 

Wir definieren $`c_{\mathrm{S}}>c_{\mathrm{L}}`$. Die Polarisationsrichtung von S und L bezeichnen wir jeweils als **schnelle und langsame Achse**. Je nach optischer Orientierung entspricht entweder die schnelle oder die langsame Achse der optischen Achse des Mediums. 

Der Unterschied in $c_{i}$ führt zu einem Unterschied der Wellenlängen 
$$
\begin{equation*}
\lambda_{i} = \frac{\lambda}{n_{i}},
\end{equation*}
$$
wobei $\lambda$ der Wellenlänge im Vakuum entspricht. Aufgrund dieses Unterschieds verschieben sich S und L beim Durchgang durch VP gegeneinander, so dass es abhängig von der Dicke $d$ von VP zur Phasenverschiebung $\Delta\phi$ zwischen beiden Strahlen kommt, wie in **Abbildung 2** skizziert:

---

<img src="../figures/OptischeDichte.png" width="500" style="zoom:100%;" />

**Abbildung 2**: (Phasenverschiebung der Strahlen S und L aufgrund von Doppelbrechung in VP. Zur Veranschaulichung wurden die Parameter $d=\lambda_{L}$ und $n_{S}/n_{L}=4/5$ gewählt, so dass S nach Durchlaufen von VP L um eine viertel Periode vorauseilt)

---

🔔 Welcher Anteil von $\lambda_{i}$ in $d$ liegt ist durch das Produkt
$$
\begin{equation*}
d\,k_{i}=\frac{2\pi\,d}{\lambda_{i}} = \frac{2\pi\,d\,n_{i}}{\lambda} = d\,k\,n_{i}
\end{equation*}
$$
geometrisch vorgegeben. Die Phasendifferenz $\Delta\phi$ zwischen S und L nach Durchlaufen der Strecke $d$ erhält man aus 
$$
\begin{equation}
\Delta\phi = \frac{2\pi\,d}{\lambda}\left(n_{\mathrm{L}}-n_{\mathrm{S}}\right).
\tag{1}
\end{equation}
$$
🔔 Für die Parameterwahl aus **Abbildung 2** erhält man $\Delta\phi=\pi/2$, die für **Abbildung 2** gewählten Abmessungen entsprechen also den Abmessungen für ein $\lambda/4$-Plättchen zur Erzeugung zirkularer Polarisation für die Wellenlänge $\lambda$.

### Lineare Polarisation am Gitter

Eine der einfachsten Methoden linear Polarisiertes Licht zu erzeugen besteht in der Bestrahlung eines Gitters mit elektrisch leitenden Verbindungen ([Drahtgitterpolarisator](https://de.wikipedia.org/wiki/Drahtgitterpolarisator)), wie in **Abbildung 3** gezeigt:

---

<img src="../figures/PolarisationGitter.png" width="1000" style="zoom:100%;" />

**Abbildung 3**: (Lineare Polarisation am Drahtgitter (Quelle [Wikipedia](https://commons.wikimedia.org/w/index.php?curid=724493)))

---

🔔 Durch die Einstrahlung von em Wellen werden die leitenden Verbindungen am Gitter zu Schwingungen angeregt und fungieren als [Herztsche Dipole](https://de.wikipedia.org/wiki/Hertzscher_Dipol). Die abgestrahlte Welle erfährt aufgrund der Randwerte einen Phasensprung um $\pi$. Unter der Annahme idealer Leiter (ohne inneren Widerstand) führt dies zur destruktiven Interferenz und damit zur Auslöschung der Welle jenseits des Gitters. Vor dem Gitter führt die Dipolstrahlung durch Reflexion zur Ausbildung einer stehenden Welle. 

🔔 Senkrecht zu den leitenden Verbindungen ist durch deren geringe Abmessungen ($d\ll\lambda$) keine nennenswerte Schwingung möglich und alle Anteile der Welle mit dieser Polarisationsrichtung können das Gitter ungehindert passieren. 

🔔 Ein Gitter wirkt nur dann als Polarisationsfilter, wenn es eine hinreichend große Anzahl von Verbindungen mit hinreichend geringem Durchmesser $d$ und Abstand $g$ aufweist. 

### Lineare Polarisation durch Reflexion oder Streuung

Eine ebenfalls wohlbekannte Methode zur Erzeugung von linear polarisiertem Licht ist **Polarisation durch Reflexion**, z.B. unter dem [Brewster-Winkel](https://de.wikipedia.org/wiki/Brewster-Winkel), wie in **Abbildung 4** gezeigt:

---

<img src="../figures/BrewsterWinkel.png" width="1000" style="zoom:100%;" />

**Abbildung 4**: (Geometrische Darstellung des **Brewster-Winkels**. Die Doppelpfeile senkrecht zu S uns S' stellen die Polarisation in der Bildebene dar, die Kreise mit den schwarzen Punkten auf den $\vec{k}$-Vektoren zu S, S' und S'' die Polarisationspfeile senkrecht zur Bildebene)

---

🔔 Der Strahl S wird an einem optisch dichteren Medium (mit $n_{2}$) zur optischen Achse hin gebrochen. Unter dem **Brewster-Winkel** steht der gebrochene Strahl S' senkrecht zum reflektierten Strahl S''. S'' ist zu 100% senkrecht zur Bildebene polarisiert. Dies erklärt sich wie folgt: 

🔔 Durch S werden atomare Dipole im dichteren Medium zur Schwingung angeregt. S'' wird parallel zu den Dipolen reflektiert, einer Richtung in der die Dipole nicht abstrahlen. Dadurch wird der Polarisationsanteil in der Bildebene unterdrückt, der Polarisationsanteil in der Ebene senkrecht zur Bildebene wird ungehindert abgestrahlt. Auf die gleiche Art und Weise wird gestreutes Licht polarisiert.  

## Erwartung

Was wir an dieser Stelle von Ihnen erwarten:

- :white_check_mark: Sie können erklären, was **lineare, zirkulare und elliptische Polarisation** von Licht ist und wie man sie mathematisch beschreibt. 
- :white_check_mark: Sie können die **Funktionsweise einer VP** und insbesondere eines $\lambda/4$-Plättchens erklären.
- :white_check_mark: Sie können den Effekt linearer Polarisation am elektrisch leitenden Gitter und durch Reflexion oder Streuung erklären.

## Testfragen

1. Welche Polarisation des Lichts erwarten Sie, wenn Sie nach oben in den blauen Himmel sehen? Welche Polarisation erwarten Sie für das rote Licht im Abendrot?
1. Welche Intensität erwarten Sie für einen zirkular polarisierten Lichtstrahl hinter einem linearen Polarisationsfilter? Welche Polarisation erwarten Sie?

---

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Polarisation/README.md)
