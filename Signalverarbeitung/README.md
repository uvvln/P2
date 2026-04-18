

<img src="../figures/Logo_KIT.svg" width="200" style="float:right;" />

# Fakultät für Physik

## Physikalisches Praktikum P2 für Studierende der Physik

Versuch **H17** (Stand: **April 2026**)

[Raum F1-13](https://labs.physik.kit.edu/img/Klassische-Praktika/Lageplan_P2.png)

# Signalverarbeitung

## Motivation

> Moderne Messtechnik im physikalischen Experiment hat die Aufgabe verschiedenste analoge Messgrößen, als elektrische Signale digital zu erfassen und zu verstärken. Diese Erfassung erfolgt mit Hilfe des [Analog-Digital-Wandlers](https://de.wikipedia.org/wiki/Analog-Digital-Umsetzer) (**Analog to Digital Converter, ADC**), der einer gegebenen Eingangsspannung einen digitalen Wert zuweist. 

Häufig haben ADCs aufgrund ihrer technischen Auslegung nur einen begrenzten Eingangsbereich, z.B. $0{-}3\ \mathrm{V}$, woraus sich die Notwendig ergibt, analoge elektrische Signale vor der Messung durch Verstärkung, Abschwächung, Filterung und Verschiebungen an den Eingangsbereich des eingesetzten ADC anzupassen.

Elektrische Signale, die bei einem physikalischen Experiment zu erfassen sind, können sehr vielfältig sein. Je nach Experiment und Messgröße können sie entweder sehr klein oder sehr groß sein. Oft werden sie außerdem entweder innerhalb eines sehr kurzen oder eher langen Zeitraums erfasst. In diesem Versuch lernen Sie einige wichtige Schaltungen zur Signalverarbeitung kennen, die im Laboralltag in Verwendung sind, um den verschiedenen Anforderungen physikalischer Experimente an die Datenerfassung gerecht werden zu können. Es handelt sich um Grundschaltungen, die sich schnell und einfach realisieren lassen und in der Praxis oft Verwendung finden, um elektrische Signale auf einfache Weise anzupassen. Im Praktikum begegnen Ihnen diese Schaltungen zum Beispiel in den Versuchen: 

- [Photoeffekt](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Photoeffekt): Hier besteht die Herausforderung darin, eine Spannung zu messen, die von nur wenigen Ladungsträgern auf einem Kondensator erzeugt wird. Es geht also um Spannungsverstärkung und Impedanzwandlung. Ohne einen sehr hohen Eingangswiderstand der Messanordnung würde sich der Kondensator bei der Messung sofort entladen.
-  [Franck-Hertz-Versuch](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Franck_Hertz_Versuch).  Hier besteht die Herausforderung darin einen Strom im Bereich weniger $\mathrm{nA}$ zu messen.

## Lenrziele

Wir listen im Folgenden auf, was wir von Ihnen erwarten, nachdem Sie diesen Versuch erfolgreich absolviert haben:  

- :white_check_mark: Sie kennen die Grundschaltung eines **frequenzkompensierten Spannungsteilers**.
- :white_check_mark: Sie sind im **Umgang und Verständnis elektrischer Schaltungen** geübt.
- :white_check_mark: Sie sind im **Einsatz und der Dimensionierung von Operationsverstärkern OPV** geübt.
- :white_check_mark: Sie haben ein grundsätzliches Verständnis der einzelnen Schritte, die hinter dem Signaleingang eines modernen Messgeräts, wie einem Datenlogger oder einem Digitaloszilloskop, ablaufen, um die Daten eines Experiments digital zu erfassen.

## Weiterführendes Angebot

Die Aufgabenstellungen zu diesem Versuch sind bewusst freier gefasst. Zum Beispiel ist der konkrete Einsatz von Widerständen und Kondensatoren ist nicht vorgegeben. Sie können daher die Gelegenheit nutzen, frei mit den Bauteilen zu experimentieren und verschiedene Lösungen der Aufgabenstellungen ausprobieren und testen. Ihre Tutor:innen stehen Ihnen dabei ggf. mit Rat zur Seite.

## Versuchsaufbau

Ein typischer Aufbau für den Versuch **Signalverarbeitung** ist in **Abbildung 1** gezeigt:

---

<img src="./figures/Aufgabe_1_Testaufbau.jpg" width="1000" style="zoom:100%;" />

**Abbildung 1**: (Ein typischer Aufbau für den Versuch **Signalverarbeitung**)

---

Alle Schaltungen werden mit Hilfe von Operationsverstärkern, sowie verschiedener, am Versuchsplatz hinterlegter Widerstände und Kondensatoren auf einem Schaltbrett aufgesteckt und mit dem Oszilloskop oder dem Multimeter verifiziert. Zur Erzeugung eines geeigneten Eingangssignals dient ein Funktionsgeber. 

## Was macht diesen Versuch aus?

> In Anlehnung an die Grundversuche des P1, bietet Ihnen dieser Versuch die Möglichkeit frei am Schaltbrett (Breadboard) mit elektrischen Schaltungen zu experimentieren, um die vorgeschlagenen Schaltungen zu realisieren und auszuprobieren. 

Sie sollten genug Zeit haben, um sich ein klares Verständnis der grundlegenden Schritte der analogen Signalverarbeitung auf dem Weg zum digitalen Datensatz zu erarbeiten. Der Versuch beginnt mit einem leeren Steckbrett, einem Multimeter, Oszilloskop, Funktionsgeber und einer Sammlung von Bauteilen in einem Sortierkasten. Die Aufgabenstellungen sind zum Teil freier gefasst. Im Laboralltag wären nicht einmal diese Voraussetzungen gegeben. Sie würden mit der Aufgabenstellung (den Spezifikationen Ihres Messvorhabens) beginnen und sich die Bauteile, die Sie zu deren Realisierung benötigen, eigenverantwortlich zusammenstellen.   

Es ist explizit erwünscht, dass Sie sich die Zeit nehmen, sich ohne einen vorgefertigten, konkreten Aufbau, mit den teils vertrauten, teils neuen Aspekten elektrischer Schaltungen, im Experiment auseinander zu setzen. Wie bei anderen Versuchen dieser Art, besteht der Fokus hier auf der Durchführung und dem Vorgang des Experimentierens selbst, mehr als auf der Auswertung oder dem erzielen eines bestimmten, anvisierten Messwerts. Stellen Sie sich vor, dass die von Ihnen aufgebauten Schaltungen auf der Grundlage Ihrer Angaben in Serie auf einer Platine aufgelötet werden, die Sie und andere für weitere Messungen verwenden möchten. Die funktionsfähige Realisierung und in diesem Sinne gewissenhafte Charakterisierung jeder entsprechenden Schaltung ist das Ergebnis dieses Versuchs. 

# Inventar des Versuchs

- Wir gehen davon aus, dass Sie das Protokoll zu diesem Versuch aus einer **Jupyter-Umgebung** führen:
  - 💡 Hierzu steht Ihnen das [bwJupyter Hub](https://hub.bwjupyter.de/) zur Verfügung.
  - 💡 Nutzen Sie **diesen [Direkt-Link](https://hub.bwjupyter.de/services/profilemanagement/add?profile=5fbace23-bf49-4edd-bcaf-c9d421afa8c7)** zur erstmaligen Einrichtung der Umgebung für das P1/P2-Praktikum.
  - 💡 Hinweise zur Arbeit auf dem bwJupyter Hub entnehmen Sie der Datei [JupyterServer.md](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/doc/JupyterServer.md).
- Die folgenden Links führen auf/in die wichtigsten Dateien und Verzeichnisse dieser Versuchsanleitung:
  - [Signalverarbeitung.iypnb](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Signalverarbeitung/Signalverarbeitung.ipynb): Aufgabenstellung und Vorlage fürs Protokoll (in Form eines Jupyter-notebook).
  - [Signalverarbeitung_Hinweise.ipynb](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Signalverarbeitung/Signalverarbeitung_Hinweise.ipynb): Hinweise zu Versuchsdurchführung und Auswertung (in Form eines Jupyter-notebook).
  - [Datenblatt.md](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Signalverarbeitung/Datenblatt.md): Inventar und technische Details zu den Versuchsaufbauten.
  - [doc](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Signalverarbeitung/doc): Dokumente zur Vorbereitung auf den Versuch.
  - [figures](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Signalverarbeitung/figures): Bilder, die für die Dokumentation des Versuchs verwendet wurden.
