#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sun March 28 18:39:59 2021

@author: Richard
"""

import csv
import time
import sys

sourceData = "../data/Sample_OnlineRetail.csv"
placeholder = "../output/LastLine.txt"

""" with open(sourceData) as file:
    # csv_reader = csv.reader(file)
    for i, l in enumerate(file):
        print(i,l)
 """

def GetLineCount():
    with open(sourceData) as file:
        for i, l in enumerate(file):
            pass
    return i

def MakeLog(startLine, numLines):
    desData = time.strftime("../output/%Y%m%d-%H%M%S.log")
    with open(sourceData, 'r') as csvfile:
        with open(desData, 'w') as dstfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(dstfile)
            next(reader)
            inputRow = 0
            linesWritten = 0
            for row in reader:
                inputRow += 1
                if (inputRow > startLine):
                    writer.writerow(row)
                    linesWritten += 1
                    if (linesWritten >= numLines):
                        break
            return linesWritten


startLine = 0
numLines = 3

print(sys.argv)

if (len(sys.argv) > 1):
    numLines = int(sys.argv[1])

try:
    with open(placeholder, 'r') as file:
        for line in file:
            startLine = int(line)
except IOError:
    startLine = 0

print("Writing " + str(numLines) + " lines starting at line " + str(startLine) + "\n")

totalLinesWritten = 0
linesInFile = GetLineCount()

while (totalLinesWritten < numLines):
    linesWritten = MakeLog(startLine, numLines - totalLinesWritten)
    totalLinesWritten += linesWritten
    startLine += linesWritten
    if (startLine >= linesInFile):
        startLine = 0

print("Wrote " + str(totalLinesWritten) + " lines.\n")



with open(placeholder, 'w') as file:
    file.write(str(startLine))
