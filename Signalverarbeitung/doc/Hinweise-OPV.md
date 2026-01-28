# Hinweise für den Versuch **Signalverarbeitung**

## Einführung Operationsverstärker

Ein [Operationsverstärker](https://de.wikipedia.org/wiki/Operationsverst%C3%A4rker) (OPV) ist ein integrierter Schaltkreis mit vielen verschiedenen Einsatzzwecken. In diesem Versuch werden einfache Schaltungen mit dem OPV aufgebaut und untersucht. Um diese Schaltungen zu verstehen, sind einige Grundkenntnisse über den OPV notwendig.

Das Schaltsymbol eines OPVs ist in **Abbildung 1 (a)** mit seinen Anschlüssen gezeigt:

- Ein invertierender (-) und ein nicht-invertierender (+) Eingang.
- Ein Ausgang
- Zwei Anschlüsse für die Spannungsversorgung ($\mathrm{V_{S\pm}}$), die in Schaltbildern i.a. nicht gezeigt werden und daher in den weiteren Bildern weggelassen sind.

An den Eingängen und am Ausgängern des OPV sind die die relevanten Spannungen und Ströme eingezeichnet, auf die im Verlauf der Beschreibung Bezug genommen wird.

---

<img src="../figures/opamp_overview.png" width="750" style="zoom:100%;"/>

**Abbildung 1**: (In Abbildung (a) ist das Schaltsymbol eines OPV mit Definition der relevanten Anschlüssen, Spannungen und Strömen gezeigt. Abbildung (b) zeigt das Gehäuse, in dem der MCP6002 verbaut ist. Abbildung \(c\) zeigt das Anschlussschema des OPV MCP6002, wie er in diesem Versuch verwendet wird. $V_{S\pm}$ bezeichnet die Versorgungsspannung. Die Beschaltung im Inneren des OPV, sowie die Versorgungsspannung(en) werden in Schaltbildern i.a. nicht gezeigt)

---

**Abbildung 1 \(c\)** zeigt das Anschlussschema des MCP6002, welcher für diesen Versuch verwendet wird und gleich zwei OPVs in einem Gehäuse bereitstellt. Das Gehäuse ist in **Abbildung 1 (b)** dargestellt.

Ein OPV lässt sich auf viele verschiedene Weisen beschalten und bietet damit eine Vielzahl von verschiedenen Einsatzmöglichkeiten. In diesem Praktikumsversuch werden die wichtigsten Schaltungen, die auf dem Prinzip der [Gegenkopplung](https://de.wikipedia.org/wiki/Negative_R%C3%BCckkopplung) basieren, erklärt und untersucht.

## Die goldenen Regeln

Das Prinzip der Gegenkopplung (auch negative Rückkopplung genannt) beruht darauf, dass ein Teil des Ausgangssignals mit invertiertem Vorzeichen auf den Eingang zurückgeführt wird. Darüber wird das Verhalten des OPVs kontrolliert und lässt sich mit den **goldenen Regeln** beschreiben:

1. Es fließt kein Strom in die Eingänge des OPVs. Der Eingangswiderstand am invertierenden und am nicht-invertierenden Eingang wird als unendlich groß angenommen.
2. Der OPV hat eine niedrige Ausgangsimpedanz und kann als [ideale Spannungsquelle](https://de.wikipedia.org/wiki/Spannungsquelle#Ideale_und_reale_Spannungsquellen) mit einem Ausgangswiderstand $R_{out} = 0\ \Omega$ angenommen werden.
3. Der OPV wählt seine Ausgangsspannung so, dass die Differenz der Eingangsspannungen verschwindet: $U_{+} - U_{-} = 0\mathrm{V}$. Dies ist nur möglich, wenn eine Gegenkopplung vorhanden ist.

Die drei goldenen Regeln sind in **Abbildung 2** zusammengefasst.

---

<img src="../figures/golden_rules.png" width="550" style="zoom:100%;"/>

**Abbildung 2**: (Die drei goldenen Regeln des Operationsverstärkers)

---

## Spannungsfolger (Impedanzwandler)

Die einfachste Schaltung, die mit dem OPV realisiert werden kann, ist der **Spannungsfolger** (engl. *voltage follower*). Diese Schaltung ist in **Abbildung 3** dargestellt. Hier wird der Ausgang direkt in den invertierenden Eingang zurückgeführt. Das Eingangssignal wird an den nicht-invertierenden Eingang angelegt.

---

<img src="../figures/voltage_follower.png" width="400" style="zoom:100%;"/>

**Abbildung 3**: (OPV als Spannungsfolger)

---

Nach den goldenen Regeln gilt:

1. Da kein Strom in den nicht-invertierenden Eingang fließt, fällt hier auch keine Spannung ab, sodass $U_{in} = U_{+}$ gilt.
2. Da der Ausgang mit dem invertierenden Eingang verbunden ist, gilt $U_{-} = U_{out}$.
3. Damit die Differenz zwischen den beiden Eingängen verschwindet, muss $U_{+} = U_{-}$ gelten. Daraus folgt, dass $U_{in} = U_{out}$ gilt.

Nach dieser Schaltung wird die gleiche Spannung am Ausgang ausgegeben, die am nicht-invertierenden Eingang anliegt, weshalb diese Schaltung auch als **Spannungsfolger** bezeichnet wird. Der Nutzen dieser Schaltung liegt darin, dass am Ausgang die Spannung $U_\mathrm{out} = U_\mathrm{in}$ abgegriffen werden kann, ohne dass der Eingang belastet wird. Somit kommt es zu keiner Spannungsänderung am Eingangssignal durch die Last am Ausgang.

Der Spannungsfolger kann verwendet werden, um die Ausgangsspannung eines Spannungsteilers abzugreifen, ohne den Spannungsteiler zu belasten. 

## Die Feedback-Schleife

Der einfache Fall, in dem das Feedback aus einer direkten Verbindung von Ausgang und invertierendem Eingang besteht, kann durch das Einfügen von Bauelementen in die Feedback-Schleife erweitert werden. Elektrische Bauelemente haben einen Einfluss auf die Spannung des rückführenden Signals wodurch sich die Ausgangsspannung des OPVs verändert, um die dritte goldene Regel zu erfüllen. In **Abbildung 4** wird dieses Konzept dargestellt. Dabei können je nach Anwendungszweck sowohl das veränderte als auch das ursprüngliche Eingangssignal als Ausgang weiterverwendet werden.

---

<img src="../figures/feedback_loop_strange.png" width="600" style="zoom:100%;"/>

**Abbildung 4**: (Durch Hinzufügen von Bauteilen in die Feedback-Schleife verändert sich das Ausgangssignal des OPVs, damit die dritte goldene Regel erfüllt wird. Dabei können sowohl das veränderte als auch das ursprüngliche Eingangssignal abgenommen werden.)

---

Bei einer bekannten Feedback-Schleife lässt sich das veränderte Ausgangssignal des OPVs bestimmen. Die Feedback-Schleife transformiert eine Spannung $U$ wie eine mathematische Funktion $\mathfrak{F}(U)$. Da das Feedback-Signal am invertierenden Eingang anliegt und zum Eingangssignal identisch ist, muss das Ausgangssignal des OPVs so gewählt werden, dass gilt:
$$
U_\mathrm{out} = \mathfrak{F}^{-1}(U_\mathrm{in})
$$
mit der inversen Funktion $\mathfrak{F}^{-1}$ der Feedback-Funktion $\mathfrak{F}$. In **Abbildung 5** ist dieses Prinzip dargestellt. In den nachfolgenden Schaltungen wird die Feedback-Schleife zur Umsetzung gezielter Veränderungen des Eingangsssignals entworfen.

---

<img src="../figures/feedback_loop_description.png" width="500" style="zoom:100%;"/>

**Abbildung 5**: (Das Ausgangssignal des OPVs lässt sich über die inverse der Feedback-Funktion bestimmen.)

---

## Nicht-invertierender Verstärker

Der Nicht-invertierende Verstärker verwendet einen Spannungsteiler in der Feedback-Schleife, um eine Spannungsverstärkung zu realisieren. Die Schaltung ist in **Abbildung 6** dargestellt.

**TODO: Continue**



# Fortsetzung: Die goldenen Regeln 

Die Verstärkerschaltungen lassen sich mit den goldenen Regeln erklären. Dennoch gibt es Grenzen, in denen die goldenen Regeln gelten:

- Die goldenen Regeln basieren auf dem Prinzip des negativen Feedbacks. Wenn kein Feedback ankommt (z.B. durch einen Kabelbruch oder einen extrem hochohmigen Widerstand in der Feedback-Schleife) oder wenn das Feedback nicht an dem invertierenden Eingang anliegt, gelten die goldenen Regeln nicht.
- Die goldenen Regeln gelten nur, solange der OPV nicht gesättigt ist. Das bedeutet, dass die Ausgangsspannung des OPVs innerhalb der Grenzen der Versorgungsspannung liegen muss. Wenn die Ausgangsspannung diese Grenzen überschreitet, kann der OPV die dritte goldene Regel nicht mehr erfüllen, da er keine Spannung $\gt{}V_\mathrm{S+}$ oder $\lt{}V_\mathrm{S-}$ ausgeben kann.
- Bei hohen Frequenzen verhält sich der OPV wie ein Tiefpass-Filter, wodurch die Verstärkung abfällt. Ebenfalls können schnelle Änderungen an den Eingangssignalen bei hoher Verstärkung nicht immer am Ausgang nachverfolgt werden (Slew-Rate-Beschränkung), da der OPV nur eine begrenzte Änderungsrate der Ausgangsspannung (für den LM358: $0,3 \frac{\mathrm{V}}{\mathrm{\mu{}s}}$) liefern kann.


## Essentials

Was Sie ab jetzt wissen sollten:

- Operationsverstärker haben einen **invertierenden (N-) und einen nicht-invertierenden P-Eingang**. Im allgemeinen werden Sie zur **Spannungsverstärkung** eingesetzt. 
- Für die äußere Beschaltung mit Widerständen (Dimensionierung) gelten zur groben Abschätzung die **golgenen Regeln**. Diese sollten Sie benennen können. 

## Testfragen

1. Was macht eine ideale Spannungsquelle aus?
2. Was sagt die dritte Goldene Regel zur Dimenionsierung von OPVs über $X_{a}$ aus?

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Operationsverstaerker)

