# Practica 5 Webscrapping.py
# Mauricio Alejandro Torres Luna 1809779

import requests
from bs4 import *
import os
from PIL import TAGS, GPSTAGS
from PIL import Image

# Este scrip nos permite descargar imagenes de un sitio web
# Se ejecuta en la consola de esta forma
# >python Webscrapping -link 'Link de la pagina'

def Images(url):
    r = requests.get('http://www.'+url)
    soup = BeautifulSoup(r.text, 'html.parser')
    urls = list()
    images = soup.select(img['src'])
    for img in images:
        urls.append(img['src'])
    global ruta
    ruta = input('Introduce la ruta y seleccione el nombre del directorio a crear: ')
    os.mkdir(ruta)
    i = 1
    for index, img_link in enumerate(urls):
        if i <= len(urls):
            img_data = request.get(img_link).content
            with open(ruta+'\\'+str(index+1)+'.jpg','wb+') as f:
                f.write(img_data)
            i += 1
        else:
            f.close()
            break
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArguentParser(description = 'El script descarga las imagenes del sitio que indiques e imprime la metadata de cada uno')
    parser.add_argument('-link', '-url', help='La ruta de donde quieras descargar las imagenes')
    args = parser.parse_args()
    url = args.url
    get_images(url)