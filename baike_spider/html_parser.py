# -*- coding: UTF-8 -*-

# 网页解析器

import re
import urllib.parse
from bs4 import BeautifulSoup


class HtmlParser(object):

    # 方法1：获取 url 列表， 得到了所有词条的 url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # https://baike.baidu.com/item/Python/407313?fr=aladdin
        links = soup.find_all('a', href = re.compile(r"/item/+")) # 正则表达式
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 方法2：解析数据，得到了 h1 和 summary
    def _get_new_data(self, page_url, soup):
        # 首先建一个 res_data 存放数据，用一个字典
        res_data = {}

        # 最好把 url 也放进最终的数据中，方便最终的使用
        res_data['url'] = page_url

        # 获取 title 节点
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # 在获取 summary 节点
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_ = 'lemma-summary')
        if summary_node is None:
            return
        res_data['summary'] = summary_node.get_text()

        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser')

        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data
