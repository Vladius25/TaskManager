# TaskManager

Сервис, позволяющий пользователю ставить себе задачи, отражать в системе
изменение их статуса и просматривать историю задач.

## Технологии
- Python 3.7
- Django 3
- PostgreSQL 12
- Docker

## Описание API

#### Пользователь может зарегистрироваться в сервисе задав пару логин-пароль.

- POST /register/

Запрос:
```
{
    "username": str
    "password": str
}
```

Ответ *(HTTP_201_CREATED)*:
```
{
    "username": str
    "token": str
}
```

#### В системе может существовать много пользователей
Используются встроенные Django пользователи (модель User).

#### Пользователь может авторизоваться в сервисе предоставив парулогин-пароль и получив в ответе токен

- POST /login/

Запрос:
```
{
    "username": str
    "password": str
}
```

Ответ *(HTTP_200_OK)*:
```
{
    "token": str
}
```

#### Пользователь видит только свои задачи

- GET /api/v1/tasks/

Пользователь определяется по переданному в заголовке *Authorization* токену.
В выборку попадают только задачи это пользователя посредством *queryset.filter*.

- GET /api/v1/tasks/<task_id>

Пользователь определяется по переданному в заголовке *Authorization* токену.
Пользователь видит задачу, если она его. Иначе *HTTP_403_FORBIDDEN*.
За проверку отвечает *permissions*.

Ответ *(HTTP_200_OK)*:
```
{
    "id": int
    "owner": str
    "name": "str
    "description": str
    "creation_date": str
    "end_date": str
    "status": str
}
```

#### Пользователь может создать себе задачу

- POST /api/v1/tasks/

Запрос:
```
{
    "name": str
    "description": str
    "end_date": str/null
    "status": str
}
```

Ответ *(HTTP_201_CREATED)*:
```
 {
     "id": int
     "owner": str
     "name": str
     "description": str
     "creation_date": str
     "end_date": str
     "status": str
 }
```

#### Пользователь может менять задачу

- PATCH /api/v1/tasks/<task_id>

Запрос:
```
{
    "status": str
}
```

Ответ *(HTTP_200_OK)*:
```
{
    "id": int
    "owner": str
    "name": str
    "description": str
    "creation_date": str
    "end_date": str
    "status": str
}
```

#### Пользователь может получить список задач своих задач с возможностью фильтрации по статусу и планируемому времени завершения

- GET /api/v1/tasks/?status=str
- GET /api/v1/tasks/?from_date=str&to_date=str

Ответ *(HTTP_200_OK)*:
```
[
  {
      "id": int
      "owner": str
      "name": "str
      "description": str
      "creation_date": str
      "end_date": str
      "status": str
  },
]
```

#### Возможность просмотреть историю изменений задачи
- GET /api/v1/tasks/history/<task_id>

Реализовано посредством модуля *django-simple-history*.

Ответ *(HTTP_200_OK)*:
```
[
    {
        "name": str,
        "description": str,
        "status": str,
        "end_date": str,
        "update_date": str
    },
    {
        "name": str,
        "description": str,
        "status": str,
        "end_date": str,
        "update_date": str
    },
]
```

