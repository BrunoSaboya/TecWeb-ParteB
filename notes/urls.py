from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    
]


# Facil acesso aos comandos:
# docker run --rm --name pg-docker -e POSTGRES_PASSWORD=insper -d -p 5432:5432 -v C:\Users\lucam\docker\volumes\postgres:/var/lib/postgresql/data postgres
# python manage.py runserver
# env\Scripts\activate.bat