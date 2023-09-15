# currency_converter
Simple dockerized RESTful app with Django REST framework
### Starting:
### 1. Clone app from github
```shell
$ git clone git@github.com:RBstyle/currency_converter.git
$ cd currency_converter
```
### 2. Start docker compose.
```shell
$ docker compose up
```
___
### Описание функционала приложения
___

Приложение имеет один endpoint. В ответ на GET запрос с параметрами "`from`", "`to`" и "`value`" возвращает ответ с результатом конвертации валюты из одной в другую в количестве "`value`".
Пример: 

GET `http://0.0.0.0:8000/api/rates/?from=USD&to=RUB&value=1`

Возвращает:

```bash
{
    "result": 96.1609
}
```
Курсвалют берется с ресурса `https://www.cbr-xml-daily.ru/`.
