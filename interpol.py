#! /usr/bin/python2.7

import re

def _interpol_str(var, string):
    for k, v in var.iteritems():
        string = re.sub('%\{?' + k + '\}?', v, string)
    return string

def _interpol_set(var, st):
    r = set()
    for s in st:
        r.add(interpol(var, s))
    return r

def _interpol_dct(var, dct):
    for k, v in dct.iteritems():
        dct[k] = interpol(var, v)
    return dct

def _interpol_lst(var, lst):
    for i in range(len(lst)):
        lst[i] = interpol(var, lst[i])
    return lst

def interpol(var,v):
    """Interpolates variables in ``var`` into value ``v``. The following forms are substituted:

       * %identifier
       * %{identifier} - for embedding in strings
       * %identifier:2 - from second character on
    """
    m = { dict: _interpol_dct,
          list: _interpol_lst,
          set: _interpol_set,
          str: _interpol_str }
    t = type(v)
    if m[t]:
        return m[type(v)](var, v);
    else:
        return v
