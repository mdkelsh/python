import urllib2
import urllib
import re
import os
import sys




def main():
  while 1: 
    global url_found
    url_found = ['6711']
    if url_found:
      parser()
      url_getter()
  
    else:
      getter = raw_input('What is the data you want?: ')  
    try:
      global url_data
      url_data = getter
      url_getter()  
    except:
      sys.exit()


def url_getter():
  url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' 
  req = urllib2.Request(url, data=parsed_data)
  response = urllib2.urlopen(req)
  global read_data
  read_data = ['']
  read_data.append(response.read())
  print read_data

def parser():
  global parsed_data
  found = re.compile('\d+')
  url_found.append(found.findall(read_data[-1]))
  parsed_data = url_found[-1]    
  
  
  
if __name__ == "__main__":
  main()

  
