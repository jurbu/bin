#!/usr/bin/python

from urllib import quote
from sys import argv

if argv[1]:
  print quote(argv[1],'/:')