#! /usr/bin/python2.7

import os
import fnmatch

from string import lower, ljust

def red(string):
    return '\033[91m' + string + '\033[0m'
def green(string):
    return '\033[92m' + string + '\033[0m'

def max_checker_desc_len():
    return max([len(checker.desc) for checker in checkers])

class NameChecker:

    errors = []
    desc = "File name check"

    def check(self, file):
        if lower(file) != file:
            self.errors.append("file: " + file + "failed")

    def finished(self):
        pass

class FileExists:

    errors = []
    desc = "File exists check"
    found = False

    def check(self, file):
        if fnmatch.fnmatch(file, '*.conf'):
            self.found = True

    def finished(self):
        if not self.found:
            self.errors.append("No file found")


checkers = [NameChecker(), FileExists()]

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

