import requests
import hashlib 
import re

#GET para obter a String
url = 'http://docker.hackthebox.eu:32071'
r=requests.session()

#Regex para obter a String de Retorno
out=r.get(url)
out=re.search("<h3 align='center'>+.*?</h3>",out.text)
out=re.search("'>.*<",out[0])
out=re.search("[^|'|>|<]...................",out[0])

#Encoded para MD5
out=hashlib.md5(out[0].encode('utf-8')).hexdigest()

#Post com MD5
send = r.post(
    url,
    data = {
        "hash": out
    }
)
print(send.content)
