from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('month/<int:month>', views.month_by_number),
    path('month/<str:month>', views.month, name='month-challenges')
]
