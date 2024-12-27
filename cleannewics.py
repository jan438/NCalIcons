import os
import sys
from pathlib import Path

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
            
def process_organizer(line, pos):
    processed = line[:pos] + line[pos+36:]
    return processed

def process_organizers(line, pos):
    processed = line
    for i in range(len(pos), 0, -1):
        processed = process_organizer(processed, pos[i-1])
    return processed

def process_linebreak(line, pos):
    processed = line[:pos] + line[pos+3:]
    return processed

def process_linebreaks(line, pos):
    processed = line
    for i in range(len(pos), 0, -1):
        processed = process_linebreak(processed, pos[i-1])
    return processed

def process_backslash(line, pos):
    processed = line[:pos] + line[pos+1:]
    return processed

if sys.platform[0] == 'l':
    path = '/home/jan/git/NCalIcons/IconIndexes'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/NCalIcons/IconIndexes"
os.chdir(path)
src = "Ent.ics"
inpfile = open(src, 'rb')
line = inpfile.read()
BEGINVEVENT = "BEGIN:VEVENT".encode()
BEGINVALARM = "BEGIN:VALARM".encode()
ENDVALARM = "END:VALARM".encode()
SUMMARY = "SUMMARY".encode()
DESCRIPTION = "DESCRIPTION".encode()
DTSTART = "DTSTART".encode()
DTEND = "DTEND".encode()
crlf = '\r\n'.encode()
linebreak = '\r\n '.encode()
backslash = "\\".encode()
ORGANIZER = "ORGANIZER:mailto:local@newcalendar".encode()
ICONPREFIX = '[i'.encode()
organizers = find_all_occurrences(line, ORGANIZER, 0, len(line))
line = process_organizers(line, organizers)
neweventpos = line.find(BEGINVEVENT)
dtstartpos = line.find(DTSTART)
dtendpos = line.find(DTEND)
summarypos = line.find(SUMMARY)
descriptionpos = line.find(DESCRIPTION)
summaries = find_all_occurrences(line, SUMMARY, 0, len(line))
descriptions = []
icons = []
for i in range(len(summaries)):
    descriptionpos = line.find(DESCRIPTION, summaries[i])
    descriptions.append(descriptionpos)
for i in range(len(summaries)):
    linebreaks = find_all_occurrences(line, linebreak, summaries[i], descriptions[i])
    if len(linebreaks) > 0:
        line = process_linebreaks(line, linebreaks)
descriptions = find_all_occurrences(line, DESCRIPTION, 0, len(line))
for i in range(len(descriptions)):
    iconindexpos = line.find(ICONPREFIX, descriptions[i])
    icons.append(iconindexpos)
for i in range(len(descriptions)):
    linebreaks = find_all_occurrences(line, linebreak, descriptions[i], icons[i])
    if len(linebreaks) > 0:
        line = process_linebreaks(line, linebreaks)
    backslashpos = line.find(backslash)
    while backslashpos > 0:
        line = process_backslash(line, backslashpos)
        backslashpos = line.find(backslash)
inpfile.close()
print("Summaries", len(summaries), "Descriptions", len(descriptions))
key = input("Wait")
