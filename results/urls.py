from django.urls import path
from . import views

urlpatterns = [
    path('', views.roll_number_input, name='roll_number_input'),
    path('result/<str:roll_no>/', views.result_page, name='result_page'),
]
