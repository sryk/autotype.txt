import urllib as dw

class autotype:
  data = {}
  # Code for the autotype interpreter.
  def __init__(weblist):
    data.files = weblist
    
  def parse(weblist):
    data = {}
    for w in data.files:
      attxt = dw.urlopen(w + "/autotype.txt")
      attxt = a.open().split("'")
      # data = {}
      for i=1, len(attxt):
        if attxt[i] == "siteName":
          data.siteName = attxt[i+1]
          i+=1
        elif attxt[i] == "siteGenre":
          data.siteGenre = attxt[i+1]
          i+=1
        elif attxt[i] == "keyWords":
          data.keywords = attxt[i+1].split(",")
          i+=1
        elif attxt[i] == "siteInclude":
          data.includedFiles = attxt[i+1].split('@')
          i+=1
