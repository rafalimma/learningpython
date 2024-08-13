import requests

# http:// -> 80
# https:// ->443
url = 'http://localhost:3333/'
response = requests.get(url)

print(response)