# latexfixer

## Description

A small class to normalise unicode to latex-compatible unicode, with fixes for some common typographic errors.

## Usage

    from latexfixer.fix import LatexText

    string = 'Hello, Prof. World'
    string = LatexText(string) # 'Hello Prof.~World'