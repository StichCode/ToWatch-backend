import re
from urllib.parse import urlparse, urlunparse


class UrlParse:
    def __init__(self, url):
        self._u = url
        self.__parsed = self.__parse

    @property
    def next(self):
        self.__next_page()
        return self._u

    @property
    def __parse(self):
        return urlparse(self._u)

    def refresh_url(self, new_url):
        self._u = new_url

    def __next_page(self):
        params = self.__params
        for i, d in params.items():
            if isinstance(d, dict) and d.get("page") is not None:
                d["page"] = str(int(d["page"]) + 1)
        path = self.__un_split(params)
        self.collect_url(path)

    def collect_url(self, path):
        nn = []
        for ii, i in enumerate(tuple(self.__parsed)):
            if ii == 2:
                nn.append(path)
            else:
                nn.append(i)
        new = urlunparse(tuple(nn))
        self.refresh_url(new)

    def __un_split(self, params):
        return '/'.join(self.__collect_params(params))

    @property
    def __split_path(self):
        return [io for io in re.split('/', self.__parsed.path) if io]

    @property
    def __params(self):
        params = {}
        path = self.__split_path
        ii = None
        for i, r in enumerate(path):
            if ii == i:
                continue
            if r.startswith("m_act") or r.endswith("page"):
                ii = i + 1
                params[i] = {r: path[ii]}
            else:
                params[i] = r
        return params

    @staticmethod
    def __collect_params(params):
        _params = ['']
        for i, r in params.items():
            if isinstance(r, str):
                _params.append(r)
            else:
                _params.extend(list(r.keys()))
                _params.extend(list(r.values()))
        _params.append('')
        return _params