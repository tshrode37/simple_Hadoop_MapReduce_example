#!/usr/bin/env python
import sys
import string
from sklearn.feature_extraction import stop_words

stopwords = set(stop_words.ENGLISH_STOP_WORDS)
# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    punct = line.translate(string.maketrans("",""), string.punctuation)

    # split the line into words; splits on any whitespace

    words = punct.split()
    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stopwords:
           print '%s\t%s' % (word, "1")
