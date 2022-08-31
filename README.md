# Note Chest
Web приложение "Note Chest" для хранения полезных ссылок и заметок.

## Технологий
Реализовано по принципу микросервисов на Docker.
 - ЯП: Python 
 - Фреймворк: Flask 
 - SQL : SQLAlchemy (Postgres)

## Реализовано
- ### Сервис user
  - Отвечает за регистрацию и авторизацию новых пользователей.
  - Позволяет обновлять данные пользователя и удалять пользователя из БД. 
  - Получить список всех пользователей в БД
  - Получить данные пользователя по id

  #### API сервиса: 
  - api/user/register - регистрация
  - api/user/auth - авторизация
  - api/user/logout - logout
  - api/user/crud - обновление данных и удаление
  - api/user/get/all - получение списка пользователей
  - api/user/get - получение данных пользователя по id

## Установка

Выполнить команды: 

`git clone https://github.com/Kandrey1/NoteChest.git`

`cd NoteChest`

`docker-compose up --build -d`
