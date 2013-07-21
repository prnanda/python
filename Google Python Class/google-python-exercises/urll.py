## Version that uses try/except to print an error message if the
## urlopen() fails.
import urllib

def wget2(url):
  try:
    ufile = urllib.urlopen(url)
    if ufile.info().gettype() == 'text/html':
      print ufile.read()
  except IOError:
    print 'problem reading url:', url

wget2('http://www.google.com')