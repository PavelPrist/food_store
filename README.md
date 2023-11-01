# Food-store

Django-проект для магазина продуктов
## Стек технологий

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

### Использованные инструменты:

* Python
* Django REST Framework
* JWT + Djoser
* (полный список в файле requirements.txt)

### Реализован следующий функционал

* DONE Должна быть реализована возможность создания, редактирования, удаления категорий и подкатегорий товаров в админке.

* DONE Категории и подкатегории обязательно должны иметь наименование, slug-имя, изображение

* DONE Подкатегории должны быть связаны с родительской категорией

* DONE Должен быть реализован эндпоинт для просмотра всех категорий с подкатегориями. Должны быть предусмотрена пагинация.
* DONE Должна быть реализована возможность добавления, изменения, удаления продуктов в админке.
* DONE Продукты должны относится к определенной подкатегории и, соответственно категории, должны иметь наименование, slug-имя, изображение в 3-х размерах, цену
* DONE Должен быть реализован эндпоинт вывода продуктов с пагинацией. Каждый продукт в выводе должен иметь поля: наименование, slug, категория, подкатегория, цена, список изображений
* DONE Реализовать эндпоинт добавления, изменения (изменение количества), удаления продукта в корзине.
* DONE Реализовать возможность полной очистки корзины
* DONE Реализовать эндпоинт вывода  состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.
* DONE Операции по эндпоинтам категорий и продуктов может осуществлять любой пользователь
* DONE Операции по эндпоинтам корзины может осуществлять только авторизированный пользователь и только со своей корзиной
* DONE Реализовать авторизацию по токену


### Установка и запуск

1. Клонировать проект, создать и активировать виртуальное окружение, установить
зависимости

Для Windows:

```shell
git clone git@github.com:PavelPrist/food_store.git
cd Django-shop
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Для Linux:

```shell
git clone git@github.com:PavelPrist/food_store.git
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
(можно воспользоваться файлом базы db_example.sqlite3 для теста)

3. Создать суперпользователя и через админку заполнить БД (категории, подкатегории, продукты)
```shell
python manage.py createsuperuser
```
4. Запустить проект
```shell
python manage.py runserver
```

### API проекта
http://127.0.0.1:8000/  по адресу можно посмотреть 
все реализованные ендпоинты и примеры их выполнения(если заполнена база)

## Авторы
[Павел](https://github.com/PavelPrist)

## Ссылка не схему моделей
https://disk.yandex.ru/i/xpXoVPR9lD1gEQ