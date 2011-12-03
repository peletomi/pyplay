#! /usr/bin/python2.7

import os
import fnmatch
import argparse

def red(string):
    return '\033[91m' + string + '\033[0m'
def green(string):
    return '\033[92m' + string + '\033[0m'
def yellow(string):
    return '\033[93m' + string + '\033[0m'
def blue(string):
    return '\033[94m' + string + '\033[0m'
def magenta(string):
    return '\033[95m' + string + '\033[0m'
def cyan(string):
    return '\033[96m' + string + '\033[0m'
def white(string):
    return '\033[97m' + string + '\033[0m'
def bold(string):
    return '\033[1m' + string + '\033[0m'

parser = argparse.ArgumentParser(description='Prints out files and directories matching glob expression.')
parser.add_argument('directory', metavar='D', nargs='?', default='.', help='directory to process, defaults to .')
parser.add_argument('glob', metavar='G', nargs='?', default='*', help='glob expression, defaults to *')
args = parser.parse_args()

for root, dirs, files in os.walk(args.directory):
    for name in files:
        if fnmatch.fnmatch(name, args.glob):
            print magenta(name)
    for name in dirs:
        if fnmatch.fnmatch(name, args.glob):
            print yellow(name)
