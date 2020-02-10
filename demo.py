import json # 認証に必要な情報を読み込むために使用

from cotohapy3 import CotohaAPI # 今回使用するライブラリ

# 各種情報の取得
with open("config.json") as f:
    d = json.load(f)

# 1. 認証
api = CotohaAPI(developer_api_base_url=d["developer_api_base_url"], access_token_publish_url=d["access_token_publish_url"])
api.login(clientid=d["clientid"], clientsecret=d["clientsecret"])

# 2. 各種APIの利用
print(api.parse("昨日母と銀座で焼き肉を食べた"))
print(api.ne("昨日は東京駅を利用した。"))
print(api.coreference("太郎は友人です。彼は焼き肉を食べた。"))
print(api.keyword("レストランで昼食を食べた。"))
print(api.similarity("近くのレストランはどこですか？", "このあたりの定食屋はどこにありますか？"))
print(api.sentence_type("あなたの名前は何ですか？"))
print(api.user_attribute("私は昨日田町駅で飲みに行ったら奥さんに怒られた。"))
print(api.remove_filler("えーーっと、あの、今日の打ち合わせでしたっけ。すみません、ちょっと、急用が入ってしまって。"))
print(api.detect_misrecognition("温泉認識は誤りを起こす"))
print(api.sentiment("人生の春を謳歌しています"))
with open("summary.txt", "r", encoding="utf-8") as f:
    document = f.read()
print(api.summary(document, 1))