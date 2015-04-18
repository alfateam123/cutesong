import requests
#import ListResponse

def list():
  return requests.get("http://openings.moe/api/list.php").json()

def filenames():
  return requests.get("http://openings.moe/api/list.php?filenames").json()
