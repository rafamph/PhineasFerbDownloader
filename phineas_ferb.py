from bs4 import BeautifulSoup
import requests
import re
import wget
import time

response = requests.get("http://www.pyflatino.com/p/lista-de-episodios-de-phineas-y-ferb.html")
soup = BeautifulSoup(response.content, "html.parser")


url = []
final_urls = []
final_final_urls = []

for links in soup.findAll('a'):
    url.append(links.get('href'))
#print(url.index('http://pyflatino.blogspot.com/2014/01/episodio-01-phineas-y-ferb-la-montana.html'))
#print("not sure %s" % (url.index('http://pyflatino.blogspot.com/2014/09/episodio-131-132-phineas-y-ferb-star.html')))


repeated_episodes = (url[63:188])
#repeated_episodes = (url[63:65])

for download_links in repeated_episodes:
    requestsss = requests.get(download_links)
    soupsss = BeautifulSoup(requestsss.content, "html.parser")
    class_thingy = str(soupsss.findAll("div", { "class" : "contenedor-video"}))
    
    #if "a" not in class_thingy or class_thingy is None
    final_url = re.search('<iframe frameborder="0" height="360" src="(.*)" width="560"></iframe></div>]', class_thingy) 
    #print(type(final_url))

    if final_url is None:
        pass
    else:
        final_urls.append(final_url.group(1))

print("done")



for each in final_urls:
    f_requests = requests.get(each)
    f_soups = BeautifulSoup(f_requests.content, "html.parser")
    f_classes = str(f_soups.findAll("script", {"type" : {'text/javascript'}}))
    last_url = re.search("""(http://embed.myvideo.ge(.*)',)""", f_classes)
    if last_url is None:
        pass
    else:
        final_final_urls.append(last_url.group(1))



the_other = []



while True:
    for each in final_final_urls:
        wget.download(each)
        time.sleep(3*60)
        the_other.append(each)
    if len(the_other) == len(final_final_urls):
        break
