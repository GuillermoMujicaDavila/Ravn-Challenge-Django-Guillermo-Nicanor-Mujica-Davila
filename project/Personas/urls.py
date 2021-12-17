# from django.contrib import admin
from django.urls import path
from .views import (PersonController, PeopleController)
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('person/<int:id>',PersonController.as_view()),
    path("people/", PeopleController.as_view())
]
