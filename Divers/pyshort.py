# Comment raccourcir une url avec python ?

# dans une console, s'utilise de cette façon :
# python pyshort.py http://www.monsite.com

import sys

# cette librairie s'intalle avec "pip install pyshorteners" dans la console
import pyshorteners

url = pyshorteners.Shortener()
print(url.tinyurl.short(sys.argv[1]))