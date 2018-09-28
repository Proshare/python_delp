import urllib

def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()  # 读取页面源代码


    return html