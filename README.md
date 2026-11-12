# Mach–Zehnder interference

A guided investigation, **From Interference to a Beam Angle**, connecting interference, fringe spacing, beam angle, and lens magnification.

[Compiled worksheet](worksheet.pdf)

© 2026 Amy Roberts  
ORCID: [0000-0001-8538-9155](https://orcid.org/0000-0001-8538-9155)  
Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). See [LICENSE.txt](LICENSE.txt).

## Reproduce the worksheet

Install Python 3, GNU Make, a TeX distribution with `pdflatex` and `latexmk` (MacTeX or TeX Live), and an SVG renderer. The recommended renderer is librsvg (`brew install librsvg` on macOS; `sudo apt install librsvg2-bin` on Debian/Ubuntu).

Alternatively, install CairoSVG and its system Cairo dependency using a virtual environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

Install DejaVu Sans and Arial (or Liberation Sans as an Arial substitute) for the figure text. Rendering may vary slightly with local fonts or tool versions.

From the repository root:

```sh
make
```

This regenerates the triptych SVG using `make_triptych.py`, converts all eight editable SVGs to PDF using `render_figures.py`, and compiles `worksheet.tex` into `worksheet.pdf`. No files outside this repository are used as content inputs. Dependencies must be installed separately.

Individual steps:

```sh
python3 make_triptych.py
python3 render_figures.py
latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
```

`make pdf` compiles using the included figure PDFs. `make clean` removes intermediate TeX files and preserves the compiled PDF.

## Files and provenance

- `worksheet.tex`: complete editable worksheet source.
- `figures/*.svg`: all eight recovered editable figures, including the unused alternate adjacent-fringe diagram.
- `figures/*.pdf`: figure PDFs regenerated from those SVGs.
- `figures/01_wavefronts_updated.png`: additional image preserved from the source archive; not used by the LaTeX.
- `make_triptych.py`: the only Python figure generator present in the recovered archive; its drawing instructions are preserved, with rendering delegated to `render_figures.py`.
- `render_figures.py`: added conversion utility for every SVG.
- `worksheet.pdf`: compiled worksheet.

Recovered from `Mach_Zehnder_Worksheet_v36_Source.zip` in the author's Downloads folder. Archive SHA-256: `a9e5564ffabfb190eef943029999e13a93b97d95b40ef88eee465117db0e5022`. All downloaded copies labeled Version 36 or RECOVERED had this same checksum. The referenced chat was not directly readable in this session; the downloaded archive is the recovered baseline.

The source archive contained no Python generators for the other seven SVG figures. Those figures are fully editable SVG sources and can be rendered directly; no missing generator is required to reproduce them.

Changes from that baseline: the requested triptych introduction; “Out of phase: destructive interference” heading; an explanation of partial cancellation for unequal field amplitudes; and linked author, ORCID, and CC BY 4.0 attribution. Question 4(c) now says “Mark the three locations on the screen” following author review. Question 7 asks students to show the small-angle limit, refers to the derivation in Question 6, and omits the redundant final instruction. Other worksheet prose and figure geometry are preserved. The redundant triptych snapshot label was removed after review. The fancyhdr footer puts the page number on the left and the copyright, ORCID, and “All materials herein CC BY 4.0” statement on the right. First-page figure spacing preserves the eight-page layout. Header-height and PDF transparency-group compatibility adjustments ensure a clean build. Build instructions, licensing, and conversion tooling were added.

## Verification

See [VERIFICATION.md](VERIFICATION.md) for compilation and rendering checks.
