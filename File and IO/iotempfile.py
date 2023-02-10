from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('dsajd')
    f.write('dsadsa')

    f.seek(0)
    data = f.read()