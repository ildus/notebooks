#!/usr/bin/env python
#coding: utf-8

import sys

occurrences = {}
words = open(sys.argv[1], 'r').read()
for word in words.split():
	occurrences[word]=occurrences.get(word,0)+1

for word in sorted(occurrences):
	count = occurrences[word]
	if count > 1 and not word[0].isdigit():
		print("{0} - {1}".format(word, count))
