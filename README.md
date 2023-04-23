# PetProjectShop 

## **Stack:**

### **Frameworks:** Django, DRF
### **Databases:** Postgres, Redis
### **Queue:** Celery

## **Запуск проекта через Docker**
1. Клонируйте репозиторий на свой компьютер:
https://github.com/hahawait/PetProjectShop

2. Установите Docker и Docker Compose.

3. Запустите проект с помощью команды:
**docker-compose up --build**

UPD 

Эта команда запустит все контейнеры, необходимые для проекта: PostgreSQL, Redis, Django, Celery и Flower. Флаг --build используется для пересборки образов контейнеров, если они изменились с момента последнего запуска.

4. После запуска проекта вы можете открыть браузер и перейти по адресу **http://localhost:8000/**, чтобы увидеть работающий проект.

5. Для остановки контейнеров используйте команду:
**docker-compose down**

UPD

Эта команда остановит все запущенные контейнеры и удалит их.

6. Если вы хотите изменить настройки проекта, вы можете изменить файл *docker-compose.yml* и запустить команду **docker-compose up --build** снова, чтобы применить изменения.

## **Установка и запуск проекта (путь самурая)**
### Чтобы запустить проект, выполните следующие шаги:

1. Клонируйте репозиторий на свой компьютер:
https://github.com/hahawait/PetProjectShop

2. Установите зависимости из файла requirements.txt:
**pip install -r requirements.txt**

3. Создайте и настройте базу данных:
**python manage.py migrate**

4. Создайте административного пользователя:
**python manage.py createsuperuser**

5. Запустите сервер:
**python manage.py runserver**

### UPD
Для отправки писем после создания заказа понадобится установить и запустить Redis, Celery, Flower (для мониторинга). Последние два устанавливаются во 2 пункте "Установка и запуск проекта".

1. Запуск Celery: **celery -A server worker -l info**

UPD если не работает пробуй (eventlet лежит в requirements.txt, устанавливать отдельно не нужно):

**celery -A project worker -l info -P eventlet**

2. Запуск Flower: **celery -A server flower**

Я запускал через cmd на Windows 10 и GitBash, если возникнут проблемы шерстить офф доки и гайды индусов на ютубе.

### **Использование API**
1. Реализованы CRUD-запросы для каждого приложения. 

