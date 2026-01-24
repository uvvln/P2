# Bilder von Schaltungen

## Bilder erstellen

Dieses Verzeichnis beinhaltet LaTeX CircuiTikz Zeichnungen von Schaltplänen.

Die Datei `minimal.tex` ist ein von Pdflatex kompilierbares Dokument, in dem die Schaltpläne eingebunden sind. Die Schaltpläne sind in separaten Dateien gespeichert.

Um einen Schaltplan in ein PDF-Bild zu kompilieren, muss zuerst in der Datei `minimal.tex` der gewünschte Schaltplan eingebunden werden. Anschließend kann die LaTeX-Datei über die Kommandozeile mit `latexmk -pdf minimal.tex` kompiliert werden. Die von Pdflatex erzeugte PDF-Datei (minimal.pdf) enthält den Schaltplan. Mit dem Befehl `latexmk -C` können die Hilfsdateien, die während der Kompilierung erzeugt wurden, wieder entfernt werden.

Unter Ubuntu müssen folgende Packete installiert sein:
- texlive
- texlive-pictures
- texlive-scientific
- latexmk

### Circuitikz-Anleitung:

Die Datei `anleitung_circuitikz.tex` ist ein LaTeX-Dokument, welches in den Kommentaren innerhalb des LaTeX-Dokuments eine Anleitung zur Verwendung von Circuitikz enthält. Diese Datei kann ebenfalls mit `latexmk -pdf anleitung_circuitikz.tex` kompiliert werden.
Bevor die Bilder für die Praktikums-Anleitung bearbeitet werden, sollte diese Anleitung gelesen werden. Für alle danach verbleibenden Fragen sollte ein Blick in das [Circuitikz-Handbuch](https://ctan.dcc.uchile.cl/graphics/pgf/contrib/circuitikz/doc/circuitikzmanual.pdf) helfen.

## PDF in PNG umwandeln

Die PDF-Dateien können mit **ImageMagick** in PNG Bilder umgewandelt werden. Dabei sind ein paar Kommandozeilen-Parameter wichtig, um die Auflösung und den Hintergrund richtig zu setzen. Folgender Befehl wandelt die Datei `image.pdf` in die Datei `image.png` um:
```bash
magick convert \
    -density 500 \  # the PDF file DPI, higher means better quality
    image.pdf \  # the target file
    -quality 100 \  # use the compression with the highest quality for the PNG file
    image.png  # the output file
````
Für gewöhnlich wird das in der Kommandozeile in einer einzigen Zeile gemacht und würde so aussehen:
```bash
magick convert -density 500 image.pdf -quality 100 image.png
```
### Hintergrund bearbeiten

Manchmal sind weiße Flächen in Kreisen. Diese können mit den folgenden Argumenten vor der Ausgabedatei transparent gemacht werden: `-fuzz 50% -transparent white`. Der Fuzz-Wert gibt vor, wie _ähnlich_ zwei Farben zueinander sind und muss eventuell angepasst werden (meistens werden mehr als 50% benötigt, damit auch weniger ähnliche Farbtöne als weiß angesehen werden).

Falls der transparente Hintergrund wieder weiß gemacht werden soll, können die folgenden Argumente vor der Ausgabedatei verwendet werden: `-background white -alpha remove -alpha off`.

Ein weiterer Trick, um alle nicht-transparenten Pixel schwarz zu machen:
```bash
magick convert image.png -alpha extract -threshold 0 -negate -transparent white image.png
````
