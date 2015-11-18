# Buscaticket

Buscaticket es un buscador de tickets estil google per la plataforma gn6

## Instalació

Cal instalar el mongo 3 (important la versió 3 i no anteriors) i en principi qualsevol versió de Python

http://www.liquidweb.com/kb/how-to-install-mongodb-on-ubuntu-14-04/

Llavors cal instalar el driver de Python per mongo, el modul suds per webservices i el Flask per aplicacions web

```
$ sudo easy_install pymongo
$ sudo easy_install suds
$ sudo easy_install Flask
```

Fer una copia del settings_sample.py a settings_default.py i omplir els valors que hi ha al fitxer

Llavors, amb el mongo en marxa, omplir la BD amb els tickets
```
$ python omplir.py -c
```

## Execució

I llavors executar el servidor
```
$ python buscador.py
```

El buscador estarà disponible a

http://localhost:5000/

## Actualització dels indexos

Per executar els indexos amb els tickets oberts o tancats des de l'ultima actualització
```
python omplir.py 
```
