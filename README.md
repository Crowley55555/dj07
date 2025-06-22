# Django Telegram Bot Project

Этот проект представляет собой интеграцию Django REST API и Telegram-бота для регистрации и получения информации о пользователях Telegram.

## Возможности
- Регистрация пользователей Telegram через бота
- Получение информации о пользователе через бота
- REST API для работы с пользователями

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <repo-url>
   cd dj07
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Создайте файл `.env` в корне проекта и добавьте ваш токен Telegram-бота:
   ```env
   TELEGRAM_BOT_TOKEN=ваш_токен_бота
   ```
4. Примените миграции:
   ```bash
   python manage.py migrate
   ```

## Запуск

- Запустите Django сервер:
  ```bash
  python manage.py runserver
  ```
- Запустите Telegram-бота:
  ```bash
  python bot_main.py
  ```

## API

- `POST /api/register/` — регистрация пользователя
- `GET /api/user/<user_id>/` — получение информации о пользователе

## Структура проекта
- `bot/` — Django-приложение для работы с пользователями
- `bot_main.py` — основной файл Telegram-бота
- `djangotelebot/` — настройки Django-проекта

## Переменные окружения
- `TELEGRAM_BOT_TOKEN` — токен вашего Telegram-бота (обязательно)

## Лицензия
MIT

