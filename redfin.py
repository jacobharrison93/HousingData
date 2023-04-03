import requests

payload = {'username':'jacob', 'password':'testing'}
url_comic = 'http://httpbin.org/post'
request = requests.post(url_comic,data=payload)

r_dict = request.json()
print(r_dict['form'])

