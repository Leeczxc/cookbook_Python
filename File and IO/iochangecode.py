import io
import sys
import urllib.request
import operator

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
print(text)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')