from django.urls import path

from . import views

urlpatterns = [
    path('', views.L4_page, name='L4_page'),
    path('<int:f_id>/', views.L3_page, name='L3_page'),
]