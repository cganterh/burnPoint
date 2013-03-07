#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from os import system
from sys import argv
from re import sub, findall

def remove_handout(string):
    return sub('\n\n\-+\n\n(?:.|\n)*\n\n\*+\n\n', '\n\n'+'-'*10+'\n\n', string)
    
def remove_note_markers(string):
    return sub('__', '', string)
    
def remove_all_ulines(string):
    return sub('_', '', string)
    
def replace_strong_markers(string):
    return sub('_', '**', string)
    
def get_notes_string(string):
    lines = findall('(?:(?:^|\n)#.+\n|__(?:.|\n)+?__)', filestr)
    lines = map(lambda line: '* '+line if line[0]=='_' else line, lines)
    lines = map(remove_note_markers, lines)
    lines = map(replace_strong_markers, lines)
    return '\n'.join(lines)
    
def remove_hadout_sep(string):
    return sub('\n\n\-+\n\n', '\n\n', string)

if __name__ == "__main__":
    with open(argv[1], 'r') as f:
        filestr = f.read()
    
    with open('slides.md', 'w') as slides:
        slides.write(remove_all_ulines(remove_handout(filestr)))
    system('pandoc -s --self-contained -t beamer -o slides.pdf slides.md')
    
    with open('handout.md', 'w') as slides:
        slides.write(remove_hadout_sep(remove_all_ulines(filestr)))
    system('pandoc -s --self-contained -t beamer -o handout.pdf handout.md')
    
    with open('notes.md', 'w') as slides:
        slides.write(get_notes_string(filestr))
    system('pandoc -s --self-contained -t beamer -o notes.pdf notes.md')
