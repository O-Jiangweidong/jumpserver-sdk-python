from jms_client.v1.models.instance import Instance


class Response(object):
    def __init__(self, net_response, ins_class=None, **kwargs):
        # base attrs
        self._next_url = ''
        self._previous_url = ''
        self._total = 0
        # other
        self._err_msg = ''
        self._http_status = 0
        self.ins_class = ins_class
        self._data = self._parse_data_from_resp(net_response)

    def is_success(self):
        return not bool(self.get_err_msg())

    def is_request_ok(self):
        return self._http_status < 500

    def get_err_msg(self):
        return self._err_msg

    def to_obj(self, attrs):
        if not self.ins_class or not issubclass(self.ins_class, Instance):
            return attrs
        return self.ins_class(**attrs)

    def _parse_data_from_resp(self, response):
        data = []
        self._http_status = response.status_code
        if response.status_code >= 400:
            self._err_msg = response.reason
            return data

        if response.text == '':
            return data
        try:
            data = response.json()
            if isinstance(data, list):
                self.total = len(data)
            else:
                self.total = data.get('count', 0)
                self._previous_url = data.get('previous') or ''
                self._next_url = data.get('next') or ''
                data = [self.to_obj(d) for d in data.get('results') or []]
        except Exception as e:
            self._err_msg = str(e)
        return data

    def get_data(self):
        return self._data
