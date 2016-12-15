#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize

text = "Demography is the statistical study of populations, \
especially human beings. As a very general science, it can analyse any kind \
of dynamic living population, i.e., one that changes over time or space \
(see population dynamics). Demography encompasses the study of the size, \
structure, and distribution of these populations, and spatial or temporal \
changes in them in response to birth, migration, ageing, and death. Based \
on the demographic research of the earth, earth's population up to the year \
2050 and 2100 can be estimated by demographers. Demographics are quantifiable \
characteristics of a given population. Demographic analysis can cover whole \
societies or groups defined by criteria such as education, nationality, \
religion, and ethnicity. Educational institutions usually treat demography \
as a field of sociology, though there are a number of independent demography \
departments. Formal demography limits its object of study to the measurement \
of population processes, while the broader field of social demography or \
population studies also analyses the relationships between economic, social, \
cultural, and biological processes influencing a population. "

print 'Input text:'
print text
print 'Summary:'
print summarize(text)
print summarize(text, split=True)
print '\n\n\n'
print 'Summary2------------------------------:'
print summarize(text, ratio=0.5)
print '\n\n\n'
print 'Summary3------------------------------:'
print summarize(text, word_count=50)
from gensim.summarization import keywords

print 'Keywords:'
print keywords(text)