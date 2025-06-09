Django Ninja Blog API
Простой блог с API, написанный на Django и Django Ninja. Поддерживает авторизацию через сессию, документацию Swagger и работу в Docker.

✨ Возможности
CRUD-действия для постов (создание, чтение, обновление, удаление)

Swagger-документация по адресу /api/docs

Авторизация через сессионный вход в Django admin

PostgreSQL и Docker

🚀 Быстрый старт
1. Клонировать репозиторий
git clone https://github.com/yourname/blog-api.git
cd blog-api
2. Запустить Docker
docker-compose up --build
3. Провести миграции и создать суперпользователя
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
👁️ API Документация
Swagger доступен по адресу:

http://localhost:8000/api/docs
Можно:

Смотреть список маршрутов

Выполнять запросы напрямую из браузера

Авторизоваться через кнопку Authorize (работает после входа в админку)

🔐 Авторизация и Аутентификация
🔒 Через браузер
Зайди на http://localhost:8000/admin

Авторизуйся как суперпользователь

Перейди на http://localhost:8000/api/docs

Замочек закроется — теперь можно отправлять запросы

📊 Примеры эндпоинтов
GET /api/blog/posts — список постов

GET /api/blog/posts/{id} — один пост

POST /api/blog/posts — создать

PUT /api/blog/posts/{id} — обновить

DELETE /api/blog/posts/{id} — удалить