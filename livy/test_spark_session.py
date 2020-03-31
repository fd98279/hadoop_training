import json, pprint, requests, textwrap
host = 'http://sandbox-hdp.hortonworks.com:8999'
data = {'kind': 'spark'}
headers = {'Content-Type': 'application/json'}
headers = {'X-Requested-By': 'root'}
r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)
print(r.content)
