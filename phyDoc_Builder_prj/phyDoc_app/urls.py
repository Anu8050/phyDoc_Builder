from django.urls import path
from phyDoc_app import views


urlpatterns = [

    path('',views.insert, name='insert'),
]