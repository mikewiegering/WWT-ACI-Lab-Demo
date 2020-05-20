#! /user/bin/env python

import requests

tenant = 'bdtest'

s = requests.session()

# step 1 is to authenticate to APIC and get a token

url = "https://192.168.2.149/api/aaaLogin.json"

payload = "{\r\n\t\"aaaUser\":{\r\n\t\t\"attributes\":{\r\n\t\t\t\"name\": \"admin\",\r\n\t\t\t\"pwd\":\"WWTwwt1!\"\r\n\t\t}\r\n\t}\r\n}"
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'APIC-cookie=SqZoiBkQydWCRYnFcfVyQJbwok82kX8Akeskur4Wl8d24xzz4alAPIqbqpVOhVX/zLc/3d7elmB6Es+92g9uwvmLAjZgV9aB6wo4BwwSIt2+9aVkNURjNPJzi+Vti4QpeDhO+Wp9cICYjpBJ6FgKYkX26a4As/KgVa4DUaogGZ4MGKgBzPeAoZCddVXOJXdt'
}

response = s.request("POST", url, headers=headers, data = payload, verify = False)

print(response.text.encode('utf8'))


# Step 2 create a new tenant

url = "https://192.168.2.149/api/node/mo/uni/tn-%s.json" % (tenant)

payload = "{\n    \"fvTenant\": {\n        \"attributes\": {\n            \"dn\": \"uni/tn-%s\",\n            \"name\": \"%s\",\n            \"rn\": \"tn-%s\",\n            \"status\": \"created\"\n        },\n        \"children\": []\n    }\n}" % (tenant, tenant, tenant)
headers = {
  'Content-Type': 'application/json',
  
}

response = s.request("POST", url, headers=headers, data = payload, verify = False)

print(response.text.encode('utf8'))
