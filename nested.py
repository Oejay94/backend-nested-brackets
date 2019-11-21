#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Oejay94 with some help from Stackoverflow, GeeksforGeeks, and Google"

import sys
openbrac = ['[', '(', '{', '(*', '<']
closedbrac = [']', ')', '}', '*)', '>']


def is_nested(line):
    stack = []
    count = 0
    matching_openbrac = ''
    while line:
        token = line[0]
        if line[:2] == '(*':
            token = '(*'
        if line[:2] == '*)':
            token = '*)'
        count += 1

        if token in openbrac:
            stack.append(token)
        if token in closedbrac:
            i = closedbrac.index(token)
            matching_openbrac = openbrac[i]
            if stack and stack.pop() != matching_openbrac:
                return count

        line = line[len(token):]

    if stack:
        return count
    return 0

def main(args):
    with open('input.txt') as f:
        with open('output.txt', 'w') as f_out:
            for line in f:
                result = is_nested(line)
                if result > 0:
                    f_out.write(f'No {result}\n')
                else:
                    f_out.write('Yes\n')

if __name__ == '__main__':
    main(sys.argv)	    
