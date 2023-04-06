from django.urls import path
from . import views

app_name = 'hydro'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_latest_data/', views.get_latest_data, name='get_latest_data'),
]
