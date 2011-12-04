#! /usr/bin/python2.7

import os
import fnmatch

from string import lower, ljust, upper

def red(string):
    return '\033[91m' + string + '\033[0m'
def green(string):
    return '\033[92m' + string + '\033[0m'

def max_checker_desc_len():
    return max([len(checker.desc) for checker in checkers])

def matches_case(file, case):
    if case == 'lower':
        return lower(file) == file
    else:
        return upper(file) == file

class NameChecker:

    errors = []
    desc = "File name check"
    config = [] # { pattern: *.java, case: 'upper' } lower camel caps

    def __init__(self, config):
        self.config = config

    def check(self, file):
        for conf in self.config:
            if fnmatch.fnmatch(file, conf['pattern']) and not matches_case(file, conf['case']):
                self.errors.append("file: " + file + "failed")

    def finished(self):
        pass

class FileExists:

    errors = []
    desc = "File exists check"
    found = False
    config = [] # { pattern: *.java }

    def __init__(self, config):
        self.config = config

    def check(self, file):
        for conf in self.config:
            if fnmatch.fnmatch(file, conf['pattern']):
                self.found = True

    def finished(self):
        if not self.found:
            self.errors.append("No file found")


checkers = [
                NameChecker([{'pattern': '*.java', 'case': 'lower'}, {'pattern': '*.txt', 'case': 'lower'}]),
                FileExists([{'pattern': '*.java'}])
           ]

# check stuff
for root, dirs, files in os.walk('/tmp'):
    for name in files:
        for checker in checkers:
            checker.check(name)
    for name in dirs:
        for checker in checkers:
            checker.check(name)

# print results
for checker in checkers:
    checker.finished()
    print ljust(checker.desc, max_checker_desc_len() + 5) + "[" + (checker.errors and red("FAILED") or green("OK")) + "]"

