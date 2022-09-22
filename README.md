# Microservice for statistics counters

### Описание:
Микросервис для счетчиков статистики. Сервис умеет взаимодействовать с клиентом при помощи REST API запросов. Также реализована валидация входных данных.

### Cтек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![Django REST Framework](https://img.shields.io/badge/MySQL-%20-008080)](https://www.mysql.com/)
[![](https://img.shields.io/badge/Unit--tests-%20-008080)](https://docs.djangoproject.com/en/4.1/topics/testing/overview/)
[![](https://img.shields.io/badge/drf__yasg-%20-008080)](https://drf-yasg.readthedocs.io/en/stable/)
[![](https://img.shields.io/badge/django__filters-%20-008080)](https://django-filter.readthedocs.io/en/stable/guide/usage.html)

### Шаблон наполнения `.env` файла:
- DB_ENGINE=db_engine
- DB_NAME=db_name
- USER=user
- PASSWORD=password
- DB_HOST=db_host
- DB_PORT=db_port
- SECRET_KEY=secret_key

### Как запустить проект:

**Клонировать репозиторий и перейти в него в командной строке:**

`https://github.com/Alweee/microservice-for-statistics-counters.git`

`cd statistics_counter`

**Cоздать и активировать виртуальное окружение:**

`python -m venv venv`

`source venv/bin/activate`

**Установить зависимости из файла requirements.txt:**

`python -m pip install --upgrade pip`

**pip install -r requirements.txt**

**Выполнить миграции:**

`python3 manage.py migrate`

**Запустить проект:**

`python manage.py runserver`

## API методы:
- Метод сохранения статистики
- Метод показа статистики
- Метод сброса статистики

## Метод показа статистики
Принимает на вход:
- **from** - дата начала периода (включительно)
- **to** - дата окончания периода (включительно)

Отвечает статистикой, отсортированной по дате. В ответе должны быть поля:
- **date** - дата события
- **views** - количество показов
- **clicks** - количество кликов
- **cost** - стоимость кликов
- **cpc** = cost/clicks (средняя стоимость клика)
- **cpm** = cost/views * 1000 (средняя стоимость 1000 показов)

## Метод сброса статистики
Удаляет всю сохраненную статистику.

## Примеры запросов:
**`POST` | Метод сохранения статистики: `/api/v1/statisitcs/`**

Request:
```
{
    "date": "2019-08-24",
    "views": 45,
    "clicks": 15,
    "cost": 19.3
}
```

Response:
```
{
    "id": 32,
    "date": "2019-08-24",
    "views": 45,
    "clicks": 15,
    "cost": 19.3,
    "cpc": 1.29,
    "cpm": 428.89
}
```
[Александр Воробьёв](https://github.com/Alweee/)
