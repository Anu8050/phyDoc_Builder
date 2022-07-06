from django.urls import path
from phyDoc_app import views


urlpatterns = [

    path('create',views.insert, name='insert'),
]