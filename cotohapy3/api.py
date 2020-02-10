import json

import requests

from .utils import CotohaError

class BaseAPI:
    def __init__(self, developer_api_base_url, access_token_publish_url):
        self.developer_api_base_url = developer_api_base_url
        self.access_token_publish_url = access_token_publish_url
        self.requests = requests.Session()

    def requests_call(self, method, url, headers={}, params=None, data=None, stream=False, requests_kwargs=None):
        try:
            if (method == 'GET'):
                return self.requests.get(url, params=params, headers=headers, stream=stream)
            elif (method == 'POST'):
                return self.requests.post(url, params=params, data=data, headers=headers, stream=stream)
        except Exception as e:
            raise CotohaError(f"requests {method} {url} error: {e}")
        
        raise CotohaError(f"Unknown method: {method}")

    def require_auth(self):
        if self.access_token is None:
            raise CotohaError('Authentication required! Call login() first!')

    def get_result(self, r):
        return json.loads(r.text)

    def login(self, clientid, clientsecret):
        return self.auth(clientid, clientsecret)

    def auth(self, clientid, clientsecret):
        url = self.access_token_publish_url
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "grantType": "client_credentials",
            "clientId": clientid,
            "clientSecret": clientsecret
        }
        data = json.dumps(data).encode()
        r = self.requests_call("POST", url, headers=headers, data=data)
        
        if (r.status_code not in [200, 201]):
            raise CotohaError(f"[ERROR] auth() failed! check client Id or client Secret.\nHTTP {r.status_code}: {r.text}")

        token = None
        try:
            token = self.get_result(r)
            self.access_token = token["access_token"]
            self.expires_in = token["expires_in"]
            self.issued_at = token["issued_at"]
        except:
            raise CotohaError(f"Get access_token error! Response: {r.headers}, {r.text}")

        return token