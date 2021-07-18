# paack_test
CLI to know the weather of the cities of Barcelona using the 'eltiempo.com' api

## Instructions
Clone the project's repository:
```bash
$ cd paack_test
```
Install dependencies from Pipfile:
```bash
$ pipenv install
```
Move to app folder
```bash
$ cd app
```
The differents commands can inform about the average of the minimum and maximum
temperature during the week, and the temperature of the day.
```bash
eltiempo.py -today 'Gavà'
eltiempo.py -av_max 'Gavà'
eltiempo.py -av_min 'Gavà'
```          
