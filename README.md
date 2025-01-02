# db_project
Project for "Database management" discipline in the university

---

#### Предварительные требования

- установленный Docker Desktop

#### Порядок установки

- добавить в **./hotel/hotel/** файл .env
- добавить в него следующий текст:
```
DEBUG=True
SECRET_KEY={{ ВАШ КЛЮЧ }}
ALLOWED_HOSTS={{ ВАШ ВНЕШНИЙ IP }}

DATABASE_NAME=hotel
DATABASE_USER=postgres
DATABASE_PASSWORD=1234
DATABASE_HOST=db
DATABASE_PORT=5432

LANGUAGE_CODE=ru
TIME_ZONE=Europe/Moscow
```

__Чтобы посмотреть IP-адрес на Windows, надо в CMD вбить команду ipconfig, в выведенном тексте найти Ethernet adapter vEthernet (WSL (Hyper-V firewall)) ->  IPv4 Adress__

__В качестве ключа можно написать просто test__

- В корневой папке проекта открыть терминал и запустить следующую команду:
```
docker compose up --build
```
после чего начнется процесс сборки контейнеров

- далее перейдите по адресу **{{ ВАШ IP }}:8000**, проект запущен