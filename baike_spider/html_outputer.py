# _*_ coding: UTF-8 _*_

# html输出器

class HtmlOutputer(object):

    # 首先我们需要一个列表来维护所搜集的数据
    def __init__(self):
        self.datas = []


    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    # 将收集好的数据写出到 html 文件中，打开这个文件便能看到收集好的数据
    def output_html(self):
        # 首先我们建立一个文件的输出对象
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<html>')
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write('<body>')
        fout.write('<a>')

        # Python2 默认编码 Ascii
        for data in self.datas:
            # fout.write('<tr>')
            # fout.write('<td>%s</td>' % data['url'])
            # fout.write('<td>%s</td>' % data['title'])
            # fout.write('<td>%s</td>' % data['summary'])
            # fout.write('<tr>')
            fout.write('<a href="%s">%s</a>' % (data['url'], data['title']))
            fout.write('<p>%s</p>' % data['summary'])

        fout.write('</a>')
        fout.write('</body>')
        fout.write('</html>')


        fout.close()