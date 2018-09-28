import urllib
import gethtml
import re

# page = urllib.request.urlopen('http://tieba.baidu.com/p/1753935195')
# html = page.read()  # 读取页面源代码
# print(html)
# 写入到文件当中
html = gethtml.get_html("http://tieba.baidu.com/p/1753935195")

html=html.decode('utf-8')#python3

reg= 'src="(.+?\.jpg)" width'#正则表达式

reg_img=re.compile(reg)#预编译一下
imglist=reg_img.findall(html) #进行匹配
x=0
for img in imglist :
    # print(img)
# 下载图片s
    urllib.request.urlretrieve(img,"%s.jpg" %x)

    x+=1

# pageFile = open('pageCode.txt', 'wb+')
# # 以写的方式打开pageCode.txt
#
# pageFile.write(html)
# pageFile.close() #开了记得关



