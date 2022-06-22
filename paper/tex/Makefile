TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
BIB = bibtex

TEXFILE = main

default: all

.PHONY: all view

all : $(TEXFILE).pdf

view :
	open $(TEXFILE).pdf

$(TEXFILE).pdf : $(TEXFILE).tex $(TEXFILE).bbl $(TEXFILE).blg
	$(TEX) $(TEXFILE).tex

$(TEXFILE).bbl $(TEXFILE).blg : $(TEXFILE).bib $(TEXFILE).aux
	$(BIB) $(TEXFILE)

$(TEXFILE).aux : $(TEXFILE).tex
	$(TEX) $(TEXFILE).tex

$(TEXFILE).bib : $(TEXFILE).tex
	$(TEX) $(TEXFILE).tex

clean:
	rm -f $(TEXFILE).bbl
	rm -f $(TEXFILE).aux
	rm -f $(TEXFILE).log
	rm -f $(TEXFILE).blg
	rm -f $(TEXFILE).lof
