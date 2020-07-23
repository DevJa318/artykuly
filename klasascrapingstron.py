
from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
from bs4 import BeautifulSoup

class Noweartykuly:
    def __init__(self, s: str, z:str, p:str):
        self.strona = s
        self.znacznik = z
        self.plik = p
    #def pobierz_a_do_listy(self):
        
    def pobranie_strony_artykulow(self):
        link = urlopen(self.strona)
        bs = BeautifulSoup(link.read(),'html.parser')
        lista = bs.findAll(self.znacznik)
        return self.lista

    def zapis_do_pliku(self):
        with open(self.plik, 'a+') as pl:
            zawartosc = pl.read()
            for line in self.lista:
                if line in zawartosc:
                    pass
                else:
                    print('NOWY: ', line)
                    pl.write(line)
                    pl.write('\n')


