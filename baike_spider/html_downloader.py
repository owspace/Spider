# -*- coding: UTF-8 -*-

# html下载器

import string
from urllib import request
from urllib.parse import quote

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        # 增修
        url_ = quote(url, safe=string.printable)
        response = request.urlopen(url_)

        if response.getcode() != 200:
            return None

        return response.read()
