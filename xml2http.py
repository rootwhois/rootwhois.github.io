#coding=utf-8
import urllib
import urllib.request
import re
import xml.etree.cElementTree as et
url='https://rootwhois.cn/atom.xml'
file_name='atom.xml'
html=urllib.request.urlopen(url).read()
html=html.decode('utf-8')
with open(file_name, 'w') as f:
    f.write(html)

tree_obj = et.parse("atom.xml")
root = tree_obj.getroot()
# print(root.tag)
file = open('baidu_urls.txt', 'w')
for url in root.iter('{http://www.w3.org/2005/Atom}id'):
    # print(url.text)
    url.text = url.text.replace('https://', 'https://www.')
    file.write(url.text + '/r/n')
file.close()

