import gzip

from toolz import take

with gzip.open('data/01-nobelprize-data.nt.gz', 'rt') as f:
    for line in take(100, f):
        print(line)