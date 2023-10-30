# Food-store

Django-проект для магазина продуктов

### Использованные инструменты:

* Python
* Django REST Framework
* JWT + Djoser

### Установка и запуск

1. Клонировать проект, создать и активировать виртуальное окружение, установить
зависимости

Для Windows:

```shell
git clone git@github.com:elityaev/Django-shop.git
cd Django-shop
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Для Linux:

```shell
git clone git@github.com:elityaev/Django-shop.git
cd Django-shop
python3 -m venv venv
source venv/bin/activat
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
2. Перейти в папку ```/food_store```, применить миграции 
```shell
python manage.py migrate
```
3. Создать суперпользователя и через админку заполнить БД (категории, подкатегории, продукты)
```shell
python manage.py createsuperuser
```
4. Запустить проект
```shell
python manage.py runserver
```