import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
import re

with open('References_clean.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

with open('/Users/stuart/Papers/repro_of_topo_analysis/refs.bib') as bibtex_file:
    bib_database2 = bibtexparser.load(bibtex_file)

refs = bib_database.entries + bib_database2.entries

with open('/Users/stuart/Papers/repro_of_topo_analysis/chapter.tex') as f:
    lines = f.read()

tags = (re.findall(r'(?:\\cite[pt]+?\[?e?\.?g?\.?,?\]?\[?\]?{)([\w\-_\d,\s]+)',
                   lines))

ids = []
for t in tags:
    if ',' in t:
        t = t.replace(' ', '').split(',')
        for i in t:
            ids.append(i)
    else:
        ids.append(t)

book_refs = []


for ref in refs:
    if ref['ID'] in ids:
        book_refs.append(ref)

output = BibDatabase()
output.entries = book_refs

with open('/Users/stuart/Papers/repro_of_topo_analysis/refs.bib', 'w') as bibtex_file:
    bibtexparser.dump(output, bibtex_file)
