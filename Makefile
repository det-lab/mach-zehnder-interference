.PHONY: all figures pdf clean
PYTHON ?= python3
all: figures pdf
figures:
	$(PYTHON) make_triptych.py
	$(PYTHON) render_figures.py
pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error worksheet.tex
clean:
	latexmk -c worksheet.tex
