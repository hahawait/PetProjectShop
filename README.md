# PetProjectShop 
## Django, DRF


### **Установка и запуск проекта**
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
Для отправки писем после создания заказа понадобится установить и запустить RabbitMQ, Celery, Flower (для мониторинга). Последние два устанавливаются во 2 пункте "Установка и запуск проекта".

1. Запуск Celery: celery -A server worker -l info
2. Запуск Flower: celery -A server flower
3. Запуск RabbitMQ (из директории с самим RabbitMQ): rabbitmq-service.bat start

Я запускал на через cmd на Windows 10 и GitBash, если возникнут проблемы шерстить офф доки и гайды индусов на ютубе.

### **Использование API**
1. Реализованы CRUD-запросы для каждого приложения. 

