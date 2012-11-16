class HttpRedirectException(Exception):
    def __init__(self, response, *args, **kwargs):
        self.response = response
        super(HttpRedirectException, self).__init__(*args, **kwargs)
