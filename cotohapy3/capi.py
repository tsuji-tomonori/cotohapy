import time
import json

from .api import BaseAPI
from .utils import CotohaError

class CotohaAPI(BaseAPI):
    def __init__(self, developer_api_base_url, access_token_publish_url):
        super().__init__(developer_api_base_url, access_token_publish_url)

    def auth_requests_call(self, method, url, headers={}, params=None, data=None, stream=False, requests_kwargs=None):
        self.require_auth()
        if(int(self.expires_in)*1000 + int(self.issued_at)) < int(time.time()*1000):
            raise CotohaError("Access token has expired. Please login again")
        r = self.requests_call(method, url, headers=headers, params=params, data=data, stream=stream, requests_kwargs=requests_kwargs)
        r.encoding = "utf-8"
        return r

    # 構文解析
    def parse(self, sentence, **kwargs):
        url = self.developer_api_base_url + "nlp/v1/parse"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "sentence": sentence
        }
        data.update(kwargs)
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)

    # 固有表現抽出
    def ne(self, sentence, **kwargs):
        url = self.developer_api_base_url + "nlp/v1/ne"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "sentence": sentence
        }
        data.update(kwargs)
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)

    # 照応解析
    def coreference(self, document, **kwargs):
        url = self.developer_api_base_url + "nlp/v1/coreference"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "document": document
        }
        data.update(kwargs)
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)

    # キーワード抽出
    def keyword(self, document, **kwargs):
        url = self.developer_api_base_url + "nlp/v1/keyword"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "document": document
        }
        data.update(kwargs)
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)

    # 類似度計算
    def similarity(self, s1, s2, **kwargs):
        url = self.developer_api_base_url + "nlp/v1/similarity"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "s1": s1,
            "s2": s2
        }
        data.update(kwargs)
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)

    # 文タイプ判定
    def sentence_type(self, sentence, **kwargs):
        url = self.developer_api_base_url + "nlp/v1/sentence_type"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "sentence": sentence
        }
        data.update(kwargs)
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)

    # ユーザー属性推定(β)
    def user_attribute(self, document, **kwargs):
        url = self.developer_api_base_url + "nlp/beta/user_attribute"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "document": document
        }
        data.update(kwargs)
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)

    # 言い淀み除去(β)
    def remove_filler(self, text, **kwargs):
        url = self.developer_api_base_url + "nlp/beta/remove_filler"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "text": text
        }
        data.update(kwargs)
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)

    # 音声認識誤り検知(β)
    def detect_misrecognition(self, sentence, **kwargs):
        url = self.developer_api_base_url + "nlp/beta/detect_misrecognition"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "sentence": sentence
        }
        data.update(kwargs)
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)

    # 感情分析
    def sentiment(self, sentence):
        url = self.developer_api_base_url + "nlp/v1/sentiment"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "sentence": sentence
        }
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)

    # 要約(β)
    def summary(self, document, sent_len, **kwargs):
        url = self.developer_api_base_url + "nlp/beta/summary"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "document": document,
            "sent_len": sent_len
        }
        data = json.dumps(data).encode()
        r = self.auth_requests_call("POST", url, headers=headers, data=data)
        return self.get_result(r)
