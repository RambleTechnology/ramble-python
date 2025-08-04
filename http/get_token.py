import http.client

conn = http.client.HTTPConnection("127.0.0.1", 8086)
payload = ''
headers = {
   'token': 'fe4970d8-3a01-4229-9394-c9ce596f4e37',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': '127.0.0.1:8086',
   'Connection': 'keep-alive'
}
conn.request("GET", "/testTask/test1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))