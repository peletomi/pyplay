#! /usr/bin/python2.7

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

yamyam = load(open('test.yaml', 'r'))
print yamyam
