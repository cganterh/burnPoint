#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from os import system
from sys import argv
from re import sub, findall, match
from logging import debug, info, getLogger, DEBUG

getLogger().setLevel(DEBUG)

def one_of(*res):
    return '(?:' + '|'.join(res) + ')'

BLINE = r'\n\n'
DASHES = BLINE + '\-+' + BLINE
I_HANDOUT_SEP = BLINE + '!===+' + BLINE
F_HANDOUT_SEP = BLINE + '===+!' + BLINE
TEXT = one_of('.', r'\n')
ASTERISKS = BLINE + '\*+' + BLINE
NOTE = '__' + TEXT + '+?__'
LINESTART = one_of('^', r'\n')
HEADER = LINESTART + r'#.+\n'
TITLE_BLOCK = one_of('^%'+TEXT+'*%'+TEXT+'*'+BLINE, 
                     '^---'+TEXT+'*\.\.\.')


def remove_handout(string):
    return sub(I_HANDOUT_SEP+TEXT+'*?'+F_HANDOUT_SEP, BLINE, string)
    
def remove_note_markers(string):
    return sub('__', '', string)
    
def remove_all_ulines(string):
    return sub('_', '', string)
    
def replace_strong_markers(string):
    return sub('_', '**', string)
    
def is_note(string):
    return bool(match(NOTE, string))
    
def notes_to_list_items(string):
    return '* '+string if is_note(string) else string
    
def get_notes_string(filestr):
    regexp = one_of(HEADER, NOTE, TITLE_BLOCK)
    debug('notes string regex: %s', regexp)
    lines = findall(regexp, filestr)
    lines = map(notes_to_list_items, lines)
    lines = map(remove_note_markers, lines)
    lines = map(replace_strong_markers, lines)
    return '\n'.join(lines)
    
def remove_separator(string, separator):
    return sub(separator, BLINE, string)
    
def remove_hadout_sep(string):
    return remove_separator(string,
                            one_of(I_HANDOUT_SEP, F_HANDOUT_SEP))
    
def remove_slide_sep(string):
    return remove_separator(string, ASTERISKS)
    
def remove_all_separators(string):
    debug('removing handout separators ...')
    result = remove_hadout_sep(string)
    debug('removing slide separators ...')
    result = remove_slide_sep(result)
    return result

if __name__ == "__main__":
    with open(argv[1], 'r') as f:
        filestr = f.read()
    
    with open('slides.md', 'w') as slides:
        slides.write(remove_all_ulines(remove_handout(filestr)))
    exit_status = system('pandoc -s --self-contained -t beamer -o '
                         'slides.pdf slides.md')
    
    with open('handout.md', 'w') as handout:
        result = remove_all_ulines(filestr)
        result = remove_all_separators(result)
        handout.write(result)
    system('pandoc -s --self-contained -o handout.pdf handout.md')
    
    with open('notes.md', 'w') as notes:
        notes.write(get_notes_string(filestr))
    system('pandoc -s --self-contained -o notes.pdf notes.md')
