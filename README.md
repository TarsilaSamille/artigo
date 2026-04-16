# SBC Conferences Template - Bidaio Jagoy Translator

This repository contains the LaTeX source files for the paper: **"Bidaio Jagoy Translator: A Hybrid Client-Centric RAG System for Low-Resource Language Preservation"**.

## Prerequisites

To compile this project, you need a LaTeX distribution installed on your system:
- **macOS:** [MacTeX](https://tug.org/mactex/)
- **Windows:** [MiKTeX](https://miktex.org/) or [TeX Live](https://tug.org/texlive/)
- **Linux:** [TeX Live](https://tug.org/texlive/)

## How to Generate the PDF

### Option 1: Using `latexmk` (Recommended)

`latexmk` is an automated tool that handles all necessary compilation steps (including bibliography) and re-runs when needed.

```bash
latexmk -pdf main.tex
```

To clean up auxiliary files after compilation:
```bash
latexmk -c
```

### Option 2: Manual Compilation

If you don't have `latexmk`, you can run the following commands in sequence:

1. Compile the document:
   ```bash
   pdflatex main.tex
   ```
2. Process the bibliography:
   ```bash
   bibtex main
   ```
3. Re-compile to resolve references (twice):
   ```bash
   pdflatex main.tex
   pdflatex main.tex
   ```

## Project Structure

- `main.tex`: The main LaTeX source file.
- `sbc-template.sty`: The SBC (Brazilian Computer Society) conference style file.
- `references.bib`: Bibliography file containing all citations.
- `sbc.bst`: BibTeX style file.
- `*.png`, `*.jpg`: Figure and diagram files.

## Output

The generated PDF will be saved as `main.pdf`.
