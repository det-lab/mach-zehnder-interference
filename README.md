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

This regenerates the triptych SVG using `make_triptych.py` and the apparatus schematic using `make_setup.py`, converts all nine editable SVGs to PDF using `render_figures.py`, and compiles `worksheet.tex` into `worksheet.pdf`. No files outside this repository are used as content inputs. Dependencies must be installed separately.

Individual steps:

```sh
python3 make_triptych.py
python3 make_setup.py
python3 render_figures.py
latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
```

`make pdf` compiles using the included figure PDFs. `make clean` removes intermediate TeX files and preserves the compiled PDF.

## Files and provenance

- `worksheet.tex`: complete editable worksheet source.
- `figures/*.svg`: all eight recovered editable figures plus the new apparatus schematic, including the unused alternate adjacent-fringe diagram.
- `figures/*.pdf`: figure PDFs regenerated from those SVGs.
- `figures/01_wavefronts_updated.png`: additional image preserved from the source archive; not used by the LaTeX.
- `make_triptych.py`: the only Python figure generator present in the recovered archive; its drawing instructions are preserved, with rendering delegated to `render_figures.py`.
- `render_figures.py`: added conversion utility for every SVG.
- `make_setup.py`: original Python generator for the apparatus schematic, including the output lens and the lens-to-screen distance L.
- `worksheet.pdf`: compiled worksheet.

Recovered from `Mach_Zehnder_Worksheet_v36_Source.zip` in the author's Downloads folder. Archive SHA-256: `a9e5564ffabfb190eef943029999e13a93b97d95b40ef88eee465117db0e5022`. All downloaded copies labeled Version 36 or RECOVERED had this same checksum. The referenced chat was not directly readable in this session; the downloaded archive is the recovered baseline.

The source archive contained no Python generators for the other seven SVG figures. Those figures are fully editable SVG sources and can be rendered directly; no missing generator is required to reproduce them.

Changes from that baseline: the requested triptych introduction; “Out of phase: destructive interference” heading; an explanation of partial cancellation for unequal field amplitudes; and linked author, ORCID, and CC BY 4.0 attribution. Question 4(c) now says “Mark the three locations on the screen” following author review. Question 7 guides students through a Taylor approximation about zero: identify the small dimensionless parameter, construct the sine expansion, compare the cubic and linear terms, and derive the small-angle limit. It provides the general expansion formula, an explanation of why simpler approximations are useful, and optional 3Blue1Brown and MIT OpenCourseWare resources. Parts D and E use the directly measured lens-to-screen distance $L$ throughout; the former distances $D$ and $a$ have been removed from the worksheet. The measurement table, far-screen approximation, uncertainty prompt, and screen-movement question use $L$. Question 14 asks students to derive the far-screen approximation from Question 12 and calculate f/L from experimental values and explain why it can be neglected before propagating uncertainty. Other worksheet prose and figure geometry are preserved. The redundant triptych snapshot label was removed after review. The fancyhdr footer puts the page number on the left and the copyright, ORCID, and “All materials herein CC BY 4.0” statement on the right. First-page figure spacing is compact. The Taylor-approximation activity begins on its own page to provide room for student work, with additional page breaks around the apparatus and derivation activities; the current worksheet is ten pages. Header-height and PDF transparency-group compatibility adjustments ensure a clean build. Build instructions, licensing, and conversion tooling were added.

## Apparatus schematic reference

The original schematic in `figures/03_setup.svg` uses the standard Mach–Zehnder arrangement. The [Thorlabs EDU-QE1 User Guide, Rev E, printed page 4, Figure 1](https://lenlasers.ru/upload/iblock/365/EDU_QE1_M-Manual.LLS.pdf) was consulted as an apparatus reference (distributor-hosted copy). No artwork or photographs were extracted, traced, or included. The lens placement follows the author's lab: after the second beam splitter, with L measured to the screen. This differs from the manual's input-lens arrangement for ring patterns. The diagram and its generator are original material under this repository's CC BY 4.0 license.

The apparatus schematic and alignment caption appear at the start of Part D. The worksheet is now ten pages, with page breaks that keep the derivations and questions together. Question 14 asks students to calculate f/L using their experimental values and explain why the term can be neglected.

## Verification

See [VERIFICATION.md](VERIFICATION.md) for compilation and rendering checks.
