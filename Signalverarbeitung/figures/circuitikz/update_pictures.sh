#!/bin/bash

# Create the output directory for all the output files
SCRIPT_DIR="$(dirname "$0")"
OUTPUT_DIR="output_pdf"
mkdir -p "$SCRIPT_DIR/$OUTPUT_DIR"

# Loop through all the .tikz files and convert them to .pdf using latexmk
for file in "$SCRIPT_DIR"/*.tikz; do
    base=$(basename "$file" .tikz)

    cat <<EOF >> "$SCRIPT_DIR/$base.tex"
\documentclass[border=2mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{circuits.logic.IEC}
\usetikzlibrary{arrows.meta}
\usetikzlibrary{math}
\usepackage[siunitx, european]{circuitikz}
\usepackage{amssymb}  % mathematical expressions
\usepackage{siunitx}
\sisetup{locale = DE}
\begin{document}
$(cat "$file")
\end{document}
EOF

		latexmk -pdf -interaction=nonstopmode -output-directory="$SCRIPT_DIR/$OUTPUT_DIR" "$SCRIPT_DIR/$base.tex"
		rm "$SCRIPT_DIR/$base.tex"
		magick convert -density 500 "$SCRIPT_DIR/$OUTPUT_DIR/$base.pdf" -quality 100 -background white -alpha remove -alpha off "$SCRIPT_DIR/../$base.png"
		latexmk -C
done

rm -rf "$SCRIPT_DIR/$OUTPUT_DIR"
