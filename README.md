به نام خدا
# گزارش کار آزمایش ۵ و ۶
- سید علیرضا هاشمی ۹۷۱۰۲۶۲۲
- مجتبی جعفری ۹۶۱۰۵۶۵۹
---------------------

می‌توانید معماری پروژه را در تصویر زیر مشاهده کنید:

![arch](https://user-images.githubusercontent.com/45389673/169655482-87eb9f21-0eb0-4ebf-bc36-22a0d65ab074.jpg)


# نحوه نصب و راه‌ندازی پروژه 

ما در این پروژه، سه سرویس مجزای مختلف داریم:
- پروژه‌ی جنگو که شامل دو اپِ core و scoring و دو دیتابیس sqlite است.
- سرویس celery که برای هندل‌کردن تسک‌ها به صورت async به کار می‌رود.
- سرویس rabbitMQ که یک صف است و توسط celery استفاده می‌شود.

## راه‌اندازی پروژه جنگو

دستورات زیر را به ترتیب اجرا کنید:

- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python3 manage.py migrate`
- `python3 manage.py migrate --database=scoring`
- `python3 manage.py createsuperuser`
- `python3 manage.py runserver`

## راه‌اندازی سرویس RabbitMQ

دستور زیر را اجرا کنید:

- `docker-compose up`

## راه‌اندازی سرویس celery

دستور زیر را اجرا کنید:

- `celery -A bike_system worker --loglevel=INFO`


توجه کنید که ابتدا باید سرویس RabbitMQ و سپس سرویس celery را اجرا کنید. هم‌چنین در تصویر زیر، چگونگی ارتباط celery و RabbitMQ را مشاهده می‌کنید:

![image](https://user-images.githubusercontent.com/45389673/169655518-530d238e-9beb-48dc-b43c-9764c79df8cf.png)


# endpoints

پس از اجرای پروژه‌ی جنگو، می‌توانید لیستی از endpoint ها را در آدرس `localhost:8000/swagger` مشاهده کنید.

# منابع

- https://levelup.gitconnected.com/introduction-to-message-queue-build-a-newsletter-app-using-django-celery-and-rabbitmq-in-30-min-6d484162391d
- https://github.com/Nancy-Chauhan/newsletter
