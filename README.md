# ApplicationBot

Telegram-бот для приёма заявок от пользователей.

## Возможности

- команда `/start`;
- главное меню;
- выбор услуги;
- ввод имени;
- ввод телефона вручную или через Telegram Contact;
- подтверждение заявки;
- отмена заявки;
- отправка заявки администратору;
- сохранение заявки в PostgreSQL.

## Технологии

- Python
- aiogram 3
- PostgreSQL
- SQLAlchemy
- asyncpg
- python-dotenv

## Установка

Клонировать репозиторий:

```bash
git clone https://github.com/Nitto0/ApplicationBot.git
cd ApplicationBot
```

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать виртуальное окружение на Windows:

```bash
.venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Настройка PostgreSQL

Перед запуском необходимо создать базу данных PostgreSQL:

```text
application_bot
```

Например через pgAdmin.

## Настройка переменных окружения

Создать файл `.env` в корне проекта.

Пример содержимого:

```env
BOT_TOKEN=your_bot_token
ADMIN_ID=your_telegram_id
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/application_bot
```

Где:

- `BOT_TOKEN` — токен Telegram-бота;
- `ADMIN_ID` — Telegram ID администратора;
- `DATABASE_URL` — строка подключения к PostgreSQL.

Файл `.env` не должен загружаться в GitHub.

## Запуск

Запустить бота:

```bash
python bot.py
```

При первом запуске SQLAlchemy создаст необходимые таблицы в базе данных.

## Как работает бот

1. Пользователь запускает бота командой `/start`.
2. Выбирает пункт `Оставить заявку`.
3. Выбирает услугу.
4. Вводит имя.
5. Вводит номер телефона или отправляет контакт.
6. Проверяет данные заявки.
7. Подтверждает заявку.

После подтверждения заявка:

- сохраняется в PostgreSQL;
- отправляется администратору.

Пользователь также может отменить заполнение заявки командой:

```text
/cancel
```

## Структура проекта

```text
ApplicationBot/
├── bot.py
├── config.py
├── handlers/
│   ├── start.py
│   └── application.py
├── keyboards/
│   ├── reply.py
│   └── inline.py
├── states/
│   └── application.py
├── database/
│   ├── database.py
│   ├── models.py
│   └── requests.py
├── utils/
│   └── validators.py
├── data/
│   └── services.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```