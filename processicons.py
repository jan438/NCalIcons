import os
import sys
from pathlib import Path

SUMMARY = "SUMMARY".encode()
DESCRIPTION = "DESCRIPTION".encode()
ICONPREFIX = '[i'.encode()
ICONSUFFIX = ']'.encode()
linebreak = '\r\n'.encode()

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
            
ncalicons = []
if sys.platform[0] == 'l':
    path = '/home/jan/git/NCalIcons/IconIndexes'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/NCalIcons/IconIndexes"
os.chdir(path)
#src = "Ent.ics"
#inpfile = open(src, 'rb')
#line = inpfile.read()
#summarypos = line.find(SUMMARY)
#while summarypos > 0:
#    ncalicon = ""
#    linebreakpos = line.find(linebreak, summarypos)
#    ncalicon = ncalicon + line[summarypos+8:linebreakpos].decode('utf-8')
#    line = line[linebreakpos:]
#    descriptionpos = line.find(DESCRIPTION)
#    closingpos = line.find(ICONSUFFIX, descriptionpos)
#    ncalicon = ncalicon + ":" + line[descriptionpos+14:closingpos].decode('utf-8')
#    ncalicons.append(ncalicon)     
#    summarypos = line.find(SUMMARY)
#inpfile.close()
#src = "General.ics"
#inpfile = open(src, 'rb')
#line = inpfile.read()
#summarypos = line.find(SUMMARY)
#while summarypos > 0:
#    ncalicon = ""
#    linebreakpos = line.find(linebreak, summarypos)
#    ncalicon = ncalicon + line[summarypos+8:linebreakpos].decode('utf-8')
#    line = line[linebreakpos:]
#    descriptionpos = line.find(DESCRIPTION)
#    closingpos = line.find(ICONSUFFIX, descriptionpos)
#    ncalicon = ncalicon + ":" + line[descriptionpos+14:closingpos].decode('utf-8')
#    ncalicons.append(ncalicon)     
#    summarypos = line.find(SUMMARY)
#inpfile.close()
#src = "Others.ics"
#inpfile = open(src, 'rb')
#line = inpfile.read()
#summarypos = line.find(SUMMARY)
#while summarypos > 0:
#    ncalicon = ""
#    linebreakpos = line.find(linebreak, summarypos)
#    ncalicon = ncalicon + line[summarypos+8:linebreakpos].decode('utf-8')
#    line = line[linebreakpos:]
#    descriptionpos = line.find(DESCRIPTION)
#    closingpos = line.find(ICONSUFFIX, descriptionpos)
#    ncalicon = ncalicon + ":" + line[descriptionpos+14:closingpos].decode('utf-8')
#    ncalicons.append(ncalicon)     
#    summarypos = line.find(SUMMARY)
#inpfile.close()
src = "Work.ics"
inpfile = open(src, 'rb')
line = inpfile.read()
summarypos = line.find(SUMMARY)
while summarypos > 0:
    ncalicon = ""
    linebreakpos = line.find(linebreak, summarypos)
    ncalicon = ncalicon + line[summarypos+8:linebreakpos].decode('utf-8')
    line = line[linebreakpos:]
    descriptionpos = line.find(DESCRIPTION)
    closingpos = line.find(ICONSUFFIX, descriptionpos)
    ncalicon = ncalicon + ":" + line[descriptionpos+14:closingpos].decode('utf-8')
    ncalicons.append(ncalicon)     
    summarypos = line.find(SUMMARY)
inpfile.close()
result = "Result.txt"
outfile = open(result, 'w')  
for i in range(len(ncalicons)):
    outfile.write(ncalicons[i] + '\r\n')
outfile.close()
key = input("Wait")
