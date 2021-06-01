#coding=utf-8
import urllib
import urllib.request
import re
import xml.etree.cElementTree as et
hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Charset': 'utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive'}
site='https://blog.rootwhois.cn/sitemap.xml'
file_name='sitemap.xml'

r = urllib.request.Request(site, headers=hdr)
response = urllib.request.urlopen(r)
res = response.read().decode('utf-8')


with open(file_name, 'w') as f:
    f.write(res)

tree_obj = et.parse("sitemap.xml")
root = tree_obj.getroot()
# print(root.tag)
file = open('baidu_urls.txt', 'w')
for url in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
    # print(url.text)
    file.write(url.text + '\n')
file.close()

