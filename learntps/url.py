import urllib2
import requests
import wget

response = urllib2.urlopen("http://google.de")
page_source = response.read()
print page_source


url='http://google.de'
cd = { 'sessionid': '123..'}

r = requests.get(url, cookies=cd)
print r.content


url = 'https://www.decalage.info/files/HTML.py-0.04.zip'
filename = wget.download(url)