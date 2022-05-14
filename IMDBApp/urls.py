from django.urls import path
from  . import views

urlpatterns = [
    path('main',views.mainpage,name = 'main'),
    path('prediction',views.prediction,name ='prediction')


]