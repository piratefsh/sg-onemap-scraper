# quick and dirty scraper to get images from http://hm.onemap.sg/
# requires requests module

import requests
import os

def get_image(url, filename):
  r = requests.get(url)

  if r.status_code == 200:
    # make folder
    dirname = "%d" % year
    if not os.path.exists(dirname):
      os.makedirs(dirname)

    with open("%s/%s" % (dirname, filename), 'wb') as fd:
      for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

    return True

  return False

for year in range(1958, 2018):
  url = 'http://hm.onemap.sg/%d/%d (indexmap).jpg' % (year, year)
  filename = "./_%d-fullmap.png" % year
  found = get_image(url, filename)

  if found:
    # get subsection
    for section in range(290, 300):
      subsection_url = "http://hm.onemap.sg/%d/%d (%d).jpg" % (year, year, section)
      subsection_filename = "%d-%d.png" % (year, section)
      get_image(subsection_url, subsection_filename)


