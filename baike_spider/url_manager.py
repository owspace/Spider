# -*- coding: UTF-8 -*-

# url管理器

class UrlManager(object):

    # url 管理器需要维护两个 url 列表：待爬取，已爬取
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()


    # 向 url 管理器中添加一个新的 url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)


    # 向 url 管理器中批量添加 urls
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断管理器中是否有新的待爬取 url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 从 url 中获取1个新的待爬取 url
    def get_new_url(self):
        new_url = self.new_urls.pop() # pop 方法会从列表中获取一个 url 并且移除这个 url
        self.old_urls.add(new_url)
        return new_url

