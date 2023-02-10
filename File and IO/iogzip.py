import bz2
import gzip

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()


# 指定压缩等级
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

