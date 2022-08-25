# microservice-for-statistics-counters
Простой микросервис для счетчиков статистики на REST API.

### Список некоторых используемых технологий/пакетов:
* djangorestframework==3.13.1
* flake8==5.0.4
* mysqlclient==2.1.0
* drf-yasg==1.21.3
* django-filter==22.1
* python-dotenv-0.20.0

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Alweee/microservice-for-statistics-counters.git
```

```
cd statistics_counter
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

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

## Примеры запросов:
Метод сохранения статистики: api/v1/statisitcs/

Ввод:
```
{
    "date": "2019-08-24",
    "views": 45,
    "clicks": 15,
    "cost": 19.3
}
```

Вывод:
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
