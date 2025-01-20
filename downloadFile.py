import requests
import re

def getFilename(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


url = 'https://example-files.online-convert.com/document/txt/example.txt'
r = requests.get(url, allow_redirects=True)
filename = getFilename(r.headers.get('content-disposition'))
open("downloaded.txt", 'wb').write(r.content)
