import requests
import re
import urllib.parse


def download_images(dirname: str, url: str):
    url += 'pages'
    def result():
        r = requests.get(url)
        return r.text
        
    text = result()
        
    pattern = r'\/\/(.*?)(?=\")'
    urls = re.findall(pattern, text)
    
    def is_right_url(i):
        if ('SMALL' not in i) and ('PREVIEW' not in i):
            return True
        else:
            return False
    def short_url_to_full(url):
        url = 'https://' + url
        return url    
    right_urls = list(map(short_url_to_full, filter(is_right_url, urls)))
    
    
   
    
    #### TODO
    for i in range(len(right_urls)):
        with open(f'{dirname}/{i+1}.jpg', 'wb') as file:
            url = right_urls[i]
            url = urllib.parse.quote(url.replace('\\', '/'), safe=':/')
            file.write(requests.get(url).content)
    return dirname