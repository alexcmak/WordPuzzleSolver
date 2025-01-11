# WordPuzzleSolver
Go a word word puzzle and don't want to find the words yourself? I've got you.


This program also uses [pytest](https://docs.pytest.org/en/stable/) for unit testing.


```
C:\>python PuzzleSolver.py
puzzle file puzzle.txt successfully read
----------------
f. find word
p. show puzzle
s. show found words
q. quit
Your choice: p
   0123456789
 0 ZFOHFTEPZP
 1 XNJEVUOFHT
 2 JQRVAYCUXB
 3 PKIPIWECAZ
 4 ATPXLMFBIT
 5 HLAFRRGBQR
 6 EZZCROZXWX
 7 BPPZGCVAKI
 8 ANANABZSDZ
----------------
f. find word
p. show puzzle
s. show found words
q. quit
Your choice: f
Find a word: APPLE
### Word found! ###
----------------
f. find word
p. show puzzle
s. show found words
q. quit
Your choice: s

   0123456789
 0 ..........
 1 ..........
 2 ....A.....
 3 ...P......
 4 ..P.......
 5 .L........
 6 E.........
 7 ..........
 8 ..........
----------------

```

# ImageToPuzzle

Use python OCR to read an image and convert into a text file for use with Word Puzzle Solver
This program uses tesseract.

Follow this video [How to use Tesseract OCR in a Python script (pytesseract)](https://www.youtube.com/watch?v=HNCypVfeTdw) to get pyton OCR to work on your computer.

You will need to install that also the PIL library, too