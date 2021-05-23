# Databases-course-project

Project GitHub repo -- https://github.com/denysgerasymuk799/Databases-course-project.git

Hosted project link -- https://alice-in-weedland-app.herokuapp.com/

Video-presentation -- https://youtu.be/R2g_NRMFZn0


## Структура проекту

- queries.sql -- всі запити на SQL мові із прикладами, які можна заранити на своїх даних

- project_db.sql -- база даних проекту

- docs -- папка із схемою бази даних (у двох екземплярах щоб було видно що ми змінили після мідтерму), коротка презентацією, мокапом



## Налаштування та локальний запуск

1. Встановити необхідні пакети

```console
pip install -r requirements.txt
```

2. Створити свою локальну базу даних на Postgresql

- створити нову database
- заранити ./project.sql у Query Tool на цій створені базі даних

3. Якщо у вас інші налаштування сервера для бази даних, то зайдіть у ./db_config.py та змініть host, database, user, password 

4. Заранити ./app.py

5. Зайти на http://localhost:8000
   
6. Насолоджуватися зробленою роботою :-)
