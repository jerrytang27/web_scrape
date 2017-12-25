from urllib.request import urlopen

url  = "https://s.taobao.com/search?q=Iphone&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20171204&ie=utf8&style=list"

def get_webpage(url):
    
    print("Getting Request Object")
    request = urlopen(url)
    print("Reading Request Object")
    data = request.read()
    text = data.decode("utf-8")
    
    print("Web Page Downloaded")
    return text

text = get_webpage(url)

with open('html_text.txt', 'w') as f:
    f.write(text)
