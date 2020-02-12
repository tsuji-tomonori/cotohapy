import json

from cotohapy3 import CotohaAPI

# load config
with open("config.json") as f:
    d = json.load(f)

# auth
api = CotohaAPI(
    developer_api_base_url=d["developer_api_base_url"], 
    access_token_publish_url=d["access_token_publish_url"]
)
api.login(clientid=d["clientid"], clientsecret=d["clientsecret"])

document = input()
print(api.summary(document, 3))