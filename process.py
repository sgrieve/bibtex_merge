import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
import re

# This is the thesis references, with the month values wrapped
# in braces to stop bibtexparser complaining
with open('References_clean.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# This is the new project
with open('/Users/stuart/Papers/repro_of_topo_analysis/refs.bib') as bibtex_file:
    bib_database2 = bibtexparser.load(bibtex_file)

# Add the two lists of dictionaries together
refs = bib_database.entries + bib_database2.entries

# Load the text of the new project to find all the citation ids
with open('/Users/stuart/Papers/repro_of_topo_analysis/chapter.tex') as f:
    lines = f.read()

# returns a list of all the citation ids
tags = (re.findall(r'(?:\\cite[pt]+?\[?e?\.?g?\.?,?\]?\[?\]?{)([\w\-_\d,\s]+)',
                   lines))

# split out multiple citations from one \cite tag
ids = []
for t in tags:
    if ',' in t:
        t = t.replace(' ', '').split(',')
        for i in t:
            ids.append(i)
    else:
        ids.append(t)

# Grab the bib entries for every id in the tex file
book_refs = []
for ref in refs:
    if ref['ID'] in ids:
        book_refs.append(ref)

# Build a new BibDatabase as we need this object for writing
output = BibDatabase()
output.entries = book_refs

# Overwrite the input bibtex file with the complete set of entries
with open('/Users/stuart/Papers/repro_of_topo_analysis/refs.bib', 'w') as bibtex_file:
    bibtexparser.dump(output, bibtex_file)
