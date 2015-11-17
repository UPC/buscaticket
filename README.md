Cal instalar el mongo 3

http://www.liquidweb.com/kb/how-to-install-mongodb-on-ubuntu-14-04/

Llavors cal instalar el driver de Python, el modul suds i el Flask

$ sudo easy_install pymongo

$ sudo easy_install suds

$ sudo easy_install Flask

Fer una copia del settings_sample.py a settings_default.py i omplir els valors que hi ha al fitxer

Llavors, amb el mongo en marxa, omplir la BD amb els tickets

$ python omplir.py -c

I llavors executar el servidor

$ python buscardor.py

http://localhost:5000/

Successives invocacions nomes han d'executar python omplir.py per actualitzar els tickets
