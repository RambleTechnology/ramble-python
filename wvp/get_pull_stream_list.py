import http.client
import requests
import json


token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjNlNzk2NDZjNGRiYzQwODM4M2E5ZWVkMDlmMmI4NWFlIn0.eyJqdGkiOiJqTGdJd3NMb3RfclNlQ3g0T0YxUHhBIiwiaWF0IjoxNzQ1NzQ0MjIxLCJleHAiOjE3NDU3NDYwMjEsIm5iZiI6MTc0NTc0NDIyMSwic3ViIjoibG9naW4iLCJhdWQiOiJBdWRpZW5jZSIsInVzZXJOYW1lIjoiYWRtaW4ifQ.WsTwbuOaMYdQ9RPYM61AjXUKW_jXFUXj8k3_LZr0u4o-IKEtoRYRTVdWCv-LmQBEKuP6qG3jqW2QMjheRpDvhvsp8ojlgIoRAwmAX23f4G1PkEw9jxBJPCON5VSYRQS3ouH85ruQc1gzpCt0N9r7p1Rtv_afjckpthiwbzyopFp8OBV8Cf5mHJVyvDfeQhqJ8hb_zCqUBdte04JTyaZ5-BhFp1A7OTMDOvisr9nBNyw2NMw2LWdcgsP2serA45fvMzFZDekjOQL3xPuYgASAivEnUibXyx9u1nHkXAm9wTCuIoaPNTMtAz_tPuE6RPEYqMu5E2My-N8vT8WRpFgyUw"

url_prefix = ""

conn = http.client.HTTPSConnection(url_prefix)


def login():
    url = "http://192.168.1.23:18080/api/user/login"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
    }
    params = {"username": "admin", "password": "21232f297a57a5a743894a0e4a801fc3"}
    response = requests.get(url, headers=headers, params=params)
    j =json.loads(response.text)
    print(f"响应体={j}")
    return j["data"]["accessToken"]
    


def get_pull_stream_list():
    url = "http://192.168.1.23:18080/api/proxy/list"
    headers = {
        "access-token": token,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
    }
    params = {"page": 0, "count": 99, "query": "", "pulling": "", "mediaServerId": ""}
    response = requests.get(url, headers=headers, params=params)
    print(response.text)


if __name__ == "__main__":
    accessToken=login()
    print(f"登录成功，获取到的token={token}")
    token=accessToken
    get_pull_stream_list()
