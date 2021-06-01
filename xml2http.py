#coding=utf-8
import urllib
import urllib.request
import re
import xml.etree.cElementTree as et
url='https://blog.rootwhois.cn/sitemap.xml'
file_name='sitemap.xml'
u=urllib.request.urlopen(url)
print(u.getcode())
html=u.read()
html=html.decode('utf-8')
with open(file_name, 'w') as f:
    f.write(html)

tree_obj = et.parse("sitemap.xml")
root = tree_obj.getroot()
# print(root.tag)
file = open('baidu_urls.txt', 'w')
for url in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
    # print(url.text)
    file.write(url.text + '\n')
file.close()

