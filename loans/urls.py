from django.urls import path
from loans import views

urlpatterns = [
    path('', views.sign_in, name='signin'),
    path('index', views.index, name='index'),
    path('reports', views.blank, name='reports'),
    path('notify', views.notify, name='notify'),
]
