# Hinweise für den Versuch: "Laser-Optik, Teil B" 

##  Aufgabe 1: Beugungsbild eines Spalts

### Hinweise zum Versuch:

Dieser Versuch veranschaulicht Ihnen den Zusammenhang zwischen dem physikalischen Phänomen der Beugung von kohärentem Licht an einem Objekt mit der **Fourier-Transformation**, am einfachen Fall der Beugung am Einfachspalt. Sie können sich daraus anschaulich die Bedeutung des differentiellen Wirkungsquerschnitts in der Kern- und Teilchenphysik erschließen.

Mit Aufgabe 2 des Versuchs [Laser-Optik: Teil A](https://git.scc.kit.edu/etp-lehre/p2-for-students/-/tree/main/Laser-Optik_Teil_A) haben Sie das [Babinetsche Prinzip](https://de.wikipedia.org/wiki/Babinetsches_Prinzip) eingehend studiert, demnach das Beugungsbild eines Spalts (oder einer Lochblende) zum Beugungsbild eines Stegs (oder einer Scheibe) äquivalent ist. Betrachten Sie das Licht nicht im Wellen-, sondern im Teilchenbild ist die Beugung einer ebenen Welle zur Streuung eines kontinuierlichen Strahls von Photonen am untersuchten Objekt äquivalent. Wenn Sie diesen Gedanken weiter entwickeln und das Bild des [Welle-Teilchen-Dualismus](https://de.wikipedia.org/wiki/Welle-Teilchen-Dualismus) auf Materiewellen in der Quantenmechanik übertragen und die folgenden Ersetzungen vornehmen gelangen Sie zur **quantenmechanischen Beschreibung eines klassischen Streuprozesses** in der Kern- oder Teilchenphysik: 

- Statt des Spalt betrachten Sie eine Lochblende; 
- Die Lochblende wird durch eine "Scheibe" (z.B. eines Protons oder eines Atomkerns) ersetzt; 
- Die einlaufende Lichtwelle wird durch die Wellenfunktion eines kontinuierlichen,  einlaufen Strahls z.B. von Elektronen ersetzt;
- Das Beugungsbild des Lichtes (hinter der Lochblende) wird daraufhin durch die Intensitätsverteilung der gestreuten Elektronen ersetzt. Diese entspricht dem Betragsquadrat der Wellenfunktion des gestreuten Elektronenstrahls. 

Diese Ersetzungen gelten in aller Strenge und geben Ihnen ein anschauliches Bild für die Untersuchung von Strukturen, deren Ausdehnungen weit jenseits des mit bloßem Auge Sichtbaren liegen, im "Teilchenbild der Kern- und Teilchenphysik".  

### Hinweise zur Durchführung:

Bei der Durchführung des Versuchs wird der Phototransistor rechnergesteuert von einem Schrittmotor durch das Beugungsbild des Spalts geführt und die Intensität des gebeugten Lichts vermessen. Der Verstärkungsfaktor des eingebauten Vorverstärkers wird dabei –ebenfalls rechnergesteuert– über bis zu drei Zehnerpotenzen an die jeweilige Lichtintensität angepasst. Die dabei ausgegebene, zur Lichtintensität proportionale Gleichspannung des Phototransistors wird durch einen [Analog-Digital-Wandler](https://de.wikipedia.org/wiki/Analog-Digital-Umsetzer) (ADC) digitalisiert und im Rechner gespeichert. Das Rechnerprogramm enthält neben den Steuerroutinen (z.B. für den Schrittmotor und die Verstärkeranpassung) und den Messroutinen (z.B. für die A/D-Wandlung nach dem Prinzip der [sukzessiven Approximation](https://de.wikipedia.org/wiki/Analog-Digital-Umsetzer#Sukzessive_Approximation)) auch Auswerteroutinen. Eine dieser Routinen setzt voraus, dass es sich bei dem Beugungsobjekt um einen Einfachspalt handelt. Zu den Wurzeln der Intensitätsverteilung kann jeweils das richtige Vorzeichen ergänzt und so eine Amplitudenfigur gewonnen werden. Ein FFT("[Fast Fourier Transform](https://de.wikipedia.org/wiki/Schnelle_Fourier-Transformation)")-Algorithmus transformiert diese Amplitudenfigur zurück in ein Spaltbild. 

Über Einzelheiten des Versuchsaufbaus, der Elektronik und des Programms informiert Sie das Personal im Praktikum bei Interesse gern. Bei diesem Versuchsteil erwarten wir jedoch nicht, dass Sie mit allen Details vertraut sind.



---

## Aufgabe 2:  Anwendungen des [Michelson-Interferometers](https://en.wikipedia.org/wiki/Michelson_interferometer)

### Hinweise zur Durchführung:

**2.1:** Einer der Interferometerspiegel sitzt bei diesem Interferometer auf der Stirnfläche des untersuchten $\mathrm{Ni}$-Stabs, der von einer Spule umgeben ist. Der Strom durch die Spule soll nicht über $0,5\,\mathrm{A}$ betragen und jeweils nur kurz eingeschaltet sein, weil sonst die thermische Ausdehnung den [Magnetostriktionseffekt](https://de.wikipedia.org/wiki/Magnetostriktion) überdeckt. Nutzen Sie beide Stromrichtungen für Ihre Messung.

**2.2:** Ab hier wird **ein anderes Interferometer als bei Aufgabe 2.1** benutzt! Notieren Sie mehrere Verschiebungen und die zugehörigen Anzahlen von Wechseln des Interferenzbildes. Die Auswertung soll mit Hilfe der Anpassung einer Geraden an die aufgenommenen Daten erfolgen. 

**2.3:** Bei diesem Versuch ist der bewegte Spiegel sowohl Empfänger, als auch Quelle. Ihr:e Tutor:in gibt Ihnen Hinweise zur geeigneten Justierung des Interferometers. Bestimmen Sie die Frequenzänderung $\Delta \nu$ durch Auszählen der Wechsel des Interferenzbildes innerhalb bekannter Zeitintervalle $\Delta t$, die Sie mit einer Stoppuhr bestimmen. Berechnen Sie dann aus $\Delta \nu$ und der Wellenlänge $\lambda$ des verwendeten Lasers die Geschwindigkeit des Spiegels. Vergleichen Sie diese Abschätzung (und die entsprechende Unsicherheit) mit der auf direkte Weise ermittelten Geschwindigkeit des Spiegels durch Stoppuhr und Längenmessung. 

Dass hier vom Dopplereffekt gesprochen wird, obwohl es sich wie bei Aufgabe 2.2 um Änderungen eines Interferenzbildes bei veränderlicher Spiegellage handelt, ist kein Widerspruch!

---

## Aufgabe 3: Faraday- und Pockels-Effekt
### Hinweise zur Durchführung:

**3.1:** Die Magnetfeldspule speisen Sie aus dem Zweitlautsprecher-Ausgang eines MP3-Players. Fangen Sie das modulierte Licht mit dem Photoelement in der Frontplatte des Niederfrequenz (NF)-Verstärkers mit Lautsprecher auf. Suchen Sie die günstigste Stellung des Polarisationsfilters (in der Nähe des Intensitätsminimums). Diskutieren Sie warum die hohen Frequenzen in diesem Fall so deutlich hörbar benachteiligt sind. Stellen Sie hier und bei den weiteren Aufgaben den Polarisationsfilter an Stellen möglichst großen Strahlquerschnitts auf.

**3.2:** Betreiben Sie für diese Aufgabe die Spule mit Gleichstrom. Wegen der Gefahr der Zerstörung und wegen hinderlicher Strahlkrümmung bei starker Erwärmung sind Ströme von maximal $3\,\mathrm{A}$ für nur kurze Zeit erlaubt. Eventuell sind Abkühlungspausen nötig. Wegen des kleinen Drehwinkels $\alpha$ ist die erreichbare Genauigkeit begrenzt. Nutzen Sie beide Stromrichtungen für Ihre Messung aus. Sie können probeweise statt der direkten Winkelmessungen auch Intensitätsmessungen machen und das [Malussche Gesetz](https://de.wikipedia.org/wiki/Gesetz_von_Malus) ausnutzen.

**3.3:**  Schließen Sie die am Kristall befindlichen Kondensatorplatten an die Serienschaltung von Gleichspannung (von wenigen $100\,\mathrm{V}$) und NF-Spannung (vom Lautsprecher-Ausgang eines MP3-Players über einen Transformator) an. Sie können dann an einer günstigen Stelle des Strahlungsfeldes moduliertes Licht mit dem Photoelement in der Frontplatte des NF-Verstärkers mit Lautsprecher empfangen. 

Das Laserlicht wird mit einer Linse mit $f_{1}=+10\,\mathrm{mm}$ stark divergent aufgeweitet. Dieses divergente Licht wird mit einer Linse mit $f_{2}=+30\,\mathrm{mm}$ im Zentrum der Pockelszelle fokussiert, so dass es die Zelle möglichst ohne Reflexion an den Seitenflächen des Kristalls passiert. Das austretende Licht liefert hinter einem Polarisationsfilter auf einem Schirm ein großflächiges Bild mit Hyperbelstruktur. Diskutieren Sie das Zustandekommen dieses Bildes.

**3.4:** Die Anordnung ist die gleiche, wie aus Aufgabe 3.3, jedoch ohne NF-Einkopplung. Variieren Sie die Spannung an der Pockelszelle von $U=-2000$ bis $+2000\,\mathrm{V}$ und notieren Sie die Werte, bei denen im Zentrum der Hyperbelfigur Helligkeitsextrema (Maxima oder Minima) auftreten. Nummerieren Sie diese Extrema fortlaufend und bestimmen Sie die Steigung der Ausgleichsgeraden, wenn Sie den Wert der eingestellten Spannung über die Anzahl der durchlaufenen Extrema auftragen. Die Steigung dieser Geraden heißt "Halbwellenspannung". Sie erhalten daraus 

```math
\begin{equation*}
\frac{\mathrm{d}\Delta\phi}{\mathrm{d}U},
\end{equation*}
```


die Änderung der Phasenverschiebung  

```math
\begin{equation*}
\Delta\phi(U) = \frac{2\pi}{\lambda_{0}} \left(n_{a_{0}}(U) - n_{0}(U)\right)\,\ell = \frac{2\pi}{\lambda_{0}} \Delta n(U)\,\ell
\end{equation*}
```

des [ordentlichen (mit Brechungsindex $n_{0}$) und des außerordentlichen Strahls (mit Brechungsindex $n_{a_{0}}$)](https://de.wikipedia.org/wiki/Doppelbrechung#Ordentlicher_und_au%C3%9Ferordentlicher_Strahl) längs der Strecke $\ell$ als Funktion der angelegten Spannung $U$. Dabei bezeichnet $\lambda_{0}$ die Wellenlänge des Lichtstrahls im Vakuum. Mit den bekannten geometrischen Abmessungen des Lithiumniobat-Kristalls ergibt sich die gesuchte Konstante $k$. 

Beim Messen können Sie auf ein Photoelement mit Messinstrument verzichten und sich auf Ihr Auge verlassen. Beachten Sie, dass der verwendete Kristall auch ohne elektrisches Feld schon [doppelbrechend](https://de.wikipedia.org/wiki/Doppelbrechung) ist. Beachten Sie die Ähnlichkeiten bei der Veränderung der Doppelbrechung bei mechanischer Spannung und bei der Einwirkung eines elektrischen Feldes.


---

## Aufgabe 4: 

### Hinweise zur Durchführung:

**4.2:** Spülen Sie vor dem Einfüllen der Sorbose-Lösung die Küvette gründlich aus. Reste von Haushaltszucker stören Ihre Messung! Verändern Sie hier die Konzentration nicht, und füllen Sie die vergleichsweise teure Lösung nach Gebrauch wieder in die Flasche zurück.
