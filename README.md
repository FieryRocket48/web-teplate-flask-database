# Шаблон веб-проекта на Python 

Этот проект представляет собой готовый шаблон для создания веб-приложений с использованием следующих технологий:

- **Python 3.12**
- **SQLite** в качестве базы данных
- **Flask** — микрофреймворк для веб-разработки
- **Flask-Bcrypt** — для хеширования паролей
- **Flask-Login** — для управления аутентификацией пользователей
- **Flask-Migrate** — для миграций базы данных
- **Flask-SQLAlchemy** — для работы с базой данных через ORM
- **Flask-WTF** — для работы с формами и валидацией

## 🔧 Настройка и 🚀 Запуск проекта

Для запуска проекта выполните следующие шаги:

1. **Переименуйте файл `.env.temp` в `.env`**  
   Этот файл содержит необходимые переменные окружения для работы проекта.

2. **Установите зависимости**  
   Выполните команду:
   ```bash
   pip install -r requirements.txt
   ```

3. **Перейдите в папку с проектом**  
   Рекомендуется использовать виртуальное окружение для изоляции зависимостей.

4. **Инициализируйте базу данных**  
   Выполните команду:
   ```bash
   flask db init
   ```

5. **Запустите сервер**  
   Выполните команду:
   ```bash
   flask run
   ```

6. **Перейдите по адресу**  
   Откройте браузер и перейдите по адресу:
   [http://127.0.0.1:5000/configure](http://127.0.0.1:5000/configure)  
   Здесь вы сможете выполнить первичную настройку и создать пользователя с правами администратора.

## 📂 Структура проекта

```
project/
│
├── app/                  # Основная папка приложения
│   ├── __init__.py       # Инициализация приложения
│   ├── models.py         # Модели базы данных
│   ├── routes.py         # Маршруты (роуты) приложения
│   ├── forms.py          # Формы для работы с Flask-WTF
│   ├── templates/        # HTML-шаблоны
│   └── static/           # Статические файлы (CSS, JS, изображения)
│
├── migrations/           # Папка для миграций базы данных, создатся после инцилизации
├── instance/             # Папка базы данных, создатся после инцилизации
├── .env                  # Шаблон файла переменных окружения
├── requirements.txt      # Список зависимостей
├── config.py             # Конфигурация приложения
└── run.py                # Точка входа для запуска приложения
```


# Python Web Project Template

This project is a ready-made template for creating web applications using the following technologies:

- **Python 3.12**
- **SQLite** as the database
- **Flask** — a microframework for web development
- **Flask-Bcrypt** — for password hashing
- **Flask-Login** — for user authentication management
- **Flask-Migrate** — for database migrations
- **Flask-SQLAlchemy** — for working with the database using ORM
- **Flask-WTF** — for working with forms and validation

## 🔧 Setup and 🚀 Project Launch

To launch the project, follow these steps:

1. **Rename the `.env.temp` file to `.env`**  
   This file contains the necessary environment variables for the project.

2. **Install dependencies**  
   Run the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Navigate to the project folder**  
   It is recommended to use a virtual environment to isolate dependencies.

4. **Initialize the database**  
   Run the following command:
   ```bash
   flask db init
   ```

5. **Start the server**  
   Run the following command:
   ```bash
   flask run
   ```

6. **Go to the address**  
   Open a browser and go to:
   [http://127.0.0.1:5000/configure](http://127.0.0.1:5000/configure)  
   Here you can perform the initial setup and create an administrator user.

## 📂 Project Structure

```
project/
│
├── app/                  # Main application folder
│   ├── __init__.py       # Application initialization
│   ├── models.py         # Database models
│   ├── routes.py         # Application routes
│   ├── forms.py          # Forms for working with Flask-WTF
│   ├── templates/        # HTML templates
│   └── static/           # Static files (CSS, JS, images)
│
├── migrations/           # Database migrations folder, created after initialization
├── instance/             # Database folder, created after initialization
├── .env                  # Environment variables file
├── requirements.txt      # List of dependencies
├── config.py             # Application configuration
└── run.py                # Entry point to run the application
```





