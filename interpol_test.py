#! /usr/bin/python2.7

from interpol import interpol
import unittest

class TestInterpol(unittest.TestCase):

    v = {
            'this': 'foo',
            'that': 'bar'
            }

    def test_stringWithOneValue(self):
        self.assertEqual('foo bar', interpol(self.v, '%this bar'))

    def test_stringWithTwoValues(self):
        self.assertEqual('foo bar', interpol(self.v, '%this %that'))

    def test_stringWithEmbeddedValue(self):
        self.assertEqual('foobar', interpol(self.v, '%{this}bar'))

    def test_stringWithTwoEmbeddedValues(self):
        self.assertEqual('foobar', interpol(self.v, '%{this}%{that}'))

    def test_stringSubstringFrom(self):
        self.assertEqual('o bar', interpol(self.v, '%this:2 bar'))
        self.assertEqual('o bar', interpol(self.v, '%{this:2} bar'))

    def test_stringEmbeddedSubstringFrom(self):
        self.assertEqual('obar', interpol(self.v, '%this:2bar'))
        self.assertEqual('obar', interpol(self.v, '%{this:2}bar'))
