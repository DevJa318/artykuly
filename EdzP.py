from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup as bs1
from urllib.request import URLError

try:
    #link = urlopen('http://www.pythonscraping.com/pages/page1.html')
    #link = urlopen('https://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie/Wyci%C4%85ganie_danych_z_dokumentu_HTML')
    link = urlopen('https://wiadomosci.onet.pl/uchodzcy')
    #link = urlopen('http://www.helion.pl')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    bs = bs1(link.read(),'html.parser')
    #print(bs.h3)
    #lista = bs.findall('h3')
    #print(lista)

    #zbior= bs.findAll('span',{'class':'author'})
    zbior = bs.findAll('h3')
    for nazwa in zbior:
        print(nazwa.get_text())
        
