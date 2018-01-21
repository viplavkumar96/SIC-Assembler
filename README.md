# SIC-Assembler
SIC-Assembler(Python) is the tool to convert SIC program(HL) to machine code which is understood by SIC.
Simplified Instructional Machine is a hypothetical machine used by many researchers to understand the basis of assemblers, linkers and loaders. This project is an implementation of SIC Assembler. What it basically does is take a SIC program and translates it into a object code which is intended for the the SIC to understand.


#--Run pass1 and pass2 to obtain the machine code--#

#--Will also work if pass1.py, pass2.py and inp.txt are there in the project. Rest are for only demonstration pusrpose.--# 

inp.txt -> inpute file(SIC program)

Intermediatefile.txt --> Intermediate File is created after pass one of assembler.

SymbolTab.txt  --> Contains the name of symbols and addresses after pass one.

ObjectProgram.txt --> Contains the generated object code.

