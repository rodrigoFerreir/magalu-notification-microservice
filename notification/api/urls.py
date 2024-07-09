from django.urls import path
from .views import *


urlpatterns = [
    path('squedule', CreateSqueduledNotificationAPI.as_view(), name="notification"),
]