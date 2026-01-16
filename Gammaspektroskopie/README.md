<img src="../figures/Logo_KIT.svg" width="200" style="float:right;" />

# Fakultät für Physik

## Physikalisches Praktikum P2 für Studierende der Physik

Versuch P2-261, 262, 263 (Stand: **April 2025**)

[Raum F2-19](https://labs.physik.kit.edu/img/Klassische-Praktika/Lageplan_P1P2.png)



# Gammaspektroskopie

## Motivation

Bei Experimenten der Kern- und Teilchenphysik ist neben den Fragen nach Art und Ort einer Wechselwirkung die Frage nach dem Impuls und der Energie der Reaktionsprodukte besonders wichtig. In der Teilchenphysik misst man die Energie eines einlaufenden Teilchens mit Hilfe eines [Kalorimeters](https://de.wikipedia.org/wiki/Kalorimeter_(Teilchenphysik)). Das Prinzip besteht darin, das Teilchen komplett im Detektor zu stoppen und die dadurch im Detektor deponierte Energie zu bestimmen. In diesem Versuch untersuchen Sie die Energie hoch-energetischer Photonen aus dem $\gamma$-Zerfall verschiedener radioaktiver Präparate. Der Nachweis erfolgt mit Hilfe eines [Szintillationszählers](https://de.wikipedia.org/wiki/Szintillationsz%C3%A4hler), bestehend aus einem Thallium-dotierten $\mathrm{NaJ}$-Einkristall, mit dem Sie die Energie $E_{\gamma}$ des einlaufenden Photons $\gamma$ bestimmen können. Das Messprinzip ist das gleiche, wie für ein Kalorimeter der Teilchenphysik. Bei $\mathrm{NaJ}$ handelt es sich um einen [Szintillator](https://de.wikipedia.org/wiki/Szintillator), der beim Durchgang geladener Teilchen selbst zur Emission von Photonen angeregt wird. Die vom Szintillator emittierten Photonen haben eine um mehrere Größenordnungen niedrigere Energie als $E_{\gamma}$, deren exakter Wert $\Delta E$ vom Material des Szintillators abhängt. **Ein Photon kann durch drei verschiedene Prozesse mit Materie in Wechselwirkung treten**: 

 - [Photoeffekt](https://de.wikipedia.org/wiki/Photoelektrischer_Effekt): das Photon schlägt ein Elektron aus der Hülle eines Atoms, dabei geht die gesamte Energie des Photons auf das Elektron über; 
 - [Compton-Effekt](https://de.wikipedia.org/wiki/Compton-Effekt): das Photon wird elastisch an einem Elektron in der Hülle eines Atoms gestreut, d.h. das gestreute Elektron nimmt einen Teil der Energie des einfallenden Photons ($\gamma$) auf, ein Photon ($\gamma^{\prime}$) niedrigerer Energie wird dabei emittiert; und 
 - [Paarbildung](https://de.wikipedia.org/wiki/Paarbildung_(Physik)): das Photon zerfällt, im elektromagnetischen Feld, z.B. eines Atomkerns, in ein Elektron-Positron-Paar, die Energie des Photons geht dabei zu gleichen Teilen auf das Elektron und das Positron über. 

Je nach dem Wert von $E_{\gamma}$ tragen diese Prozesse mit unterschiedlich hoher Wahrscheinlichkeit zur Wechselwirkung des Photons mit dem Detektor bei. In jedem Fall geht die Energie des Photons auf elektrisch geladene Elektronen über. Ein hoch-energetisches Elektron (oder Positron) kann selbst wieder mit einer gewissen Wahrscheinlichkeit (durch [Bremsstrahlung](https://de.wikipedia.org/wiki/Bremsstrahlung)) Photonen abstrahlen, die wiederum, wie oben beschrieben, mit Materie in Wechselwirkung treten. Auf diese Weise entsteht im Material ein sogenannter [**elektromagnetischer Schauer**](https://de.wikipedia.org/wiki/Elektromagnetischer_Schauer), der schließlich, solange er vollständig im Detektor zum erliegen kommt im statistischen Mittel zur Emission von 

$$
\begin{equation*}
\langle n_{\gamma}\rangle = \frac{E_{\gamma}}{\Delta E}
\end{equation*}
$$

Szintillationsphotonen führt. Gelingt es diese Photonen einzusammeln und (wiederum durch den Photoeffekt) nachzuweisen lässt sich aus dem so erzeugten Photostrom $E_{\gamma}$ bestimmen. Dies ist bis zum heutigen Tag das **Prinzip jedes Szintillations-Kalorimeters in der Teilchenphysik**. 

Am [CMS Experiment](https://cms.cern/detector/measuring-energy/energy-electrons-and-photons-ecal) des LHC verwendet man z.B. Bleiwolframat ($\mathrm{PbWO_{4}}$)-Einkistalle, um hoch-energetische Photonen und Elektronen im Kalorimeter auf die kurze Distanz von $\ell\approx30\,\mathrm{cm}$ möglichst zu stoppen und ihre Energie zu bestimmen. 

## Lehrziele

Wir listen im Folgenden die wichtigsten **Lehrziele** auf, die wir Ihnen mit dem Versuch **Gammaspektroskopie** vermitteln möchten: 

 - Sie lernen die **Funktionsweise, den Aufbau und die Verwendung eines Szintillationszählers** kennen. 
 - Sie **experimentieren mit radioaktiven Präparaten** und untersuchen deren Eigenschaften. 
 - Sie studieren die **Wechselwirkung von Licht mit Materie** und identifizieren entsprechende Signaturen im Energiespektrum des Szintillators. 
 - Sie diskutieren den Zusammenhang der Energieauflösung des Detektors mit den statistischen Prozessen der Messung.

## Versuchsaufbau

Ein typischer Versuchsaufbau ist in **Abbildung 1** gezeigt:

---

<img src="./figures/Gammaspektroskopie.png" width="1000" style="zoom:100%;"/>

**Abbildung 1** (Typischer Aufbau des Versuchs Gammaspektroskopie)

---

Der Photodetektor wird mit Hochspannung (bei etwa $600\ \mathrm{V}$) betrieben und ist auf ein Stativ montiert. Sie erhalten die radioaktiven Proben von Ihre:r Tutor:in. Diese sind in Aluminium-Zylinder eingeschlossen, die die $\beta$-Strahlung der Präparate hinreichend abschirmt. Zur Messung werden die Probenzylinder mit ihrer Stirnfläche in die Nähe der Stirnfläche des Photodetektors gebracht. Die im Detektor nachweisbare Intensität eintreffender $\gamma$-Strahlen hängt stark vom Abstand der Probe vom Detektor ab. Die Auslese des Signals erfolgt über einen [Vielkanalanalysators](https://de.wikipedia.org/wiki/Vielkanalanalysator) ([*Multichannel analyzer*](https://en.wikipedia.org/wiki/Multichannel_analyzer) MCA) vom Typ [Rep Pitaya](https://de.wikipedia.org/wiki/Red_Pitaya). Eine einfache graphische Benutzeroberfläche erlaubt die Beobachtung der aufgezeichneten Signale, während der Datennahme, unter Verwendung des MCA als [Oszilloskop](https://de.wikipedia.org/wiki/Oszilloskop) oder [Spektrumanalysator](https://de.wikipedia.org/wiki/Spektrumanalysator). Zur abschließenden Auswertung können Sie das aufgezeichnete Spektrum z.B. in [csv-Format](https://de.wikipedia.org/wiki/CSV_(Dateiformat)) ausgeben lassen. 

## Was macht diesen Versuch aus?

Mit diesem Versuch erleben Sie einen der modernsten Versuche des P2. Zwar ist der Szintillationsdetektor schon etwas älter, die Auslese wurde jedoch im Jahr 2024 komplett überholt. Die aus dem Detektor gekoppelten Signale werden direkt auf den Vielkanalanalysator geleitet, mit dem sie sich oszilloskopisch oder spektral sofort untersuchen lassen. Gleichzeitig experimentieren Sie erstmals mit radioaktiven Stoffen. Der radioaktive Zerfall ist ein probabilistischer Prozess. Das gleiche gilt für die Energiedepositionen der emittierten hochenergetischen Photonen im Szintillationsdetektor. In solchen Fällen interessiert man sich i.a. nicht für die Eigenschaften einzelner konkreter Prozesse. Stattdessen betrachtet man Prozesse als statistische Ereignisse und bewertet ihre Eigenschaften auf der Grundlage statistischer Ensembles vieler artgleicher aber statistisch unabhängiger Ereignisse.   

## Wichtige Hinweise

- Die Kernphysik-Räume stellen einen **innerbetrieblichen Überwachungsbereich** dar. Dies bedeutet, u.a. dass wir zu Ihrer Sicherheit permanent die auftretende Strahlendosis in diesen Räumen aufzeichnen. In einem innerbetrieblichen Überwachungsbereich gelten nach der **Strahlenschutzverordnung** des Bundes besondere Regeln, die Sie unbedingt beachten und einhalten müssen. Mehr Information finden Sie auf den entsprechenden [Webseiten des P1- und P2-Praktikums](https://labs.physik.kit.edu/163.php?tab=%5B315%5D#tabpanel-315).
- Die Versuche der Kernphysik dürfen erst nach Teilnahme an der **Strahlenschutzbelehrung** durchgeführt werden, die in der Regel während der Vorbesprechung zum Praktikum stattfindet.
- Der Zugang zum Bunker für radioaktive Präparate ist nur den Tutor:innen oder der Praktikumsleitung gestattet.

# Navigation

-  [Gammaspektroskopie.iypnb](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Gammaspektroskopie/Gammaspektroskopie.ipynb): Aufgabenstellung und Vorlage fürs Protokoll.
-  [Gammaspektroskopie_Hinweise.ipynb](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Gammaspektroskopie/Gammaspektroskopie_Hinweise.ipynb): Kommentare zu den Aufgaben.
-  [Datenblatt.md](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Gammaspektroskopie/Datenblatt.md): Technische Details zu den Versuchsaufbauten.
-  [doc](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Gammaspektroskopie/doc): Dokumente zur Vorbereitung auf den Versuch.
-  [figures](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Gammaspektroskopie/figures): Bilder, die für die Dokumentation des Versuchs verwendet wurden.

