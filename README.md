# 📇 Portfolio

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-3.1.1-lightgrey?logo=flask)](https://flask.palletsprojects.com/) [![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)](https://www.docker.com/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791?logo=postgresql)](https://www.postgresql.org/) [![Nginx](https://img.shields.io/badge/Nginx-LB-009639?logo=nginx)](https://nginx.org/) [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


> 💼 Сайт-визитка на **Python (Flask)** c контейнеризацией и CI/CD.

🌐 **Демо**: [sibiryk.ru](https://sibiryk.ru)

---

## 📜 Описание проекта

**Portfolio** - это полнофункциональное веб-приложение для публикации краткой информации о проектах разработчика с использованием современных технологий.  
Проект включает регистрацию и авторизацию пользователей, панель администратора для управления контентом, хранение данных в PostgreSQL и автоматизированное развертывание с помощью Docker и CI/CD.

---

## 🏗 Архитектура и структура проекта

- Модельно-ориентированная архитектура (MVC):  
  - **Models** - ORM-модели для работы с базой данных (SQLAlchemy).  
  - **Forms** - формы регистрации, авторизации.
  - **Views** - Flask маршруты и обработчики запросов.  
  - **Templates** - Pug-шаблоны с использованием Stylus для стилей.  
- Аутентификация и авторизация реализованы через Flask-Login.  
- Админка реализована кастомно с возможностью загрузки графики и управления проектами.  
- Используется Nginx как обратный прокси и балансировщик с SSL сертификатами от Certbot.  
- Автоматизация тестирования и деплоя с GitHub Actions.

---

## 🛠 Технологии и инструменты

- **Язык:** Python 3.13  
- **Фреймворк:** Flask 3.1.1  
- **База данных:** PostgreSQL 17 (через SQLAlchemy ORM)  
- **Шаблонизатор:** Pug (pypugjs)  
- **Стили:** Stylus  
- **Контейнеризация:** Docker Compose  
- **CI/CD:** GitHub Actions (автоматический билд и деплой)  
- **Веб-сервер:** Nginx с SSL (Certbot)  
- **Капча:** Yandex Smart Captcha для защиты форм  

---

## 📦 Зависимости и требования

Проект использует следующие ключевые зависимости (полный список в `requirements.txt`):

- **Flask** 3.1.1 - веб-фреймворк  
- **Flask-Admin** 1.6.1 - админ-панель  
- **Flask-Login** 0.6.3 - аутентификация пользователей  
- **Flask-Migrate** 4.1.0 - миграции базы данных  
- **Flask-SQLAlchemy** 3.1.1 - ORM для работы с PostgreSQL  
- **SQLAlchemy** 2.0.41 - база для ORM  
- **psycopg2** 2.9.10 - PostgreSQL драйвер  
- **pytest** 8.4.1 - тестирование  
- **pypugjs** 5.12.0 - шаблонизатор Pug для Python  
- **WTForms** 3.1.2 - работа с формами  
- **gunicorn** 23.0.0 - WSGI сервер для продакшена  
- **python-dotenv** 1.1.1 - загрузка переменных окружения из `.env`  
- **certifi, requests, urllib3** - для работы с HTTP и сертификатами  

Версия Python: **3.13** (рекомендуется использовать виртуальное окружение).

---

## 🚀 Установка и запуск

1. Клонировать репозиторий:  
   ```bash
   git clone git@github.com:sibiry-k/portfolio.git
   ```
2. Перейти в директорию проекта:  
   ```bash
   cd portfolio
   ```
3. Получить и добавить ключи **Yandex Smart Captcha** в файл `.env` (см. `.env.example`).  
4. Запустить контейнеры:  
   ```bash
   docker compose up --build
   ```
5. Проект будет доступен по адресу [http://localhost](http://localhost) (по умолчанию).

---

## 🧪 Тестирование

- В проекте используется **pytest** для модульных и интеграционных тестов.  
- Покрытие тестами охватывает основные модели, маршруты и бизнес-логику.  
- Для запуска тестов выполните:  
  ```bash
  pytest
  ```
- Планируется расширение тестового покрытия и добавление end-to-end тестов.

---

## 📈 Планы на будущее

- Улучшить UX панели администратора, добавить роли пользователей.  
- Оптимизировать фронтенд, добавить SPA-элементы.  
- Расширить тестовое покрытие, добавить CI на тесты.  

---

## 🤝 Contributing

Проект открыт для вклада и предложений:

1. Форкнуть репозиторий.  
2. Создать ветку с фичей:  
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Сделать коммит с описанием изменений:  
   ```bash
   git commit -m "Add feature description"
   ```
4. Запушить ветку в свой форк:  
   ```bash
   git push origin feature/your-feature-name
   ```
5. Создать Pull Request на основной репозиторий.

---

## 📄 Лицензия

Проект лицензирован под **MIT**. Подробнее в файле [LICENSE](LICENSE).

---

## 📬 Контакты

- Telegram: [@sibirykdev](https://t.me/sibirykdev)  
- Сайт: [sibiryk.ru](https://sibiryk.ru)
```
