#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.summarization import keywords
from gensim.summarization import summarize

def resumeFunction(text):
	return (summarize(text, word_count=50))

#print ('Keywords:')
#print (keywords(text))

print("\n\n\n\n")
texto = input("Insert text here: \n")
print(resumeFunction(texto))
