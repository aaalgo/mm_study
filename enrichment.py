#!/usr/bin/env python3
import subprocess as sp
from chart import create_chart

sp.call('mkdir -p html/enrichment', shell=True)

def load_list (path, sort=True):
    v = []
    with open(path, 'r') as f:
        for l in f:
            k, s = l.strip().split('\t')
            s = float(s)
            v.append((k,s))
            pass
        pass
    if sort:
        v.sort(key=lambda x: x[1])
    return v


bl = load_list('data/aucs/bl')
enlarged = load_list('data/aucs/enlarged_prior')
#hovon = load_list('auc/17984')

tests = [
         #(lambda x: x>0.99, [], "AUC > 0.99", 'th99'),
         (lambda x: x>0.98, [], "AUC > 0.98", 'th98'),
         (lambda x: x>0.95, [], "AUC > 0.95", 'th95'),
         (lambda x: x>0.90, [], "AUC > 0.90", 'th90'),
         (lambda x: x<0.15, [], "AUC < 0.15", 'th15'),
         (lambda x: x<0.1, [], "AUC < 0.10", 'th10'),
         #(lambda x: x<0.05, [], "AUC < 0.10", 'th10')
]

annot = "GOTERM_BP_FAT,GOTERM_CC_FAT,GOTERM_MF_FAT,INTERPRO,PIR_SUPERFAMILY,SMART,BBID,BIOCARTA,KEGG_PATHWAY,COG_ONTOLOGY,SP_PIR_KEYWORDS,UP_SEQ_FEATURE,GENETIC_ASSOCIATION_DB_DISEASE,OMIM_DISEASE"

with open('html/enrichment/b1.html', 'w') as f1, \
     open('html/enrichment/b2.html', 'w') as f2, \
     open('html/enrichment/b1b2.html', 'w') as f1f2:
    f1.write('<html><body>\n')
    f2.write('<html><body>\n')
    f1f2.write('<html><body>\n')

    for test, _, text, tag in tests:

        bl99 = [k for k, s in bl if test(s)]
        enlarged99 = [k for k, s in enlarged if test(s)]

        bl_enlarged = set(bl99) & set(enlarged99)
        print(len(bl99), len(enlarged99), len(bl_enlarged))

        create_chart(bl99, 'html/enrichment/chart.b1.%s' % tag)
        create_chart(enlarged99, 'html/enrichment/chart.b2.%s' % tag)
        create_chart(bl_enlarged, 'html/enrichment/chart.b1b2.%s' % tag)
        f1.write('<a href="http://david.abcc.ncifcrf.gov/api.jsp?type=%s&ids=%s&tool=chartReport&annot=%s" target="_blank">%s, %d genes</a><br/>\n' % ("AFFYMETRIX_3PRIME_IVT_ID", ','.join(list(bl99)), annot, text, len(bl99)))
        f2.write('<a href="http://david.abcc.ncifcrf.gov/api.jsp?type=%s&ids=%s&tool=chartReport&annot=%s" target="_blank">%s, %d genes</a><br/>\n' % ("AFFYMETRIX_3PRIME_IVT_ID", ','.join(list(enlarged99)), annot, text, len(enlarged99)))
        f1f2.write('<a href="http://david.abcc.ncifcrf.gov/api.jsp?type=%s&ids=%s&tool=chartReport&annot=%s" target="_blank">%s, %d genes</a><br/>\n' % ("AFFYMETRIX_3PRIME_IVT_ID", ','.join(list(bl_enlarged)), annot, text, len(bl_enlarged)))
        pass
    f1.write('</body></html>\n')
    f2.write('</body></html>\n')
    f1f2.write('</body></html>\n')
