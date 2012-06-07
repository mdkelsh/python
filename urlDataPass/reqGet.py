import urllib2
import urllib
import re
import os
import sys

global url_data
global read_data

def main():
  getter = raw_input('')  
  if not getter:
    parser(read_data)
    url_getter(url_found)
  else:
    url_data = getter
    url_getter(url_data)  

def url_getter(passed_url):
  url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' 
  req = urllib2.Request(url, data=passed_url)
  response = urllib2.urlopen(req)
  read_data = response.read()


def parser(parse_data):
  found = re.compile('\d+')
  url_found = found.search(parse_data)
  return url_found
  
  
  
if __name__ == "__main__":
  while 1:
    main()

  
