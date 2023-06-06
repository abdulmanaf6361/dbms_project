from django.urls import path
from .views import *

urlpatterns = [
    path("",signup),
    path("signup/",signup),
    path("success/",success),
]
