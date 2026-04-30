# Spezifische Wärmekapazität

## Spezifische Wärmekapazität als Funktion der Temperatur

Für diese Messung kühlen Sie einen Aluminium-Hohlzylinder (AL) in einem Wärmebad von Flüssigstickstoff auf möglichst tiefe Temperaturen ab. Unter Normaldruck beträgt die Siedetemperatur von Stickstoff $77\ \mathrm{K}\ (-196^{\circ}\mathrm{C})$. Daraufhin führen Sie dem AL durch eine Heizspule mit der konstanten Leistung $P_{\mathrm{Heiz}}$ kontrolliert in einem Zeitintervall $\mathrm{d}t$ die Wärmemenge 
$$
\begin{equation*}
\delta Q_{\mathrm{Heiz}} = P_{\mathrm{Heiz}}\,\mathrm{d}t
\end{equation*}
$$
zu. Da dabei keine Arbeit verrichtet wird ($\delta W=0$) geht $\delta Q_{\mathrm{Heiz}}$ vollständig in innere Energie ($\mathrm{d}U$) über:
$$
\begin{equation}
P_{\mathrm{Heiz}}\,\mathrm{d}t = \delta Q_{\mathrm{Heiz}} = \mathrm{d}U = c_{\mathrm{Al}}(T)\,m_{\mathrm{Al}}\,\mathrm{d} T.
\tag{1}
\end{equation}
$$
Daraus ergibt sich 

$$
\begin{equation}
\begin{split}
&c_{\mathrm{Al}}(T) = \frac{P_{\mathrm{Heiz}}}{m_{\mathrm{Al}}\, \dot{T}(T)};\\ 
&\\
&\text{mit}\\
&\\
&\dot{T}(T) = \lim\limits_{\Delta t\to0}\left(\frac{\Delta T}{\Delta t}\right).\\ 
\end{split}
\tag{2}
\end{equation}
$$

### Messprinzip

🔔 **Für die Messung sind $m_{\mathrm{Al}}$ und $P_{\mathrm{Heiz}}$ durch den experimentellen Aufbau fest vorgegeben. Zu messen ist der Verlauf $\dot{T}(T)$.** 🔔

Die Daten hierzu nehmen Sie, mit Hilfe eines Datenloggers, automatisiert auf. Es handelt sich um Spannungen eines [$\text{NiCr-Ni}$-Thermoelements](https://de.wikipedia.org/wiki/Thermoelement) (TE, in Volt) als Funktion der Zeit (in Sekunden), in der der Datenlogger die Werte ausließt. 

🔔 Aus diesen Daten den Verlauf von $c_{\mathrm{Al}}(T)$ im Rahmen dieser Aufgabe zu extrahieren ist eine nicht triviale **Übung der Datenanalyse**, die wir im folgenden in vier Schritten etwas weiter ausführen werden. 

🔔 Protokollieren Sie Ihr Vorgehen während des Versuchsablaufs so, dass Sie später in **jedem einzelnen Schritt** eine klare Motivation Ihres Handelns, die Schwierigkeiten und wichtigsten Punkte, auf die bei der Bearbeitung der jeweiligen Teilaufgabe zu achten ist, ggf. das Ergebnis der Aufgabe und eine Einschätzung dazu ableiten können. 

#### (1) Beschreibung der Rohdaten

Damit Sie später maximal vom Dokument Ihrer Arbeit profitieren können, stellen Sie Ihrer Auswertung eine hinreichende Beschreibung der Rohdaten voran. Hierzu sollten Sie Ihrem Protokoll nicht nur eine Beschreibung Ihres Vorgehens (**Aufgabe 2.1**), sondern auch eine Beschreibung der Funktionsweise des TE (**Aufgabe 2.2**) zufügen.

#### (2) Kalibration

Zur Kalibration der Daten (**Aufgabe 2.2**) benötigen Sie Messpunkte $(U_{i}, T_{i})$, die die gemessenen Spannungen ($U_{i}$) des TE mit Temperaturen ($T_{i}$) verknüpfen. Wir stellen Ihnen eine solche Messung in der Datei [calibration.csv](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Spezifische_Waermekapazitaet/params/calibration.csv) bereit. 

💡 Die zu extrahierende **Kalibrationskurve bezeichnen wir als $K(U, T)$**. Eine durch ein Modell der physikalischen Vorgänge motivierte Parametrisierung kann nützlich sein, ist in diesem Fall aber nicht zwingend, da Sie ohnehin schwer alle eine solche Messung beeinflussenden äußeren Parameter kontrollieren können. Trotzdem sollten Sie auf **relative Einfachheit der funktionalen Form** achten.  

🔔 Für Ihr weiteres Vorgehen ist eine Einschätzung der Güte des Modells für $K(U,T)$, z.B. basierend auf dem $\chi^{2}$-Wert der Anpassung unumgänglich. Hierzu ist eine seriöse Angabe der Unsicherheiten $\Delta U_{i}$ und $\Delta T_{i}$ unerlässlich. Sie sollten darauf achten, dass $K(U, T)$ die Datenpunkte nach der Anpassung wirklich gut beschreibt, denn **diese Kalibrationskurve bildet die Grundlage für alle weiteren Schritte**. Wenn Ihre Kalibrationskurve $K(U, T)$ den Verlauf der Datenpunkte nicht hinreichend gut beschreiben kann sind somit alle weiteren Schritte zur Bestimmung von $c_{\mathrm{Al}}(T)$ in Frage gestellt. 

#### (3) Korrektur des Wärmegangs

Wenn der AL zusätzlich zur Wärmezufuhr 
$$
\begin{equation*}
\delta Q_{\mathrm{Heiz}} = P_{\mathrm{Heiz}}\,\mathrm{d}t
\end{equation*}
$$
Wärme $\delta Q_{0}$ aus der Umgebung aufnimmt führt dies offensichtlich zu einer Verzerrung der Daten. Man bezeichnet diesen Vorgang als [Wärmegang](https://de.wikipedia.org/wiki/W%C3%A4rme%C3%BCbergangskoeffizient). Sie können diesen Effekt mit Hilfe einer Leermessung ohne elektrische Wärmezufuhr abschätzen und die originale Messung a posteriori (d.h. nachdem die Messung bereits beendet wurde) entsprechend korrigieren. Wir haben eine solche Leermessung, in der Datei [waermegang.csv](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Spezifische_Waermekapazitaet/params/waermegang.csv), für Sie bereitgestellt. 

💡 Der Wärmegang ist umso größer, je größer die Differenz zwischen Innen- und Außentemperatur des Messaufbaus ist, die entscheidende Größe dabei ist $\dot{T}_{0}(T)$. Die Korrektur besteht darin, $\dot{T}_{0}(T)$ vom Verlauf $\dot{T}^{\prime}(T)$ der aufgezeichneten Daten abzuziehen:

$$
\begin{equation}
\dot{T}(T) = \dot T^{\prime}(T)-\dot T_0(T).
\tag{3}
\end{equation}
$$

Ob Sie die Korrektur des Wärmegangs auf den Rohdaten des TE (in Volt) oder auf den kalibrierten Daten (in Kelvin) durchführen scheint zunächst gleich. Tatsächlich macht es mehr Sinn, den Wärmegang erst zu kalibrieren und dann als $\dot{T}_{0}(t)$ zu bestimmen. (💡 Beachten Sie, dass $K(U,T)$ i.a. keine Gerade ist!) Durch die Kalibration auf $\dot{T}_{0}(t)$ sollte es Ihnen möglich sein den Wärmegang durch eine einfache und physikalisch motivierte funktionale Form zu beschreiben, die Sie in den weiteren Aufgabenteilen leicht weiter verwenden können. 

In der Vergangenheit hat sich ein einfaches Modell der Form 

$$
\begin{equation}
T_{0}(t)=a_{0}\,e^{-t/b_{0}}+c_{0}
\tag{4}
\end{equation}
$$
zur Beschreibung des Verlaufs $T_{0}(t)$ der Leermessung als Funktion der Zeit bewährt, wobei $a_{0},\ b_{0},\ c_{0}$ freie Parameter des Modells sind. Die Ableitung dieses Modells nach $t$ ist leicht analytisch durchzuführen und führt auf die Form 

$$
\begin{equation}
\dot{T_{0}}(t) = -\frac{a_{0}}{b_{0}}\cdot e^{-t/b_{0}}.
\tag{5}
\end{equation}
$$

Mit der zugehörigen Umkehrfunktion zu Gleichung **(4)**
$$
\begin{equation*}
t(T_{0}) = b_{0}\cdot\ln\left(\frac{a_{0}}{T_{0}-c_{0}}\right)
\end{equation*}
$$

ergibt sich nach Einsetzen in Gleichung **(5)** der gewünschte Zusammenhang

$$
\begin{equation}
\dot{T_{0}}(T) = \frac{c_{0}-T}{b_{0}}.
\tag{6}
\end{equation}
$$
Auch für diese Aufgabe ist eine Diskussion der Güte des Modells, z.B. basierend auf dem $\chi^{2}$-Wert der Anpassung an die Daten unumgänglich. 🔔 Wenn das Modell aus Gleichung **(4)** den Verlauf der Daten nicht hinreichend gut beschreiben kann ist die Verwendung des funktionalen Zusammenhangs aus Gleichung **(6)** in Frage gestellt.

#### (4) Finale Bestimmung von $\dot{T}(T)$

🔔 Die Bestimmung von $\dot{T}(T)$ erfolgt auf den kalibrierten Daten nach Korrektur des Wärmegangs der Apparatur auf Grundlage der Leermessung, wie durch Gleichung **(3)** angegeben.

Bestimmen Sie hierzu zunächst durch Anpassung eine analytische Funktion zur Beschreibung des Verlaufs von $T'(t)$. Hierzu eignet sich ähnlich zu Gleichung **(4)** ein Modell der Form

$$
\begin{equation}
T'(t) = a\,t^{b} + c,
\tag{7}
\end{equation}
$$
mit den freien Parametern $a,\ b,\ c$.  Aus dem Modell können Sie die Ableitung wie folgt leicht bestimmen: 

$$
\begin{equation*}
\dot{T}'(t) = a\,b\,t^{b-1}.
\end{equation*}
$$
Um $\dot{T}'(T)$ zu bestimmen benötigen Sie noch die Umkehrfunktion zu Gleichung **(7)** 

$$
\begin{equation*}
t(T) = \left(\frac{T-c}{a}\right)^{1/b}.
\end{equation*}
$$
Nach Einsetzen ergibt sich der gesuchte Zusammenhang 
$$
\begin{equation*}
\dot{T}'(T) = a\, b\, \left(\frac{T-c}{a}\right)^{\frac{b-1}{b}}.
\end{equation*}
$$
Auch hier ist es wieder essentiell sehr gewissenhaft, z.B. basierend auf dem $\chi^{2}$-Wert der Anpassung, zu kontrollieren, wie gut das Modell aus Gleichung **(7)** die Datenpunkte beschreiben kann. Nur in dem Rahmen, in dem dies gewährleistet ist ergibt der Verlauf von $c_{\mathrm{Al}}(T)$ einen Sinn.   

## Erwartung

Was wir an dieser Stelle von Ihnen erwarten:

- ✅ Sie verstehen die Funktionsweise des TE.

- ✅ Sie verstehen die Bedeutung der Kalibrationskurve.

- ✅ Sie sind sich der Feinheiten bei der Korrektur des Wärmegangs bewusst. 

- ✅ Sie verstehen, wie Sie durch die einzelnen Messschritte zur Bestimmung von $\dot{T}(T)$ kommen und können das Messprinzip in eigenen Worten wiedergeben.


## Testfragen

1. Welche Vorteile hat die Verwendung des TE gegenüber einem normalen Thermometer?
2. Sowohl die Leermessung zur Bestimmung des Wärmegangs, als auch die eigentliche Messung beruhen auf Messreihen als Funktion er Zeit. Wie kommt es, dass in Ihrem Messergebnis der Parameter $t$ (d.h. die Zeit) überhaupt nicht mehr auftaucht?

---

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Spezifische_Waermekapazitaet/README.md)
