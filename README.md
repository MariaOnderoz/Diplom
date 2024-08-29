# Diplom

# **Cайт для бронирования столиков в ресторане**

### Описание задачи:

Необходимо создать сайт для бронирования столиков в ресторане. 
Сайт должен быть сверстан и подключен к админке. 
Для выполнения задачи необходимо использовать Django и Bootstrap. 
Сайт должен содержать основные разделы, необходимые для бронирования столиков и управления бронированиями.

### Функционал сайта:

1. **Главная страница**:
    - Описание ресторана.
    - Перечень предоставляемых услуг.
    - Контактная информация.
    - Форма для обратной связи.
2. **Страница бронирования**:
    - Форма для бронирования столика.
    - Просмотр доступности столиков.
    - Подтверждение бронирования.
3. **Личный кабинет**:
    - Регистрация и авторизация пользователей.
    - Просмотр истории бронирований.
    - Управление текущими бронированиями (изменение, отмена).
4. **Админка**:
    - Управление пользователями.
    - Управление бронированиями.
    - Управление контентом сайта (тексты, изображения и т.д.).

### Технические требования:

* Django
* PostgreSQL
* Bootstrap
* Docker
* Docker Compose


# Настройка

1. Для запуска пректа клонируйте репозиторий:

    https://github.com/MariaOnderoz/Diplom.git

2. Установите и активируйте виртуальное окружение:
   
    python3 -m venv env (для MacOS и Linux)
    python -m venv env (для windows)

    source venv/bin/activate (для MasOs и Linux)
    venv\Scripts\activate.bat (для windows)

3. Установите файл с зависимостями

    pip install -r requirements.txt

4. Заполните своими данными файл .env (образец в .env.sample)

5. Создайте базу данных в pgAdmin

# Использование

1. Локально:

    python3 manage.py runserver (для MasOs и Linux)
    python manage.py runserver (для windows)

2. Через Docker:

    docker-compose up -d --build
