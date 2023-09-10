from django.urls import path
from .views import TapList
from . import views

urlpatterns = [
    path('', TapList.as_view(), name='home'),
    path('new_tap/', views.new_tap, name='new_tap')
]
