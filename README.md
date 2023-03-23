# Yatube_API

## Описание
Социальная сеть для размещения текстовых постов на различные темы (с применением технологии API).

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/epatage/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры некоторых запросов через API

### Cоздание поста:
Отправить запрос по адресу:
```
http://127.0.0.1:8000/api/v1/posts/
```
с подобным содержимым (поле "text" обязательное):
```angular2html
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

### Получение всех комментариев к посту:
Отправить запрос по адресу:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
с подобным содержимым (поле "id" обязательное):
```angular2html
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    }
]
```

### Подписка на автора поста:
Отправить запрос по адресу:
```
http://127.0.0.1:8000/api/v1/follow/
```
с подобным содержимым (поле "following" обязательное):
```angular2html
{
  "following": "string"
}
```