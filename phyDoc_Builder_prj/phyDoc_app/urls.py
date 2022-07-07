from django.urls import path
from phyDoc_app import views


urlpatterns = [

    path('',views.insert, name='insert'),
    path('show/', views.show, name='show'),
    path('remove/<int:pk>', views.remove, name='remove'),
    
]