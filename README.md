# 📇 Portfolio

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791?logo=postgresql)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/Nginx-LB-009639?logo=nginx)](https://nginx.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> 💼 Сайт-визитка для демонстрации навыков работы с **Flask**, **Docker Compose**, **Nginx** и **CI/CD**.

🌐 **Демо**: [sibiryk.ru](https://sibiryk.ru)

---

## 📜 Описание

**Portfolio** — это веб-приложение, позволяющее публиковать краткую информацию о проектах, в которых принимал участие разработчик.  
Данные хранятся в базе **PostgreSQL**, фронтенд реализован на **Pug** и **Stylus**, развертывание автоматизировано с помощью Docker и CI/CD.

---

## ✨ Функциональность

- 🗂 Публикация информации о проектах с загрузкой графики.
- 🔑 Регистрация и авторизация пользователей c поддержкой Captcha.
- 🛠 Панель администратора с управлением контентом.
- 🗄 Хранение данных в PostgreSQL.
- 🎨 Верстка на Jinja + Pug + Stylus.
- 📦 Контейнеризация через Docker Compose.
- 🌐 Балансировка трафика через **Nginx**.
- 🔒 Поддержка HTTPS с помощью **Certbot**.
- 🚀 Автоматическое деплой с использованием GitHub Actions.

---

## 🛠 Технологии

- **Язык:** Python  
- **Фреймворк:** Flask  
- **База данных:** PostgreSQL  
- **Шаблонизатор:** Jinja + Pug  
- **Стили:** Stylus  
- **Инфраструктура:** Docker Compose, GitHub Actions, Nginx, Certbot

---

## 🚀 Установка и запуск

1. Клонировать репозиторий:  
   ```bash
   git clone <url-репозитория>
   ```
2. Перейти в папку проекта:  
   ```bash
   cd portfolio
   ```
3. Получить ключи **Yandex Smart Captcha**.  
4. Заполнить файл `.env` по образцу `.env.example`.  
5. Запустить приложение:  
   ```bash
   docker compose up --build
   ```

---

## 📈 Планы на будущее

- 🔹 Добавить мультиязычность.
- 🔹 Расширить возможности панели администратора.
- 🔹 Оптимизировать фронтенд и добавить анимации.
- 🔹 Улучшить тестовое покрытие.

---

## 🤝 Contributing

Буду рад любым предложениям и улучшениям!

1. Сделайте форк проекта.  
2. Создайте новую ветку:  
   ```bash
   git checkout -b feature/название
   ```
3. Внесите изменения и сделайте коммит:  
   ```bash
   git commit -m "Добавил новую фичу"
   ```
4. Отправьте изменения в свою ветку:  
   ```bash
   git push origin feature/название
   ```
5. Создайте Pull Request.

---

## 📄 Лицензия

Проект распространяется под лицензией **MIT**.  
Подробнее см. файл [LICENSE](LICENSE).

---

## 📬 Контакты

- Telegram: [@sibirykdev](https://t.me/sibirykdev)  
- Сайт: [sibiryk.ru](https://sibiryk.ru)
```