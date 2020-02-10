class CotohaError(Exception):
    """Cotoha API exception"""

    def __init__(self, reason, header=None, body=None):
        self.reason = str(reason)
        self.header = header
        self.body = body
        super(Exception, self).__init__(self, reason)

    def __str__(self):
        return self.reason

class Response:
    def __init__(self, r):
        self.result = r["result"]
        self.status = r["status"]
        self.message = r["message"]