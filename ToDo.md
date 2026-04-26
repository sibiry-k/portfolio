# ToDo — тестовое покрытие

## Баг в conftest.py
- [ ] Исправить фикстуру `test_project`: передаёт `user_id=test_user.id`, которого нет в модели `Project`; добавить обязательные поля `stack`, `role`, `tasks`

---

## 1. Views

### `GET /` (index)
- [ ] Возвращает 200 при пустой БД
- [ ] Отображает все проекты из БД (title присутствует в HTML)
- [ ] При отсутствии проектов — страница рендерится без ошибок

### `GET /register`, `POST /register`
- [ ] GET возвращает 200
- [ ] POST с валидными данными → редирект на `/login`
- [ ] POST создаёт запись пользователя в БД
- [ ] POST с уже существующим username → flash-ошибка
- [ ] POST с некорректным email → ошибка валидации
- [ ] POST без обязательных полей → ошибка валидации
- [ ] Первый зарегистрированный пользователь получает `is_admin=True`
- [ ] Второй и последующий пользователь получает `is_admin=False`

### `GET /login`, `POST /login`
- [ ] GET возвращает 200
- [ ] POST с правильными данными → редирект на `/admin`
- [ ] POST с неверным паролем → ошибка формы
- [ ] POST с несуществующим пользователем → ошибка формы

### `GET /logout`
- [ ] Авторизованный пользователь → редирект на `/`
- [ ] Неавторизованный → 302 на `/login`

### `GET /lk`
- [ ] Авторизованный → 200, содержит username в HTML
- [ ] Неавторизованный → 302 на `/login`

### `GET /media_data/<filename>`
- [ ] Существующий файл → 200
- [ ] Несуществующий файл → 404

---

## 2. Models

### `User`
- [ ] `set_password` сохраняет хеш, а не plaintext
- [ ] `check_password(верный_пароль)` → `True`
- [ ] `check_password(неверный_пароль)` → `False`
- [ ] `username` уникален (IntegrityError при дублировании)
- [ ] `email` уникален (IntegrityError при дублировании)
- [ ] `__repr__` возвращает `username`

### `Project`
- [ ] Создаётся со всеми обязательными полями
- [ ] `img_path` может быть `None` (nullable)
- [ ] `title` уникален (IntegrityError при дублировании)

---

## 3. Forms

### `LoginForm`
- [ ] `validate_username` бросает `ValidationError` если пользователь не найден
- [ ] `validate_username` бросает `ValidationError` при неверном пароле
- [ ] `get_user` возвращает объект `User` для существующего username
- [ ] `get_user` возвращает `None` для несуществующего username

### `RegistrationForm`
- [ ] Не проходит валидацию без обязательных полей
- [ ] Не проходит валидацию с некорректным email

---

## 4. Admin

### `MyAdminIndexView.is_accessible`
- [ ] `True` — пользователь аутентифицирован и `is_admin=True`
- [ ] `False` — пользователь не аутентифицирован
- [ ] `False` — пользователь аутентифицирован, но `is_admin=False`

### `inaccessible_callback`
- [ ] Неаутентифицированный → редирект на `/login?next=...`
- [ ] Аутентифицированный не-admin → редирект на `/` с flash-сообщением

---

## 5. Captcha (мокирование `requests.post`)

### `YandexCaptchaMixin.validate_captcha`
- [ ] Отсутствующий токен → `(False, "Подтвердите, что вы не робот...")`
- [ ] Не настроен `CAPTCHA_SERVER_KEY` → `(False, "Серверный ключ капчи не настроен.")`
- [ ] `requests.post` бросает `RequestException` → `(False, "Ошибка соединения...")`
- [ ] Ответ содержит `status == "ok"` → `(True, ...)`
- [ ] Ответ содержит `status != "ok"` → ошибка капчи

---

## Приоритет реализации

| Приоритет | Группа |
|-----------|--------|
| Высокий | Views: register, login, logout, lk |
| Высокий | Models: User |
| Средний | Forms: LoginForm |
| Средний | Admin: is_accessible, inaccessible_callback |
| Низкий | Captcha (mock) |