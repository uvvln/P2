# Polarisation und Doppelbrechung



## Prinzip der Polarisationsmessungen

🔔 Die Polarisation des Lichts untersuchen Sie immer mit der Kombination aus dem AF mit dem Sie den Winkel $\varphi$ der zu untersuchenden Polarisationsebene festlegen und der PZ zur Messung der Intensität des Lichts hinter dem AF. 

### Justierung der Verzögerungsplatten

Die im Praktikum verwendeten [Verzögerungsplatten](https://de.wikipedia.org/wiki/Verz%C3%B6gerungsplatte) (VP) bestehen aus [Glimmer](https://de.wikipedia.org/wiki/Glimmergruppe). Als doppelbrechendes Medium besitzt Glimmer zwei optische Achsen, entlang derer sich das Licht mit unterschiedlichen Geschwindigkeiten ausbreitet. 🔔 Um maximale elliptsche/zirkulare Polarisation beobachten zu können müssen Sie die VP im Strahlengang so ausrichten, dass die Lichtintensität entlang beider Achsen gleichgroß ist. 

Gehen Sie hierzu wie folgt vor: 

- Polarisieren Sie das Licht linear mit Hilfe des PF.
- Verdrehen Sie den AF, so dass Sie an der PZ $U=0$ messen.
- Bringen Sie die VP ein, bei zufälliger Ausrichtung sollten Sie $U\neq0$ beobachten.
- Verdrehen Sie die VP so lange, bis Sie wieder den Zustand $U=0$ erreichen. 🔔 In diesem Fall **verläuft der linear polarisierte Strahl exakt zu einer der Achsen**, so dass es bei der Transmission des Lichts nicht zur Änderung der Polarisation kommt. 
- Drehen Sie jetzt den PF um $45^{\circ}$ gegen seine ursprüngliche Position. Damit ist er um $45^{\circ}$ gegen die optische Achse der VP verdreht, so dass beide optische Achsen des Kristalls mit gleicher Intensität bestrahlt werden. 

ℹ️ Es kann sein, dass bei der Justierung die Spannung an der PZ nicht ganz auf 0 abfällt sondern einen *Offset* $U_{0}$ aufweist. 

ℹ️ **Dieses Verfahren müssen Sie für jede VP immer wieder neu durchführen.** 

### Untersuchung von linear polarisiertem Licht

Ein passendes Modell zur Beschreibung des Spannungsverlaufs der PZ ist 
$$
\begin{equation}
U(\varphi) = U_{0}+U_{A}\sin(\Omega\,\varphi+\phi_{0}).
\tag{1}
\end{equation}
$$
Mit $U_{0}$, $U_{A}$, $\Omega$ und $\phi_{0}$ besitzt dieses Modell **vier freie Parameter**.  

- $U_{0}$ erlaubt einen allgemeinen *Offset*. 
- $U_{A}$ legt die Amplitude der sinusförmigen Modulation der Lichtintensität hinter dem AF fest. 
- $\Omega$ erlaubt Abweichungen von der Erwartung von 2, und 
- $\phi_{0}$ erlaubt einen *Offset* der Winkelskala des AF relativ zum PF. 

💡 Durch den Wertebereich $[0,\pi)]$ ist die Verteilung von $U(\varphi)$ eindeutig bestimmt. Im Maximum von $U(\varphi)$ ist der AF exakt parallel zum PF ausgerichtet, im Minimum genau senkrecht. 

### Untersuchung von zirkular polarisiertem Licht

Für perfekt zirkular polarisiertes Licht erwarten Sie, das die Lichtintensität nicht von $\varphi$ abhängt ($U\neq U(\varphi)$). In der Praxis kann es sein, dass Sie immer noch eine leicht (sinusförmige) Modulation von $U(\varphi)$ feststellen. 

Sie können diese Modulation quantifizieren, wenn Sie an die Messreihe das Modell aus Gleichung **(1)** unverändert anpassen. Bei einer solchen Anpassung interessieren Sie sich in erster Linie für den Parameter $U_{A}$. 

💡 Überprüfen Sie den $\chi^{2}$-Wert der Anpassung. Weist dieser darauf hin, dass das Modell die Daten gut beschreiben kann dann überprüfen Sie, wie weit der Wert von $U_{A}$ im Rahmen der aus der Anpassung bestimmten Unsicherheit $\Delta U_{A}$ von 0 verschieden ist (den sog. *pull* $\delta$, siehe [hier](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Datenverarbeitung/doc/Hinweise-Statistik.md?ref_type=heads#kompatibilit%C3%A4t-zweier-unabh%C3%A4ngiger-messungen)). Für $`\delta>3`$ sprechen wir von einer **Evidenz** (Hinweis). Für $`\delta>5`$ von einer **Beobachtung**.

Abschließend können Sie eine Anpassung des "trivialen Modells" nur unter der Berücksichtigung von $U_{0}$, ohne den zusätzlichen Sinusterm, durchführen und den $\chi^{2}$-Wert dieser Anpassung überprüfen. Weist dieser wiederum darauf hin, dass das triviale Modell die Daten gut beschreiben kann ist eine Modulation der Daten in $\varphi$ zumindest **statistisch nicht nachweisbar**.  

### Differenz der Brechungsindizes $n_{\beta}$ und $n_{\gamma}$ von Glimmer

Aus den Intensitätsverteilungen zur elliptischen Polarisation können Sie die Differenz der Brechungsindizes 
$$
\begin{equation*}
\Delta n=\left(n_{\beta} - n_{\gamma}\right)
\end{equation*}
$$
von Glimmer berechnen.  

Den Phasenunterschied $\Delta\phi$ der beiden senkrecht zueinander stehenden Strahlen an der Austrittsfläche der VP erhalten Sie aus dem Verhältnis der minimalen ($\propto U_{\mathrm{min}}$) zur maximalen ($\propto U_{\mathrm{max}}$) Intensität des elliptisch polarisierten Lichts. Diese können Sie wiederum aus der Anpassung eines Modells in Anlehnung an Gleichung **(1)**, wie folgt bestimmen: 
$$
\begin{equation*}
\begin{split}
&U(\varphi) = U_{\mathrm{min}}+\Delta U\Bigl(1+\sin(\Omega\,\varphi+\phi_{0})\Bigr).
\\
&\\
&\text{mit}\\
&\\
&U_{\mathrm{max}} = U_{\mathrm{min}}+2\,\Delta U.\\
\end{split}
\end{equation*}
$$
🔔 Gegebenenfalls ist $U_{\mathrm{min}}$ auf den *Offset* $U_{0}$ aus Gleichung **(1)** zu korrigieren, der zuvor mit linear polarisiertem Licht bestimmt wurde. Das für die Berechnungen notwendige **Verhältnis der Amplituden** der Strahlen ergibt sich aus der Quadratwurzel des **Verhältnisses der Intensitäten**. Schließlich erhalten Sie die Phasendifferenz aus dem $\arctan(\ \cdot\ )$ dieses Verhältnisses. 

Zusammenfassend ergibt sich die Formel: 
$$
\begin{equation}
\Delta n = \frac{\lambda_{0}}{2\pi\,d}\arctan\left(\sqrt{\frac{U_{\mathrm{min}}}{U_{\mathrm{min}}+2\,\Delta U}}\right),
\tag{2}
\end{equation}
$$
wobei $d$ der Dicke der VP und $\lambda_{0}$ der Wellenlänge des Lichts (im Vakuum) entsprechen. Verwenden Sie geeignete Unsicherheiten für $U_{\mathrm{min}},\  \Delta U,\ d,\ \lambda_{0}$. 

Bestimmen Sie $\Delta n$ aus beiden Ihnen zur Verfügung stehenden Messreihen (für die jeweils unterschiedlichen Dicken $d_{i}$) aus **Aufgabe 2.1** und vergleichen Sie die Ergebnisse.

---

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Polarisation/README.md)
