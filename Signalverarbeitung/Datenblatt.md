# Technische Daten und Inventar für den Versuch **Signalverarbeitung**

Für den Versuch stehen Ihnen die folgenden Geräte und Apparaturen zur Verfügung:

- Ein Steckbrett (Breadboard) mit einer Spannungsversorgung von $5\ \mathrm{V}$.
- Jumper-Kabel zur Verbindung der Bauelemente auf dem Steckbrett.
- Operationsverstärker (OPV) vom Typ LM358 (paarweise verbaut).
- Widerstände mit verschiedenen Werten:
    - $16.2\ \mathrm{k\Omega}$.
    - $11.5\ \mathrm{k\Omega}$.
    - $9.09\ \mathrm{k\Omega}$.
    - $2.87\ \mathrm{k\Omega}$.
    - $2.26\ \mathrm{k\Omega}$.
    - $1.15\ \mathrm{k\Omega}$.
- Potentiometer mit einem Widerstandswert von $0\ldots2.2\  \mathrm{k\Omega}$.
- Kondensatoren mit verschiedenen Kapazitäten:
    - $470\ \mathrm{pF}$.
    - $82\ \mathrm{pF}$.
    - $100\ \mathrm{nF}$.
- Ein Trimmkondensator mit variabler Kapazität im Bereich $15\ldots 85\ \mathrm{pF}$. 💡 Einige Bauformen von Trimmkondendsatoren haben drei Beine, zwei davon liegen dann auf dem gleichen Potential.
- Dioden vom Typ 1N4148.
- Ein Netzteil zur Spannungsversorgung der OPVs, das ${+}12\  \mathrm{V}$ und ${-}12\ \mathrm{V}$ bereitstellt.
- Ein Tisch-Multimeter vom Typ [Kethley 169.](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/doc/Keithley_169_Manual.pdf)
- Ein Hand-Multimeter. Beachten Sie zur Anzeige die Hinweise zur Versuchsdurchführung [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Operationsverstaerker/doc/Hinweise-Versuchsdurchfuehrung.md).
- Ein Funktionsgeber (FG) vom Typ [Instek SFG 2104](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/doc/Instek_SFG_2104_Manual.pdf) ($0.2\ \mathrm{Hz} \ldots\ 2\ \mathrm{MHz}$; Sinus, Rechteck oder Dreieck; $0 \ldots \pm10\ \mathrm{V}$).
- Ein Oszilloskop vom Typ [PeakTech 1255](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/doc/PeakTech_1240-1275_07-2020_DE-EN.pdf). Eine detaillierte Beschreibung der Bedienelemente des Oszilloskops können Sie der Bedienungsanleitung oder den Anleitungen zum P1-Versuch [Oszilloskop](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Oszilloskop) entnehmen.

## Funktionsgeber und Oszilloskop

Mithilfe des Funktionsgebers können Sie Sinus-, Dreieck-, oder Rechtecksignale mit variabler Frequenz und Amplitude erzeugen. Für diesen Versuch verwenden wir hauptsächlich Sinus- und vereinzelt Rechteck-Signale im $\mathrm{kHz}$-Bereich als Eingangssignal.

Das Oszilloskop, das Sie bereits aus dem [Grundversuch Oszilloskop](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Oszilloskop/README.md) kennen, ermöglicht es Ihnen, das Eingangs- mit dem Ausgangssignal Ihrer Schaltung zu vergleichen. Schließen Sie dazu das aus dem FG kommende Signal an einen Kanal des Oszilloskops an. Mit dem zweiten Kanal können Sie an Ihrer Schaltung verschiedene Messpunkte untersuchen (z.B. das Ausgangssignal der Schaltung oder die Eingänge des OPV).

### ⚠️ **Vor der Verwendung des Oszilloskops müssen Sie die Tastköpfe kalibrieren.** ⚠️ 

Eine Beschreibung hierzu finden Sie in den Hinweisen zum Grundversuch Oszilloskop [hier](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Oszilloskop/doc/Hinweise-GrundlagenOszi.md?ref_type=heads#tastkopfkomensation).

Alternativ können Sie wie folgt vorgehen:

- Verbinden Sie dazu die beiden Tastköpfe mit dem Oszilloskop und stellen Sie am Funktionsgeber ein Rechtecksignal mit einer Amplitude von $1\ \mathrm{Vpp}$ (Spitze-Spitze) und einer Frequenz von $1\ \mathrm{kHz}$ ein. 
- Stellen Sie das Rechtecksignal gut sichtbar am Osziloskop dar. 
- Justieren Sie die Tastköpfe an jeweiligen Kalibrationsschraube so, dass das angezeigte Signal möglichst verzerrungsfrei, als Rechtecksignal zu erkennen ist.



