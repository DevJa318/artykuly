from lxml import html
import requests

"""
    Aby rozwinąć projekt: klasy:



    NOWE STRONY:
        dla każdej osobny plik
        wyświetlanie strona + NOWE

    Dodać daty! 
"""

strona = 'https://www.osw.waw.pl/pl/search?text='

#lista --> 3 elementy --> xpathi[1] --> for iteration
#podziel
#lub.. nieparzyste for itertation
xpathi = ['/html/body/div[1]/div/div/section/div/div/div/div[2]/div[','',']/div[1]/h3/a/text()']


plik = 'listaartykulow.txt'

def pobierz_ostatnie_10(strona:str ,xpathi:list):
    """ostatnie 10 artykułów - pobiera tytuły """

    najnowsze10 = []
    link = strona
    r = requests.get(link)
    hmm = html.fromstring(r.text)

    for i in range(10):
        #!!!!!!!!!!
        xpathi[1] = str(i+1)
        xpath = ''.join(xpathi)
        text = hmm.xpath(xpath)
        #print(text)
        najnowsze10.append(text[0])
    return najnowsze10

def odczytaj_plik():
    f = open(plik,'r')
    content = f.read()
    return content

def dopisz_do_pliku(najnowsze10,content):
    f = open(plik,'a+')
    for line in najnowsze10:
        if line in content:
            pass
            #print('znalazło:')
        else:
            print('NOWY: ' , line )
            #print(line)
            f.write(line)
            f.write('\n')
    f.close()

najnowsze10 = pobierz_ostatnie_10(strona,xpathi)
content = odczytaj_plik()
dopisz_do_pliku(najnowsze10,content)


