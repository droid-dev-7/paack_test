# paack_test
CLI to know the weather of the cities of Barcelona using the 'eltiempo.com' api

## Instrucciones
Clona el repositorio del proyecto:
```bash
$ cd paack_test
```
Instala desde Pipfile, si hay uno:
```bash
$ pipenv install
```
The differents commands can inform about the average of the minimum and maximum
temperature during the week, and the temperature of the day.
```bash
eltiempo.py -today 'Gavá'
eltiempo.py -av_max 'Gavá'
eltiempo.py -av_min 'Gavá'
```          
