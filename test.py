import requests

url = 'https://api.twinword.com/api/topic/generate/latest/'
text = 'imac sale in 2011\nmacs sale in 2011\nimac 2011'
myobj = {'text': text}

x = requests.post(url, data=myobj)

print(x.text)