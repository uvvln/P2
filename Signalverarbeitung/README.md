

<img src="../figures/Logo_KIT.svg" width="200" style="float:right;" />

# Fakultät für Physik

## Physikalisches Praktikum P2 für Studierende der Physik

Versuch P2-191, 192, 193 (Stand: **Februar 2025**)

[Raum F1-15](https://labs.physik.kit.edu/img/Klassische-Praktika/Lageplan_P1P2.png)



# Signalverarbeitung

## Motivation

Die Grundbausteine der modernen Messtechnik in physikalischen Experimenten drehen sich um die Erfassung, Verstärkung und Verarbeitung von elektrischen Signalen. Die Erfassung der Signale wird mit einem **Analog to Digital Converter (ADC)** durchgeführt. Bei einem ADC handelt es sich um ein Bauteil, das einer Eingangsspannung einen digitalen Wert zuweist und damit als Spannungsmessgerät verwendet wird. Häufig haben ADCs aber aufgrund ihrer technischen Auslegung nur einen begrenzten Eingangsbereich, wodurch es notwendig ist, die elektrischen Signale vor der Messung durch Verstärkungen, Abschwächungen, Filterung und Verschiebungen an den Eingangsbereich des ADCs anzupassen

Die elektrischen Signal, die bei einem physikalischen Experiment gemessen werden, können je nach Experiment und Messgröße sehr klein oder sehr groß sein und müssen innerhalb eines kurzen oder langen Zeitraums erfasst werden. In Versuchen aus der Kern- und Teilchenphysik werden z.B. sehr schnelle Signale von Photomultipliern (PMTs) ausgewertet, während in der Festkörperphysik oft sehr kleine Ströme oder Spannungen gemessen werden müssen. In der Akustik und Optik können die andere Anforderungen an die Signalverarbeitung ganz anders aussehen. Um den vielfältigen Anforderungen gerecht zu werden, sind verschiedene Bauelemente und Schaltungen notwendig. Einige wichtige  Bauelemente für die Signalverarbeitung lernen sie in diesem Versuch kennen, darunter den [Operationsverstärker](https://de.wikipedia.org/wiki/Operationsverst%C3%A4rker) (OPV).

**TODO: Den OPV erklären wir lieber in den Docs und nicht hier!**

Ein [Operationsverstärker](https://de.wikipedia.org/wiki/Operationsverst%C3%A4rker) (OPV) ist ein aus Transistoren bestehender [integrierter Schaltkreis](https://de.wikipedia.org/wiki/Integrierter_Schaltkreis) zur Signalverstärkung, der eine sehr hohe Verstärkung aufweist und durch Gegenkopplung in seinem Verhalten kontrolliert werden kann. Der Begriff *operational amplifier*, von dem sich auch die deutsche Bezeichnung **Operationsverstärker** ableitet, geht auf den anfänglich überwiegenden Einsatz zur Durchführung einfacher mathematischer Operationen in den ersten analogen Rechenmaschinen und Computern zurück. Heutzutage gibt es viele verschiedene OPV-Modelle mit unterschiedlichen Eigenschaften, die für verschiedene Anwendungen optimiert sind. In diesem Praktikum verwenden wir den weit verbreiteten OPV vom Typ **MCP6001**.

---


OPVs sind aus der heutigen Elektrotechnik und Signalverarbeitung nicht mehr wegzudenken. Sie werden als Schalter, zur Verstärkung oder als [Impedanzwandler](https://de.wikipedia.org/wiki/Impedanzwandler) verwendet. In der physikalischen Messtechnik spielen sie überall dort eine Rolle, wo Signale klein sind und/oder ein Messgerät die Messgröße nicht beeinflussen darf. Nahezu jedes physikalische Experiment, das mit kleinen Signalen konfrontiert ist benutzt daher heutzutage OPVs. Die Anforderungen an den OPV sind: 

- Gegebenenfalls hohe Verstärkung. 
- Hohe Eingangsimpedanz $X_{e}$ (im Bereich von $10^{13}\ \Omega$!). Dadurch lässt sich z.B. die Rückwirkung eines angeschlossenen Voltmeters auf das Signal minimieren. 
- Niedrige Ausgangsimpedanz $X_{\mathrm{a}}$. Dadurch lässt sich z.B. die Rückwirkung des OPV auf ein angeschlossenes Voltmeter minimieren.

Im Praktikum begegnen Ihnen diese Anforderungen zum Beispiel in den folgenden Versuchen: 

- [Photoeffekt](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Photoeffekt): Hier besteht die Herausforderung darin, eine Spannung zu messen, die von nur wenigen Ladungsträgern auf einem Kondensator erzeugt wird. Es geht also um die Spannungsverstärkung. Ohne einen sehr hohen Eingangswiderstand würde sich der Kondensator während der Messung aber wieder entladen.
-  [Franck-Hertz-Versuch](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Franck_Hertz_Versuch).  Hier besteht die Herausforderung darin einen Strom im Bereich weniger $\mathrm{nA}$ zu messen. Hier geht es also v.a. um die Stromverstärkung.

## Lehrziele

Wir listen im Folgenden die wichtigsten **Lehrziele** auf, die wir Ihnen mit dem Versuch **Signalverarbeitung** vermitteln möchten: 

- Sie lernen den **Frequenzkompensierten Spannungsteiler** als Grundbauelement elektrischer Schaltungen kennen.
- Sie lernen den **OPV als wichtiges aktives Bauelement** elektrischer Schaltkreise mit seinen wichtigsten Eigenschaften, den **Goldenen Regeln**, kennen. 
- Sie verinnerlichen die Grundschaltungen des OPV als **Impedanzwandler, nicht-invertierendem Verstärker und invertierendem Verstärker**. 
- Sie üben sich in der **Dimensionierung einfacher Schaltungen** mit dem OPV.
- Sie erkennen in der Vorbereitung auf den Versuch den Nutzen von OPVs für physikalische Messungen und erfahren, wo für konkrete Messungen im Praktikum OPVs im Einsatz sind. 

## Versuchsaufbau

Ein typischer Aufbau für den Versuch Operationsverstärker ist in **Abbildung 1** gezeigt:
**TODO: Ein anders Bild vom neuen Aufbau verwenden**

---

<img src="./figures/Operationsverstaerker.png" width="1000" style="zoom:100%;" />

**Abbildung 1**: (Ein typischer Aufbau für den Versuch Operationsverstärker)

---

Alle Schaltungen werden mit Hilfe verschiedener Widerstände, Kondensatoren und Trimmer-Kondensatoren auf dem Schaltbrett aufgesteckt und mit dem Oszilloskop oder dem Multimeter untersucht. Zur Erzeugung eines Eingangssignals dient ein Frequenzgenerator. 

## Was macht diesen Versuch aus?

Bei diesem Versuch steht das "physikalische Innenleben" des Operationsverstärkers nicht im Vordergrund. Dieses werden Sie in späteren Vorlesungen genauer studieren können. Uns geht es um ein grundlegendes Verständnis der Vorgänge und den Umgang bei der Beschaltung eines OPV. Die Grundschaltungen sollte jeder Physiker mit etwas Praxis aufbauen können. Einfache Schaltungen geben Ihnen die Möglichkeit, die Grundprinzipien der OPV-Beschaltung zu verstehen und sich mit den damit verbundenen Möglichkeiten vertraut zu machen. In seinen Anfangsjahren war der OPV für die analoge Durchführung algebraischer und numerischer Operationen in analogen Computern vorgesehen. In diesem Versuch dienen uns hauptsächlich dazu, Ihnen die Scheu bei der Beschaltung von OPVs zu nehmen. 

## Wichtige Hinweise

- Für diesen Versuch benötigen Sie einen USB-Datenträger zum Datentransfer. 

# Navigation

- [Signalverarbeitung.iypnb](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Signalverarbeitung/Operationsverstaerker.ipynb): Aufgabenstellung und Vorlage fürs Protokoll.
- [Signalverarbeitung_Hinweise.ipynb](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Signalverarbeitung/Operationsverstaerker_Hinweise.ipynb): Kommentare zu den Aufgaben.
- [Datenblatt.md](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Signalverarbeitung/Datenblatt.md): Technische Details zu den Versuchsaufbauten.
- [doc](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Signalverarbeitung/doc): Dokumente zur Vorbereitung auf den Versuch.
- [figures](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Signalverarbeitung/figures): Bilder, die für die Dokumentation des Versuchs verwendet wurden.
