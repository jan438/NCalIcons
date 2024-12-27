import os
import sys
from pathlib import Path

SUMMARY = "SUMMARY".encode()
DESCRIPTION = "DESCRIPTION".encode()
ICONPREFIX = '[i'.encode()

def find_all_occurrences(line, sub, f, t):
    index_of_occurrences = []
    current_index = f
    while True:
        current_index = line.find(sub, current_index)
        if current_index == -1 or current_index >= t:
            return index_of_occurrences
        else:
            index_of_occurrences.append(current_index)
            current_index += len(sub)
            
def process_summarypos(line, pos):
    processed = line[pos+1:]
    return processed
            
if sys.platform[0] == 'l':
    path = '/home/jan/git/NCalIcons/IconIndexes'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/NCalIcons/IconIndexes"
os.chdir(path)
src = "Ent.ics"
inpfile = open(src, 'rb')
line = inpfile.read()

summarypos = line.find(SUMMARY)
while summarypos > 0:
    print(line[summarypos+8:summarypos+13])
    line = process_summarypos(line, summarypos)
    summarypos = line.find(SUMMARY)
inpfile.close()
key = input("Wait")
