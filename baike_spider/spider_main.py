# -*- coding: UTF-8 -*-
"""
Created on 2018.04.04
@author:OW

目标：百度百科python词条以及相关词条网页--标题和简介
入口页：https://baike.baidu.com/item/Python/407313?fr=aladdin#1
url格式：词条页面url：/view/125370.htm
数据格式：
 - 标题：<dd class="lemmaWgt-lemmaTitle-title"></dd>
 - 简介：<div class="para" label-module="para">Python的创始人为Guido van Rossum。</div>
页面编码：UTF8

"""
# 总调度程序和入口程序，以一个入口的 URL 作为参数来爬取所有相关页面
# opt + 回车键:快速创建未定义的方法
# 加入循环判断 count
# 加入异常处理 try...except：选中，按Opt+Cmd+T


from baike_spider import url_manager, html_downloader, html_parser, html_outputer

# 这个 SpiderMain 所需要的功能由 URL 管理器、html下载器、html解析器、html输出器来实现
# 这些函数需要在各个函数中一一进行初始化
class SpiderMain(object):
    def __init__(self):

        # 管理器
        self.urls = url_manager.UrlManager()
        # 下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 解析器
        self.parser = html_parser.HtmlParser()
        # 输出器
        self.outputer = html_outputer.HtmlOutputer()


    # 定义 craw 方法，也就是爬虫的调度程序
    def craw(self, root_url):

        count = 1 # 记录当前爬取的是第几个 url

        # 将入口 url 添加进 url 管理器
        self.urls.add_new_url(root_url) # 向管理器中添加新的 url

        # 这时 url 管理器中已经有了url，我们就可以启动爬虫de循环
        while self.urls.has_new_url():
            try:
                # 当 url 管理器中有待爬取的 url 时，我们获取一个 url
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))

                # 启动 url 下载器，结果存储在 html_cont 中
                html_cont = self.downloader.download(new_url)

                # 下载完页面，调用解析器解析这个页面,得到新的 url（new_urls）以及新的数据（new_data)
                # 给解析器传入两个参数：当前爬取的 url(new_url) 以及下载好的页面数据(html_cont)
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                # 对解析出来的两个数据分别处理
                # 将 url 添加进 url 管理器
                self.urls.add_new_urls(new_urls) # 先管理器中添加批量 url
                # 同时收集数据
                self.outputer.collect_data(new_data)

                if count == 500:
                    break
                count += 1
            except Exception as e:
                print(str(e))
                # 根据报错信息提示错误

        self.outputer.output_html()



# 编写 main 函数
if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin' # 设置要爬取的入口 URL
    obj_spider = SpiderMain() # 创建一个类的对象 spider
    obj_spider.craw(root_url) # 调用 craw 方法启动爬虫

