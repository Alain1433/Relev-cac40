import string
from html import parser
from tokenize import String
import requests
import html.parser
import html

def getR(txt):
    return requests.get(txt)


if __name__ == '__main__':
    full = getR("https://www.google.com/finance/quote/PX1:INDEXEURO?hl=fr").text
    #print(full)
    debut_balise = '["PX1","INDEXEURO"],"CAC 40",'
    lines = full.splitlines()
    html.parser.HTMLParser().feed(full)
    x = full.split(debut_balise, 1)
    z = x.pop(1)
    #print(x)
    deb = z.rfind('[')
    fin = z.rfind(']')
    liste_finale = z.split(',')
    out = liste_finale.count(",")
    print(x)
    print("--------------------------------------------------------**************************************************---------")
    print(z) 
