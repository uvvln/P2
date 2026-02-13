# Signalverarbeitung - Simulationen

Dieses Verzeichnis beinhaltet Simulationsdateien für alle Schaltungen, die im Versuch zur Signalverarbeitung aufgebaut und untersucht werden. Die Simulationsdateien sind im `SPICE` Format und können mit dem `ngspice` Simulator ausgeführt werden. Innerhalb der Datei werden Spice-Befehle verwendet, die das zeitliche Verhalten der Spannung an einem Bauteil grafisch darstellen.

Eine `ngspice` Simulation wird aus der Kommandozeile über den Befehl `ngspice <Dateiname>` gestartet. Sobald die Simulation abgeschlossen ist, kann `ngspice` mit dem Befehl `exit` beendet werden.

## Bauteile-Suche

Bei der Entwicklung dieses Versuchs mussten bestimmte Bauteil-Werte bestimmt werden um die Gleichungen aus der Vorbereitungshilfe zu erfüllen. Dabei wurde ein Python-Skript entworfen, welches die Widerstände aus der E48-Reihe untersucht. Die verfügbaren Widerstände werden alle miteinander verglichen um die am besten geeigneten Werte zu finden.

Da es manchmal sinnvoll war, auf einen Widerstand zurück zu greifen, der bereits für eine vorherige Teilaufgabe verwendet wird, wurde das Skript an manchen Stellen dementsprechend angepasst. Dadurch kann die Gesamtanzahl an benötigten Widerständen für diesen Versuch reduziert werden.

Das Python-Skript `Bautile.py` berechnet die Bauteile und sucht die passenden Widerstände in der E48 Reihe.
