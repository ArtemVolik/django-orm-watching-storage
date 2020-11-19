# DJANGO ORM WATCHING STORAGE
Учебный проект по основам использовани ORM.
Подключенный к учебной базе, скрипт эмитирует охранный пульт управления. Вы можете сипользовать 
код верстки или посмотреть как реализованы запросы к БД. Учебная аза доступна только для учащихся.
#### 3 шаблона показывают:
 - активные пропуски в хранилище 
 - информацию о визитах по выбранному пропуску с продолжительностью и классификатором, является ли визит подозрительным.
- инофрмацию по активным визитам с продолжтельностью


## Установка и запуск
- Скопируйте файлы        
-  Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки 
зависимостей:  
```
pip install -r requirements.txt
```
- Чтобы подключить интерфейс к базе данных, создайте файл `.env` и добавьте в него соотвествующие поля настроек доступа. 
```
DB_ENGINE=put_here_the_database_backend_to_use
DB_HOST=put_here_your_database_host
DB_PORT=put_here_your_db_port
DB_NAME=put_here_db_nam
DB_USER=put_here_db_user_name
DB_PASSWORD=put_here_your_password
SECRET_KEY=put_here_your_secret_key
```

- Выполните в команндной строке, чтобы запустить сервер и просматривать интерфейс локально:

```
 python manage.py runserver 0.0.0.0:8000
``` 
    
- Для включения режима отладки поместите строку `DEBUG=true` в файл `.env`
