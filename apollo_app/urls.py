
from django.contrib import admin
from django.urls import path
from apollo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('login/',views.login),
    path('safe_a/',views.safe_a)

    path('safe_b/',views.safe_b)
]
