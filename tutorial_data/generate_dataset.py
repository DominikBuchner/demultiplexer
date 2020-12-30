import gzip
from Bio.SeqIO.QualityIO import FastqGeneralIterator
from pathlib import Path
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import shutil
import random

## define a seq template to fill with data
def record_gen(name, seq_letter, primer):

    record = SeqRecord(
        Seq('{}{}'.format(primer, seq_letter * (250 - len(primer)))),
        id = name,
        name = name,
        description = 'demultiplexing dummy',
        letter_annotations = {'phred_quality': [40] * 250}
    )

    return record

tag_pairs = [('CTGT', 'GTCCTA'), ('TCTCA', 'GAACA'), ('AGCTA', 'CACCT'), ('GTCCTA', 'CTGT')]

seqs = []

## generate the 8 sequences needed for demultiplexing
for primer, letter, tag_pair in zip([1, 5, 6, 9], 'ACGT', tag_pairs):
    seqs.append(record_gen('{}_f'.format(primer), letter, tag_pair[0]))
    seqs.append(record_gen('{}_r'.format(primer), letter, tag_pair[1]))

## possible sequence combinations to choose from
choices = [(0, 1), (2, 3), (4, 5), (6, 7)]

## write the output files
for file_name in range(1, 11):
    ## select 100k random sequences
    choices = [random.choice(choices) for i in range(100000)]

    ## compute a generator for each the forward and reverse reads
    fwd = (seqs[j[0]] for j in choices)
    rev = (seqs[j[1]] for j in choices)

    ## write the output
    for read, dir in zip([1, 2], [fwd, rev]):
        with gzip.open('{}_r{}.fastq.gz'.format(file_name, read), 'wt') as output:
            SeqIO.write(dir, output, 'fastq')
