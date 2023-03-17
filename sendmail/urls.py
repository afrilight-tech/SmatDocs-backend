from django.urls import path
from . import views

urlpatterns = [
    path('contactmail', views.contactmail, name="contactmail"),
]
