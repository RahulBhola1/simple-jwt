from .views import myfirstendpoint
from django.urls import path

urlpatterns = [
    path ('stds/' , myfirstendpoint , name="student-api")
]