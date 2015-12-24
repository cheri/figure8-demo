'''
  This file is part of a simple example of how the FIGURE8 system works.
  https://github.com/cheri/FIGURE8-demo

  Copyright (c) 2015 Sarah Harmon
    This source code is free to use under the GNU General Public License (GPL) with author attribution.

  FUNCTION
  This file provides an example of a basic test of coherence.  The main FIGURE8 demo system can call
  this file to determine whether creative constructions have been used before.

  This example uses Python's urllib module to query the number of Google results that exist for
  "[NOUN] [VERB]", where [NOUN] and [VERB] are input parameters.

  The system can then reason about the coherence (and novelty) of the paired words based on the
  number of Google results.

  Example, which can be replicated with the main function:
    "[TURTLE] [DARKENED]" returns 28 results (in 2015).
    "[TURTLE] [DREAMED]" returns 858 results (in 2015).

    Thus, our system may reason that turtles are more likely to dream than they are to darken.

  More complex queries may make use of advanced Google-fu (such as the use of the AROUND() operator).

'''

import urllib2
from urllib2 import Request
from bs4 import BeautifulSoup

def test_coherence(noun,verb):
  try:
    # Form our Google query.
    url = 'https://www.google.com/search?q="' + noun + "+"+ verb + '"&hl=en'

    # Provide a header so Google will allow us to use their website to search.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    # Perform the query.
    req = urllib2.Request(url, headers = headers)
    resp = urllib2.urlopen(req)
    source = resp.read()

    # Use Beautiful Soup (http://www.crummy.com/software/BeautifulSoup/)
    # to find the result statistics for us.
    soup = BeautifulSoup(source, "html.parser")
    stats = soup.find('div',{'id':'resultStats'}).text

    # We only want the number associated with the number of Google results.
    start = 'About '
    end = ' results'
    return int(stats[stats.find(start)+len(start):stats.rfind(end)].replace(',',''))

  except Exception as e:
    print("Simple coherence test failed: " +  str(e))
    return -1

def main():
  print '"turtle darkened" returns ' + str(test_coherence("turtle","darkened")) + ' results.'
  print '"turtle dreamed" returns ' + str(test_coherence("turtle","dreamed")) + ' results.'

if __name__ == '__main__':
  main()
