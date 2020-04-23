import re
from pprint import pprint
from urllib.parse import urlparse, urlunparse, urlsplit, urljoin

BASE_URL = 'https://www.kinopoisk.ru/top/navigator/m_act[years]/1890%3A2020/m_act[num_vote]/10/m_act[rating]' \
           '/1%3A/m_act[tomat_rating]/1%3A/m_act[review_procent]/1%3A/m_act[is_film]/on/order/rating/perpage/200/page/1/#results'


class UrlParse:
    def __init__(self, url):
        self._u = url
        self.__parsed = self.__parse

    @property
    def next(self):
        self.collect_url()
        return self._u

    @property
    def __parse(self):
        return urlparse(self._u)

    def refresh_url(self, new_url):
        self._u = new_url

    def collect_url(self):
        path = self.__un_split()
        nn = []
        for ii, i in enumerate(tuple(self.__parsed)):
            if ii == 2:
                nn.append(path)
            else:
                nn.append(i)
        new = urlunparse(tuple(nn))

        self.refresh_url(new)

    def __un_split(self):
        return '/'.join(self.__collect_params(self.__next_page()))

    def __next_page(self):
        params = self.__params
        for i, d in params.items():
            if isinstance(d, dict) and d.get("page") is not None:
                d["page"] = str(int(d["page"]) + 1)
        return params

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


if __name__ == '__main__':
    s = UrlParse
    url = BASE_URL
    for i in range(1, 55):
        url = s(url).next
        print(url)
