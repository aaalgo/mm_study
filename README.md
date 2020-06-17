
Python requirements are in requirements.txt

# 1. Glossary

- probeset
- go term
- gene: one gene has multiple probe sets, and multiple go terms.  Probe sets and go terms are related by genes.
- microarray: a large number of probesets for evaluating the expression level of genes.
- HG-U133_Plus_2: the microarray model we use in this study.
- CEL file: raw microarray data
- MAS5: summarized and normalized microarray data.

TOTAL number of genes: 54675

# 2. Data

If you have obtained mm_data.tar.bz2, goto the directory mm_study and
run
```
tar xf mm_data.tar.bz2
```
After that, you should have 'data' and 'meta' under mm_study.

## 2.1 Microarray data [ONLY RUN IF YOU HAVE MAS5 FILES]

Background: bg
Foreground: GSE19784, GSE24080, uams/{bl, mel, vel}

UAMS:

- bl: baseline
- mel, vel: after drug treatments.

## 2.2 Meta files (Provided separately)

- meta/goa_human.gaf: gene to go term mapping.
- meta/HG-U133_Plus_2.na36.annot.csv : probeset to gene mapping.
- meta/ref: list of all genes (any MAS5 file containing all the genes.)
- meta/gencode.v19.annotation.gtf

## 2.3 Preprocessing (MUST RUN)

### Generating probeset to gene mapping
```
MM.py
```
Produces data/gene_id.pkl.

### Chromosome information generation
```
./chrome.py
```
Generates chromes.pkl which is (chromes, lookup).  Lookup maps gene name
to (chrome, start, end, strand).

### Find probesets of interest
```
./ps_of_interest.py > data/interest
```
The list of genes of interest is hard-coded in the code. Modify the
code.  The script prints the probesets associated with these genes.

### Raw data to MAS conversion (DO NOT RUN)

One should not need to run this as only MAS files are provided.
These files provide a means to convert the raw CEL microarrays to MAS5
files.

- mas5.sh
- mas5.R

This step requires all the raw data to run.  The user is not expected to
have the data so skip this step.


## 2.4 Pre-generated data

- data/aucs/bl	: baselevel ranking
- data/ranks/   : interesting probesets ranking & images


# 3. MAS5 Operations [ONLY RUN IF YOU HAVE MAS5 FILES]

The intermediate results of these steps are provided in mm_data.tar.bz2.
Do not run these steps.


## 3.1 Build

These C++ files need to be built.  On ubuntu 18.04, install g++ and boost with
```
apt-get install -y g++ libboost-all-dev
```

Then type make to build the executable binaries.
```
make
```

## 3.2 import [ONLY IF YOU HAVE MAS FILES]

```
find xxx/ -type f | ./import -o yyy
```

Input is a list of paths to MAS5 files.  Assume:
- number of files is M
- number of genes is N (54675)
This will generate 3 files:

- yyy.idx: 
- yyy.expr: numpy array of M * N, dtype = float.  Gene expression level.
- yyy.rank: numpy array of M * N, dtype = uint16.  Gene expression rank.


Ranking is ascending order, highly expressed genes have large rank numbers.  Ranking can be considered a kind of normalization of expression levels.


For basic experiments we generate two sets:

```
find mas5/bg -type f | ./import -o bg			# background
find mas5/uams/bl -type f | ./import -o bl		# baselevel
```


## 3.3 compare [ONLY IF YOU HAVE MAS FILES]

```
Compare bg.npy bl.npy
```

compare the two sets and generate AUC score for each gene in the second set.  Generate an AUC value for each gene.


4. Other Scripts [TRY THESE OUT]

These operations rely on pre-computed results in the data directory.

4.1. Draw Chromosome

```
./draw_chromosome.py
./stat_chromosome.py
```


4.2 Draw ranking images

```
./draw_ranks.py
```

4.3 Enrichment Study

```
./enrichment.py
```

This generates html/enrichment.

Generate wordcloud after the above step:

```
./wc.py
```














